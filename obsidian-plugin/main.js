/*
 * Note Site Builder — an Obsidian front-end for site/build.py.
 *
 * The Python scripts stay the one renderer (GitHub Actions runs them too); this
 * plugin finds the project the open note belongs to and runs them for you:
 * build, build with PDFs, live preview, open, and publish (commit + push).
 *
 * A "project" is any folder in the vault with a site/build.py in it.
 */
const {
	Plugin, Notice, Menu, Modal, Setting, PluginSettingTab, SuggestModal,
	FileSystemAdapter, Platform, MarkdownView,
} = require("obsidian");
const { spawn, execFile } = require("child_process");
const fs = require("fs");
const path = require("path");

const BUILDER = path.join("site", "build.py");
const DEFAULTS = { python: "", port: 8321, project: "" };

function run(cmd, args, opts = {}) {
	return new Promise((resolve) => {
		execFile(cmd, args, { timeout: 60000, maxBuffer: 1 << 24, ...opts }, (err, stdout, stderr) =>
			resolve({ ok: !err, code: err ? err.code : 0, stdout: String(stdout), stderr: String(stderr) }));
	});
}

function openExternal(target) {
	try {
		const { shell } = require("electron");
		return /^https?:/.test(target) ? shell.openExternal(target) : shell.openPath(target);
	} catch (e) {
		window.open(/^https?:/.test(target) ? target : "file://" + target);
	}
}

/** Warnings from build.py are the stderr lines that start with "!". */
function warnings(stderr) {
	return stderr.split("\n").map((l) => l.trim()).filter((l) => l.startsWith("!"));
}

module.exports = class NoteSiteBuilder extends Plugin {
	async onload() {
		this.settings = Object.assign({}, DEFAULTS, await this.loadData());
		this.server = null;   // { proc, project, port }
		this.busy = false;

		this.status = this.addStatusBarItem();
		this.status.addClass("nsb-status");
		this.status.onClickEvent((evt) => this.showMenu(evt));
		this.refreshStatus();

		this.addRibbonIcon("globe", "Handout website", (evt) => this.showMenu(evt));

		this.addCommand({ id: "build", name: "Build website", callback: () => this.build(false) });
		this.addCommand({ id: "build-pdf", name: "Build website and PDFs", callback: () => this.build(true) });
		this.addCommand({ id: "preview", name: "Start/stop live preview", callback: () => this.togglePreview() });
		this.addCommand({ id: "open", name: "Open built website", callback: () => this.openSite() });
		this.addCommand({ id: "open-pdf", name: "Open handout PDF", callback: () => this.openPdf() });
		this.addCommand({ id: "publish", name: "Publish (commit and push)", callback: () => this.publish() });
		this.addCommand({ id: "open-published", name: "Open published website", callback: () => this.openPublished() });

		this.addSettingTab(new SettingsTab(this.app, this));
	}

	onunload() {
		this.stopPreview(true);
	}

	async saveSettings() {
		await this.saveData(this.settings);
	}

	// ---------- menu and status ----------

	showMenu(evt) {
		const menu = new Menu();
		const add = (title, icon, fn) => menu.addItem((i) => i.setTitle(title).setIcon(icon).onClick(fn));
		add("Build website", "hammer", () => this.build(false));
		add("Build website + PDFs", "file-down", () => this.build(true));
		add(this.server ? "Stop live preview" : "Start live preview", this.server ? "square" : "play",
			() => this.togglePreview());
		menu.addSeparator();
		add("Open built website", "globe", () => this.openSite());
		add("Open handout PDF", "file-text", () => this.openPdf());
		menu.addSeparator();
		add("Publish (commit and push)…", "upload-cloud", () => this.publish());
		add("Open published website", "external-link", () => this.openPublished());
		menu.showAtMouseEvent(evt);
	}

	refreshStatus() {
		this.status.empty();
		if (this.busy) this.status.setText("⏳ Building site…");
		else if (this.server) this.status.setText(`● Site preview :${this.server.port}`);
		this.status.toggle(Boolean(this.busy || this.server));
		this.status.setAttr("aria-label", this.server ? "Click for site options" : "");
	}

	// ---------- finding things ----------

	vaultRoot() {
		const adapter = this.app.vault.adapter;
		return adapter instanceof FileSystemAdapter ? adapter.getBasePath() : null;
	}

	/** Every folder in the vault holding a site/build.py, as absolute paths. */
	allProjects() {
		const root = this.vaultRoot();
		const found = new Set();
		for (const file of this.app.vault.getFiles()) {
			if (file.name === "build.py" && file.parent && file.parent.name === "site") {
				const dir = file.parent.parent;
				found.add(path.join(root, dir.path === "/" ? "" : dir.path));
			}
		}
		if (this.settings.project) {
			const p = path.resolve(root, this.settings.project);
			if (fs.existsSync(path.join(p, BUILDER))) found.add(p);
		}
		return [...found].sort();
	}

	/** The project the open note sits in, else the chosen default, else ask. */
	async project() {
		const root = this.vaultRoot();
		if (!root) {
			new Notice("Note Site Builder needs a vault on the local disk.");
			return null;
		}
		const file = this.app.workspace.getActiveFile();
		if (file) {
			let dir = path.dirname(path.join(root, file.path));
			while (dir.startsWith(root)) {
				if (fs.existsSync(path.join(dir, BUILDER))) return dir;
				const up = path.dirname(dir);
				if (up === dir) break;
				dir = up;
			}
		}
		const all = this.allProjects();
		if (this.settings.project) {
			const p = path.resolve(root, this.settings.project);
			if (all.includes(p)) return p;
		}
		if (all.length === 1) return all[0];
		if (!all.length) {
			new Notice("No website project found: no folder in this vault has a site/build.py.");
			return null;
		}
		return new Promise((resolve) => new ProjectPicker(this.app, all, root, resolve).open());
	}

	/**
	 * The Python to run: the setting, else the first python3 that can import the
	 * builder's packages, else the first python3 found at all.
	 */
	async python() {
		if (this.settings.python) return this.settings.python;
		if (this.detectedPython) return this.detectedPython;
		const candidates = [];
		// Apps started from the Dock don't see the shell's PATH (conda, Homebrew),
		// so ask a login shell for every python3 it knows.
		if (!Platform.isWin) {
			const shell = process.env.SHELL || "/bin/zsh";
			const res = await run(shell, ["-l", "-i", "-c", "which -a python3"], { timeout: 10000 });
			candidates.push(...res.stdout.split("\n").map((l) => l.trim()).filter((l) => l.startsWith("/")));
			const home = require("os").homedir();
			for (const conda of ["anaconda3", "miniconda3", "miniforge3", "mambaforge"]) {
				candidates.push(path.join(home, conda, "bin", "python3"));
			}
			candidates.push("/opt/homebrew/bin/python3", "/usr/local/bin/python3", "/usr/bin/python3");
		} else {
			candidates.push("python", "py");
		}
		const unique = [...new Set(candidates)].filter((c) => !path.isAbsolute(c) || fs.existsSync(c));
		for (const py of unique) {
			if ((await run(py, ["-c", "import markdown, openpyxl"], { timeout: 15000 })).ok) {
				return (this.detectedPython = py);
			}
		}
		return unique[0] || "python3"; // not cached: a pip install may fix it
	}

	/** Check the Python has the builder's packages, and say how to fix it if not. */
	async checkPython(py, project) {
		const res = await run(py, ["-c", "import markdown, openpyxl"], { cwd: project });
		if (res.ok) return true;
		const missing = /No module named '([^']+)'/.exec(res.stderr);
		new Notice(
			missing
				? `Python (${py}) is missing “${missing[1]}”.\nRun: ${py} -m pip install -r site/requirements.txt`
				: `Can't run Python at “${py}”. Set its path in Settings → Note Site Builder.`,
			15000,
		);
		return false;
	}

	// ---------- actions ----------

	async build(withPdf) {
		if (this.busy) return new Notice("A build is already running.");
		const project = await this.project();
		if (!project) return;
		const py = await this.python();
		if (!(await this.checkPython(py, project))) return;

		// Obsidian writes edits to disk on a short delay; flush before building.
		await this.app.workspace.getActiveViewOfType(MarkdownView)?.save();

		this.busy = true;
		this.refreshStatus();
		const started = new Notice(withPdf ? "Building website and PDFs…" : "Building website…", 0);
		const res = await new Promise((resolve) => {
			const proc = spawn(py, ["-u", BUILDER, ...(withPdf ? ["--pdf"] : [])], { cwd: project });
			let stdout = "", stderr = "";
			proc.stdout.on("data", (d) => (stdout += d));
			proc.stderr.on("data", (d) => (stderr += d));
			proc.on("error", (err) => resolve({ code: -1, stdout, stderr: stderr + String(err) }));
			proc.on("close", (code) => resolve({ code, stdout, stderr }));
		});
		started.hide();
		this.busy = false;
		this.refreshStatus();

		if (res.code !== 0) {
			console.error("[note-site-builder] build failed\n", res.stderr);
			const last = res.stderr.trim().split("\n").pop() || "unknown error";
			return new Notice(`Website build failed:\n${last}\n(Details in the developer console.)`, 15000);
		}
		const warn = warnings(res.stderr);
		if (warn.length) console.warn("[note-site-builder]\n" + warn.join("\n"));
		const pages = (res.stdout.match(/^built /gm) || []).length;
		new Notice(
			`Website built (${pages} file${pages === 1 ? "" : "s"}).` +
				(warn.length ? `\n${warn.length} warning(s):\n${warn.slice(0, 4).join("\n")}` : ""),
			warn.length ? 12000 : 4000,
		);
		return true;
	}

	async togglePreview() {
		if (this.server) return this.stopPreview();
		const project = await this.project();
		if (!project) return;
		const py = await this.python();
		if (!(await this.checkPython(py, project))) return;
		if (!fs.existsSync(path.join(project, "site", "serve.py"))) {
			return new Notice("This project has no site/serve.py for live preview.");
		}

		const port = Number(this.settings.port) || DEFAULTS.port;
		const url = `http://localhost:${port}`;
		const proc = spawn(py, ["-u", path.join("site", "serve.py"), String(port)], { cwd: project });
		this.server = { proc, project, port };
		this.refreshStatus();

		let stderr = "", opened = false;
		proc.stdout.on("data", (d) => {
			if (!opened && String(d).includes("serving http")) {
				opened = true;
				new Notice(`Live preview at ${url} — it rebuilds each time you save.`);
				openExternal(url);
			}
		});
		proc.stderr.on("data", (d) => {
			stderr += d;
			for (const line of warnings(String(d))) {
				if (line.startsWith("! build failed")) new Notice(`Preview: ${line.slice(2)}`, 8000);
			}
		});
		proc.on("close", (code) => {
			if (this.server && this.server.proc === proc) {
				this.server = null;
				this.refreshStatus();
				if (!this.stopping) {
					console.error("[note-site-builder] preview stopped\n", stderr);
					const inUse = /Address already in use/.test(stderr);
					new Notice(inUse
						? `Port ${port} is taken — is another preview running? Change it in settings.`
						: `Live preview stopped (exit ${code}). ${stderr.trim().split("\n").pop() || ""}`, 10000);
				}
			}
			this.stopping = false;
		});
		proc.on("error", (err) => new Notice(`Could not start preview: ${err.message}`));
	}

	stopPreview(quiet) {
		if (!this.server) return;
		this.stopping = true;
		this.server.proc.kill();
		this.server = null;
		this.refreshStatus();
		if (!quiet) new Notice("Live preview stopped.");
	}

	async openSite() {
		if (this.server) return openExternal(`http://localhost:${this.server.port}`);
		const project = await this.project();
		if (!project) return;
		const page = path.join(project, "site", "index.html");
		if (!fs.existsSync(page) && !(await this.build(false))) return;
		openExternal(page);
	}

	async openPdf() {
		const project = await this.project();
		if (!project) return;
		const dir = path.join(project, "site");
		const find = () => fs.readdirSync(dir).filter((f) => f.endsWith(".pdf"))
			.sort((a, b) => Number(b.includes("handout")) - Number(a.includes("handout")));
		let pdfs = find();
		if (!pdfs.length) {
			if (!(await this.build(true))) return;
			pdfs = find();
			if (!pdfs.length) return new Notice("No PDF was made — is Chrome installed?");
		}
		openExternal(path.join(dir, pdfs[0]));
	}

	/** https://<owner>.github.io/<repo>/ for a GitHub origin. */
	async publishedUrl(project) {
		const res = await run("git", ["-C", project, "remote", "get-url", "origin"]);
		const m = /github\.com[:/]([^/]+)\/(.+?)(?:\.git)?\s*$/.exec(res.stdout);
		return m ? `https://${m[1].toLowerCase()}.github.io/${m[2]}/` : null;
	}

	async openPublished() {
		const project = await this.project();
		if (!project) return;
		const url = await this.publishedUrl(project);
		if (!url) return new Notice("This project's git remote isn't on GitHub, so there's no Pages address to open.");
		openExternal(url);
	}

	async publish() {
		const project = await this.project();
		if (!project) return;
		const git = (...args) => run("git", ["-C", project, ...args]);
		if (!(await git("rev-parse", "--is-inside-work-tree")).ok) {
			return new Notice("This project isn't a git repository, so it can't be published.");
		}
		await this.app.workspace.getActiveViewOfType(MarkdownView)?.save();
		const status = (await git("status", "--porcelain", "--", ".")).stdout.trimEnd();
		const ahead = (await git("rev-list", "--count", "@{upstream}..HEAD")).stdout.trim();
		if (!status && (!ahead || ahead === "0")) return new Notice("Nothing to publish — no changes since the last push.");

		new PublishModal(this.app, status, async (message) => {
			const notice = new Notice("Publishing…", 0);
			const steps = [];
			if (status) {
				steps.push(["add", "-A", "--", "."]);
				steps.push(["commit", "-m", message]);
			}
			steps.push(["push"]);
			for (const step of steps) {
				const res = await git(...step);
				if (!res.ok) {
					notice.hide();
					console.error("[note-site-builder] git", step.join(" "), "\n", res.stderr);
					return new Notice(`git ${step[0]} failed:\n${(res.stderr || res.stdout).trim().split("\n").slice(-3).join("\n")}`, 15000);
				}
			}
			notice.hide();
			const url = await this.publishedUrl(project);
			new Notice(`Pushed. GitHub rebuilds the site in a minute or two${url ? `:\n${url}` : "."}`, 10000);
		}).open();
	}
};

class ProjectPicker extends SuggestModal {
	constructor(app, projects, root, resolve) {
		super(app);
		this.projects = projects;
		this.root = root;
		this.resolve = resolve;
		this.picked = false;
		this.setPlaceholder("Which website project?");
	}
	getSuggestions(query) {
		const q = query.toLowerCase();
		return this.projects.filter((p) => p.toLowerCase().includes(q));
	}
	renderSuggestion(p, el) {
		el.createEl("div", { text: path.basename(p) });
		el.createEl("small", { text: path.relative(this.root, p) || "(vault root)", cls: "nsb-muted" });
	}
	onChooseSuggestion(p) {
		this.picked = true;
		this.resolve(p);
	}
	onClose() {
		// onChooseSuggestion fires after onClose; let it win.
		setTimeout(() => this.picked || this.resolve(null), 0);
	}
}

class PublishModal extends Modal {
	constructor(app, status, onSubmit) {
		super(app);
		this.status = status;
		this.onSubmit = onSubmit;
	}
	onOpen() {
		const { contentEl } = this;
		this.setTitle?.("Publish the website");
		contentEl.createEl("p", {
			text: this.status
				? "These changes will be committed and pushed; GitHub then rebuilds the public site."
				: "No new edits, but there are commits not yet pushed. They will be pushed now.",
		});
		if (this.status) contentEl.createEl("pre", { text: this.status, cls: "nsb-status-list" });
		let message = "Update handout";
		if (this.status) {
			new Setting(contentEl).setName("What changed").addText((t) => {
				t.setValue(message).onChange((v) => (message = v));
				t.inputEl.style.width = "100%";
				setTimeout(() => t.inputEl.select(), 0);
			});
		}
		new Setting(contentEl)
			.addButton((b) => b.setButtonText("Cancel").onClick(() => this.close()))
			.addButton((b) => b.setButtonText("Publish").setCta().onClick(() => {
				this.close();
				this.onSubmit(message.trim() || "Update handout");
			}));
	}
	onClose() {
		this.contentEl.empty();
	}
}

class SettingsTab extends PluginSettingTab {
	constructor(app, plugin) {
		super(app, plugin);
		this.plugin = plugin;
	}
	display() {
		const { containerEl } = this;
		const p = this.plugin;
		containerEl.empty();

		new Setting(containerEl)
			.setName("Python")
			.setDesc("Path to the python3 that has the site's requirements installed. Leave empty to use the one your terminal finds.")
			.addText((t) => t
				.setPlaceholder(p.detectedPython || "auto-detect")
				.setValue(p.settings.python)
				.onChange(async (v) => {
					p.settings.python = v.trim();
					p.detectedPython = null;
					await p.saveSettings();
				}));

		const projects = p.allProjects();
		const root = p.vaultRoot();
		new Setting(containerEl)
			.setName("Default project")
			.setDesc("Used when the open note isn't inside a project folder (one with site/build.py).")
			.addDropdown((d) => {
				d.addOption("", projects.length === 1 ? "The only one found" : "Ask each time");
				for (const proj of projects) d.addOption(path.relative(root, proj), path.relative(root, proj));
				d.setValue(p.settings.project).onChange(async (v) => {
					p.settings.project = v;
					await p.saveSettings();
				});
			});

		new Setting(containerEl)
			.setName("Preview port")
			.setDesc("Where the live preview is served, as http://localhost:<port>.")
			.addText((t) => t.setValue(String(p.settings.port)).onChange(async (v) => {
				const n = parseInt(v, 10);
				if (n > 0 && n < 65536) {
					p.settings.port = n;
					await p.saveSettings();
				}
			}));
	}
}
