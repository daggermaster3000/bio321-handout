# Project overview

![[Pasted image 20260914194946.png]]
In this project we will analyse the neural circuits of the cerebellum as well as brain morphology in zebrafish carrying a mutation in the *inpp5e* gene (a causative gene for the ciliopathy Joubert Syndrome). We will use immunofluorescence to analyse general cerebellar circuit morphology, eurydendroid cell clusters in the cerebellum as well as general brain morphology of *inpp5e* mutants compared to controls. 
> As you will be more than planned, we will add a mutant to the project (*ift88*) so everyone can participate.


```table-of-contents
title: **Table of contents**
style: nestedList
minLevel: 1
maxLevel: 3
includeLinks: true
debugInConsole: false
```

# Background
## The primary cilium
Primary cilia are microscopic, hair-like organelles that protrude from the surface of virtually all mammalian cells. Primary cilia function as cellular antennas, sensing and transducing extracellular physical and biochemical signals, including odorants, light, growth factors, fluid flow and developmental morphogens, into cellular responses. They play essential roles in developmental pathways such as Wnt and Hedgehog signalling, neurogenesis, neuronal migration and body symmetry.

Primary cilia share a conserved architecture consisting of a **microtubule-based axoneme** extending from a modified centriole, known as the **basal body**, and surrounded by a specialized **ciliary membrane**. The ciliary membrane has a distinct protein and lipid composition regulated by multiple protein complexes. The basal body is connected to the ciliary membrane by **transition fibers**, which are the docking site for vesicles carrying lipids and proteins to the cilium. The transition zone connects the axoneme to the ciliary membrane and acts as a gate controlling entry and exit of lipids and proteins. Proteins are transported along the axoneme in a process termed intraflagellar transport (**IFT**), where IFT complexes move cargo along the axoneme's microtubules from base to tip and back.

![[Pasted image 20260909121850.png|400]]
**Figure 1: Structure of the primary cilium (adapted from Park et al., 2019)**

**Inpp5e** is located in the ciliary membrane as well as the base and the axoneme and plays a key role in regulating ciliary membrane composition, and IFT indirectly. Its dysfunction has been shown to affect the Shh pathway.
## Ciliopathies
Ciliopathies are a group of human Mendelian disorders caused by structural and functional defects in cilia. These disorders have a wide variety of phenotypes affecting multiple organ systems including the retina, the kidney, the skeleton and the brain. Joubert syndrome (JBTS), a prototypical ciliopathy, can be caused by mutations in approximately 40 genes.
All JBTS patients show malformations in cerebellar development, recognisable on MRI's and named the molar tooth sign. 
![[Pasted image 20260909122628.png|401]]
**Figure 2: MRI images of the molar tooth sign ([University of Washington Joubert Syndrome Research](https://depts.washington.edu/joubert/joubertsyndrome.php))**

JBTS patients also present with additional phenotypes such as retinal defects, kidney cysts, axonal tract malformations and scoliosis.

*Inpp5e* mutations have been reported to cause deficiencies in ciliary transduction, cilia stability and ciliopathies (Bielas et al., 2009; Zhang et al., 2022). 
## The vertebrate cerebellum
The cerebellum is found in the hindbrain and is involved in the maintenance of balance and posture, voluntary movement coordination, motor learning and some cognitive functions. It contains half of the mature neurons of the adult brain even though being only 10% of the whole brain. In human the cerebellum is separated into two hemispheres that are connected by a thin midline area called the **vermis**. It consists of an outer layer of gray matter called the cerebellar cortex surrounding inner white matter. It is connected to the brain through the **cerebellar peduncles**.
![[Pasted image 20260909133844.png]]
**Figure 3: The human cerebellum (from [TeachMeAnatomy](https://teachmeanatomy.info/neuroanatomy/structures/cerebellum/))**

In zebrafish the layout is a bit different, however the neural circuits remain conserved (across all jawed vertebrates). It is made up of the calcula cerebelli, corpus cerebelli and vestibulolateral lobe (caudal lobe and eminentia granularis)
![[Pasted image 20260910083713.png|226]]
**Figure 4: Zebrafish cerebellum (from Kaslin et al., 2013)**

The cerebellar circuits receive inputs from two excitatory fibers, climbing fibers (CFs) that synapse onto Purkinje cells and mossy fibers (MFs) that synapse onto granule cells (GCs). PCs send information to deep cerebellar nuclei (DCN) in the white matter, which send information to other areas of the brain via the cerebellar peduncles. Zebrafish cerebellum lacks white matter and DCN. PCs project to eurydendroid cells (ECs), which send information to other areas of the brain.
![[Pasted image 20260910084513.png|700]]
**Figure 5: Cerebellar neural circuits in human and zebrafish (by A.Noble based on Yopak et al., 2017)**

Below you can see a dorsal view of the ZF brain from https://mapzebrain.org/atlas/2d. The cerebellum is highlighted in blue and the eurydendroid cells in color.
![[Pasted image 20260915175526.png]]

## Zebrafish
Zebrafish larvae are optically transparent as well as a rapid developmental timeline, making them an attractive model for microscopy experiments and studying developmental biology. By treating the larvae with 1-phenyl-2-thiourea (PTU) we can block melanin pigmentation removing obstruction caused by pigmented cells.

### Developmental stages
Zebrafish development is divided into 8 distinct periods, each having specific biological processes and milestones.
![[Pasted image 20260911155839.png]]
**Figure 6: Zebrafish developmental stages. (From [ZeClinics](https://www.zeclinics.com/blog/understanding-zebrafish-development-stages/))**

1. **Zygote** (0-45min post-fertilization)
2. **Cleavage**
	1. Rapid cell division
	2. Transition from single cell to multicellular structure
3. **Blastula** 
	1. Epiboly marks the start of cell movements that shape the embryo
4. **Gastrula**
	1. Morphogenesis begins
	2. The body plan starts to form
5. **Segmentation**
	1. Developoment of brain and spinal cord
	2. Start of organogenesis, formation of tail and somites, first movements
	3. Midbrain-Hindbrain boundary formed by the end of the period 
6. **Pharyngula**
	1. Body straightening, pigmentation
	2. circulatory system starts forming and fins begin developing
	3. First heartbeat
7. **Hatching**
	1. Cartilage development in the head
8. **Larval stage**
	1. Swim bladder inflates, food seeking and avoidance behaviors indicate maturing CNS
More details here: [The Zebrafish Book — stages of embryonic development (ZFIN)](https://zfin.org/zf_info/zfbook/stages/)

### Mutant zebrafish
![[Pasted image 20260911161551.png|652]]
**Figure 7: Illustration of the *inpp5e* genomic region and the *zh507* variant**

*Inpp5e-zh507* mutants carry an 18bp deletion in exons 5/6 in the inositol polyphosphatase catalytic domain. The resulting protein is consequently believed to lose it's function. Briefly (ask me if you want more details), INPP5E is responsible for converting a certain type of ciliary membrane lipid to another. Each type plays different roles in the ciliary landscape. INPP5E knock out leads to an increase in Ptdins(4,5)P2 (one of the lipid species) in the ciliary membrane. TULP3 (an adaptor protein part of the IFT complex) binds to the Ptdins(4,5)P2  and leads to an accumulation of GPR161 (a negative regulator of the SHH pathway) in the cilia.

*Inpp5ezh507* display a curved body axis, severe retinal dystrophy, kidney cysts and cannot be raised as adults. You will (if all goes well) find out if they have a phenotype in the brain. Previously our lab has performed the same type of experiments on the *zh506* variant and found no significant differences when compared to controls. However this variant isn't a total knock out and there are high chances the protein is still able to somewhat fulfil it's function.

## Immunohistochemistry

> If you already know about this you can skip.

### The idea
The whole idea relies on an antibody binding to it's antigen with high specificity. In general antibodies are ordered by companies that specialise in producing them. However a few labs make them homemade for more specific applications. Generally we perform **indirect immunostaining**:
- The primary antibody (unlabelled) binds the antigen
- The secondary antibody (labelled with a fluorophore or enzyme) binds the primary
The main benefits of this setup are **signal amplification** as multiple secondaries can bind one primary and **flexibility** in the experimental setup.



![[Pasted image 20260911165725.png|567]]
**Figure 8: Illustration of antibody labelling principle**

### Explanation of a generic protocol
Next, we will discuss the essential steps of a staining protocol.

1. Fixation
2. Washing
3. Permeabilization
4. Blocking
5. Primary staining
6. Secondary staining
7. Counter stain
8. Clearing and mounting
#### 1. Fixation
The first step is called fixation. It allows us to lock proteins into place to take a snapshot of the living state. This will prevent degradation, proteins from diffusing away or changing shape. This is generally done with one of the following:

- Paraformaldehyde (PFA), crosslinks proteins together by forming methylene bridges between amino groups on adjacent proteins. This builds a stable mesh that holds antigens in position
- Trichloroacetic acid (TCA), precipitates proteins and can expose some epitopes better. Harsher on the sample
- Methanol (not used as often as it's a bit annoying)

Keep in mind that there is a trade-off: too little fixation and the tissue is destroyed during the experimental process or antigens will diffuse. Too much and the epitope will be masked. Fixation is antibody dependant and therefore has to be optimised and validated empirically.

#### 2. Washing
Washing removes a chemical agent (eg. PFA,primary antibody,...) before the next one is added (usually between every step). It clears residual PFA after fixation, which would otherwise crosslink the antibodies. After antibody incubation steps it removes unbound antibodies (lower background signal). Usually done with PBS (phosphate-buffered saline), that keeps the sample in physiological conditions to not osmotically shock or denature the tissue. A detergent (Triton X-100 or Tween-20) is added to the wash solution to keep the sample membrane permeable. In general more/longer washes gives cleaner images.
#### 3. Permeabilization
Antibodies being quite large (150 kDa) need a little help to penetrate the sample and access the antigen. Treating with Triton x-100, acetone or proteinase K helps the antibody penetrate the sample.

 - **Triton X-100 / Tween-20**: detergents that dissolve lipid membranes, creating pores. Triton is stronger and Tween is milder.
- **Cold acetone/methanol**: extract lipids and permeabilize, done cold (e.g. −20 °C) to be gentler and preserve morphology.
- **Proteinase K**: an enzyme that partially digests protein, loosening the fixed mesh. Powerful for dense/older tissue but easy to overdo: too much destroys morphology. Usually followed by a brief re-fixation to re-stabilize. (We won't do that)

**Trade-off:** more permeabilization = better antibody access but worse structural preservation. Older/larger samples need more and delicate structures need less.

#### 4. Blocking
Antibodies stick weakly and non-specifically to non specific surfaces in the sample. Blocking floods these non specific sites with a generic protein (like BSA) so the only strong binding site left is the specific target. 

#### 5. Primary antibody staining
The antibody is incubated @4 °C overnight. This slows everything down and favours high affinity binding over weak non-specific sticking. The main parameter we control here is dilution. Too concentrated will give a lot of background signal, to dilute will give too weak of a signal. We normally determine this by titration through a process called antibody validation.

#### 6. Secondary antiboy staining
Similar to the primary incubation step. The secondary is raised agains the primary's species (eg. goat (<- primary's host species) anti-rabbit (<- secondary's host species)) (see appendix for more on how they are made) and carries a fluorophore. Fluorophore photobleach, so this step is done in the dark to preserve signal. 

#### 7. Nuclear counterstain
This step is optional. Generally, DAPI is used to bind DNA and label nuclei.

#### 8. Clearing and mounting
Clearing with glycerol raises the refractive index of the sample to reduce light scattering. We can then image deeper into the sample with less blur. We then mount our sample such as the region of interest is as close as possible to the coverslip as objectives have limited working distance. In our case we will be doing the experiments on whole-mounts, meaning that the whole specimen conserved (as opposed to slicing, where physical sections are cut from the specimen, mounted on a glass slide then imaged (a real pain))

#### Recap
| Reagent                    | Role                                                  |
| -------------------------- | ----------------------------------------------------- |
| PFA                        | Crosslink and preserve proteins in place              |
| PBS                        | Physiological buffer, base of most solutions          |
| Detergent (Triton/Tween)   | Permeabilize membranes; reduce nonspecific binding    |
| Acetone/methanol           | Precipitate/permeabilize (alternative to detergent)   |
| Proteinase K               | Enzymatically loosen fixed tissue for antibody access |
| Serum / BSA                | Block nonspecific antibody binding sites              |
| DMSO                       | Aid reagent penetration                               |
| Primary antibody           | Specific recognition of the target antigen            |
| Secondary antibody         | Bind primary, carry the label, amplify signal         |
| Fluorophore                | Emit detectable light                                 |
| DAPI                       | Counterstain nuclei for anatomical reference          |
| Glycerol                   | Clear tissue (refractive index matching)              |
| Mounting medium + antifade | Preserve sample and slow photobleaching               |

## Microscopy refresher
A quick review of microscopy basics.
### Basic principles
The tissue of interest is illuminated by light of a specific wavelength. This light is absorbed by a fluorophore which will become excited. It will then emit light at a longer wavelength that can be detected by the microscope. 

![[Pasted image 20260914104540.png|338]]
**Figure 9: Fluorophore absorption and emission profiles (From: [MicroscopyU — absolute banger of a knowledge base](https://www.microscopyu.com/techniques/fluorescence/introduction-to-fluorescence-microscopy))**

In standard fluorescence microscopy, the whole sample is illuminated by the excitation wavelength therefore we will detect in-focus and out of focus light, creating a blurred image. 
![[Pasted image 20260914103840.png|287]]
**Figure 10: Basic fluorescence microscopy setup (From wikipedia)**

Confocal microscopy solves this issue by adding a pinhole to the setup, meaning that only light that is in focus (from the focal plane of the lens) will be detected. This creates a sharper image and enables us to image multiple planes (or optical sections) of our sample. The way the sample is imaged is also fundamentally different: illumination is achieved by scanning one or more focused beams of light from a laser accross the specimen. 
![[Pasted image 20260914104944.png|318]]
**Figure 10: Principles of confocal microscopy. Laser light is focus on a thick specimen by reflection from the dichroic mirror (DM)  and the objective lens. A pinhole allows only excited light from the confocal place to reach the photomultiplier detector (PMT)**
### The BC43 microscope
![[Pasted image 20260914105426.png|291]]
The microscope we will be using is a spinning disk confocal microscope. Meaning that the excitation beams are generated with a Nipkow disk. This allows fast imaging and is ideal for time-lapse recordings in *in-vivo* specimens (not our case for this course).
![[Pasted image 20260914105859.png]]
**Figure 11: Nipkow disk configuration (From: [MicroscopyU](https://www.microscopyu.com/techniques/confocal/introductory-confocal-concepts))**

### Key variables and parameters in microscopy
A brief reminder of two important concepts 
#### Numerical aperture and resolution
Numerical aperture (NA) is a measure of the **ability of an objective to gather light and resolve specimen detail at a fixed distance**. It is specified by the manufacturer.
$$
NA = n \times sin(\alpha)
$$
Where $\alpha$ is half the angle of angular aperture (or light cone), $n$ is the refractive index of the medium between the lens and the specimen. How does this relate to resolution?

Resolution ($r$) is the **smallest resolvable distance between two objects**. (How close can two objects be and still distinguish them as separate). It relates to NA with the following formula:
$$
r = 0.61\lambda/NA
$$
where $\lambda$ is the imaging wavelength.
These parameters are important to keep in mind when designing an experiment. But to summarize:

- The higher the NA, the better the resolving power of a microscope ($r$)
- Shorter wavelength leads to better (lower) resolution
- For more details: [MicroscopyU — resolution](https://www.microscopyu.com/microscopy-basics/resolution)
# Designing the experiment
The aims of the project are the following:

| Aim                                          | Biological question                                                                | Markers / channels                                                         | Analysis                                                                                              | Quantification                                                                          |
| -------------------------------------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **1. General cerebellar circuit morphology** | Is the overall organisation and morphology of cerebellar circuits altered?         | **AcTub**: axonal tracts<br>**SV2**: synaptic neuropil<br>**DAPI**: nuclei | Visual / qualitative assessment of cerebellar architecture                                            | **Qualitative**                                                                         |
| **2. Eurydendroid cells in the cerebellum**  | Are Eurydendroid cell number, distribution, and associated axonal bundles altered? | **Calretinin**: Eurydendroid cells<br>**DAPI**: nuclei                     | Cell segmentation/counting with **Cellpose** + manual region annotation; assessment of axonal bundles | **Cell count per hemisphere**<br>**Axonal bundle integrity**<br>**Axonal bundle width** |
| **3. Whole-brain morphology**                | Are the relative sizes of major brain regions altered?                             | **DAPI** from both stainings                                               | Manual anatomical delineation of **forebrain, midbrain, and hindbrain**                               | **Area measurements** for each region                                                   |

![[Pasted image 20260914141201.png|364]]
**Figure 12: Experimental setup, mutants can be discriminated basedon their phenotype (body curvature), therefore samples are pooled for staining, total tubes: 2**

## Choosing the fluorophores
Below is a table of the primary antibodies we will use:

**Experiment 1**

| Antibody | Type        | **Target**        |
| -------- | ----------- | ----------------- |
| AcTub    | mouse IgG2b | axoneme + axons   |
| SV2      | mouse IgG1  | neuropil/synapses |

**Experiment 2**

| Antibody   | Type   | **Target**         |
| ---------- | ------ | ------------------ |
| calretinin | Rabbit | eurydendroid cells |


The following table contains the secondary antibodies available in the lab:

| Host | Target species | Target class | Conjugate | Cat. # | Dilution  |
| ---- | -------------- | ------------ | --------- | ------ | --------- |
| Goat | Mouse          | IgG          | 488 Plus  | A32723 | 1:300–400 |
| Goat | Mouse          | IgG1         | 488       | A21121 | 1:300–400 |
| Goat | Mouse          | IgG2b        | 488       | A21141 | 1:300–400 |
| Goat | Mouse          | IgG2a        | 488       | A21131 | 1:300–400 |
| Goat | Mouse          | IgG2a        | 546       | A21133 | 1:300–400 |
| Goat | Mouse          | IgG          | 555       | A21424 | 1:300–400 |
| Goat | Mouse          | IgG1         | 568       | A21124 | 1:300–400 |
| Goat | Mouse          | IgG2a        | 568       | A21134 | 1:300–400 |
| Goat | Mouse          | IgG2b        | 568       | A21144 | 1:300–400 |
| Goat | Mouse          | IgG2a        | 647       | A21241 | 1:300–400 |
| Goat | Mouse          | IgG2b        | 647       | A21242 | 1:300–400 |
| Goat | Mouse          | IgM          | 647       | A21238 | 1:300–400 |
| Goat | Rabbit         | IgG          | 405 Plus  | A48254 | 1:300–400 |
| Goat | Rabbit         | IgG          | 488       | A11034 | 1:300–400 |
| Goat | Rabbit         | IgG          | 568       | A11036 | 1:300–400 |
| Goat | Rabbit         | IgG          | 647       | A21245 | 1:300–400 |

The BC43 has four laser lines. Decide which target goes in which channel, then fill in the dye you will use and the antibody it is conjugated to. You can go to this website to help you visualise the ex/em peaks: [FPbase spectra viewer](https://www.fpbase.org/spectra/). We will not use all of the channels. 

**Experiment 1**

| Channel | Laser Excitation | Fluorophore conjugate | Emission | Target | cat. # |
| ------- | ---------------- | --------------------- | -------- | ------ | ------ |
| Blue    | 405 nm           |                       |          |        |        |
| Green   | 488 nm           |                       |          |        |        |
| Orange  | 561 nm           |                       |          |        |        |
| Far red | 640 nm           |                       |          |        |        |

**Experiment 2**

| Channel | Laser Excitation | Fluorophore conjugate | Emission | Target | cat. # |
| ------- | ---------------- | --------------------- | -------- | ------ | ------ |
| Blue    | 405 nm           |                       |          |        |        |
| Green   | 488 nm           |                       |          |        |        |
| Orange  | 561 nm           |                       |          |        |        |
| Far red | 640 nm           |                       |          |        |        |


# Whole mount antibody staining protocol
The following section showcases the protocol we will be using. 
## General Notes

- Fix up to **20 larvae** in an Eppendorf tube.
- Use **500 µL** for all steps unless stated otherwise.
- Remove as much liquid as possible before each subsequent step, while ensuring that no embryos are accidentally aspirated.
- Place tubes on a shaker during washing steps.
- Make sure no larvae stick to the walls or lid of the tube.
- **PBDT** can be prepared on the first day and stored at **4°C** for the following day.

---

## 1. Fix Larvae

> **Note:** Fixation conditions depend on the antibody. The following options are available.

### Option 1: PFA Fixation

- Fix larvae in **4% PFA**:
  - **Overnight at 4°C**, or
  - **2 h at RT**
- Duration may depend on the antibody.

### Option 2: Methanol Fixation

- Fix larvae in **80% MeOH in DMSO**:
  - **Overnight at 4°C**, or
  - **Minimum 2 h at RT**

### Option 3: TCA Fixation

- Fix larvae in **2% TCA** for **3 h at RT**.

---

## 2. Wash Larvae 

### PFA-Fixed Larvae

1. Wash larvae **4 × 5 min in PBS**.
   - Larvae can be stored at **4°C for several days** after this step.
   - Only continue with the following steps if proceeding directly to antibody staining.
2. Wash **1 × 5 min with ddH₂O**.
3. Permeabilize with **prechilled acetone** for **7 min at −20°C**.
   - The time can be extended for larvae **older than 3 dpf** to increase permeability.
4. Wash **1 × 5 min with ddH₂O**.
5. Wash **1 × 5 min with PBS**.

---

### MeOH-Fixed Larvae

1. Rehydrate larvae through decreasing MeOH concentrations:
   - **50% MeOH/PBS**, 5 min
   - **25% MeOH/PBS**, 5 min
2. Wash **4 × 5 min with PBS**.
   - Larvae can be stored at **4°C for several days** until staining.

---

### TCA-Fixed Larvae

1. Wash larvae **4 × 5 min in PBS**.
   - Larvae can be stored at **4°C for several days** until staining.

---

## 3. Antibody Staining

### 3.1 Blocking

Block larvae with:

**PBDT + 10% goat serum**

Where:

> **PBDT = PBS + 1% BSA + 0.5% Triton X-100 + 1% DMSO**

- Incubate for **30 min at RT**.
- The serum should match the species in which the **secondary antibody** was raised.

---

### 3.2 Primary Antibody

- Add **100 µL primary antibody** diluted in **PBDT + 2% goat serum**.
- Incubate **overnight at 4°C**.
- Primary antibody dilution depends on the antibody.

---

## 4. Next Day

### 4.1 Recover Primary Antibody

> **Optional:** For precious antibodies, recover the antibody mixture into an Eppendorf tube.

- Label the recovered antibody with:
  - Exact antibody dilution
  - Date

---

### 4.2 Wash

Wash larvae **4 × with PBDT**:

- 10 min
- 15 min
- 30 min
- 1 h

---

### 4.3 Secondary Antibody

- Add **100 µL secondary antibody** diluted in PBDT.
- Typical dilution:
  - **1:400 Alexa Fluor-conjugated secondary antibody**
  - Dilution may vary depending on the antibody.
- Incubate:
  - **Minimum 2 h at RT**, or
  - **Overnight at 4°C**

> ⚠️ **From this point onward, keep tubes in the dark.**

---

### 4.4 Wash

Wash larvae **4 × with PDT**:

> **PDT = PBS + 0.5% Triton X-100 + 1% DMSO**

Wash durations:

- 10 min
- 15 min
- 30 min
- 1 h

---

### 4.5 DAPI Staining

> **Optional**

Add:

- **100 µL DAPI**
- Sigma, **10236276001**
- Dilution: **1:1000 in ddH₂O**
- Incubate for **15 min**

Then wash:

- **3 × 15 min with PDT**

---

## 5. Clearing

Clear larvae through an increasing glycerol series:

1. **25% glycerol/PDT** (or PBS)
2. **50% glycerol/PDT** (or PBS)
3. **70% glycerol/PDT** (or PBS)

Continue until larvae sink to the bottom.

> **Tip:** Surface tension can keep larvae floating. Gently knock the tube against the bench to check whether the larvae begin to sink.

- Larvae can remain in **70% glycerol at 4°C** until mounting.

---

## 6. Mounting

## Materials

- Mowiol/DABCO
- Vacuum grease
- Nail polish
- Insect pins
- Large coverslip
- Small coverslip
- 100 µL pipette

## Procedure

1. Mount larvae on coverslips using **Mowiol/DABCO**.

2. **Deyolk larvae** using insect pins.

3. If desired, cut off the heads and align:
   - Heads separately
   - Tails separately

4. Align larvae on a **large coverslip**.

> **Important:** Do not use a slide. Mounting on a coverslip allows imaging from both the **ventral and dorsal** sides.

5. Prepare a small coverslip by making **4 posts of vacuum grease**.

6. Place the small coverslip on top of the aligned larvae.

7. Gently press the small coverslip down until the sample **just makes contact** with the coverslip.

> **Note:** If the larvae have been kept whole, the head will touch the coverslip first because the sample is thicker there. The tail may therefore float to the side during the next step.

8. Using a **100 µL pipette**, add drops of Mowiol to the side of the small coverslip.

9. Allow the Mowiol to be drawn underneath the coverslip.

10. Continue adding Mowiol **drop by drop** until the entire area beneath the coverslip is filled.

11. Seal the coverslip with **nail polish**.

12. Store mounted samples at **4°C**.
# Reagent Recipes

| Reagent                       | Composition                                |
| ----------------------------- | ------------------------------------------ |
| **PBDT**                      | PBS + 1% BSA + 0.5% Triton X-100 + 1% DMSO |
| **PDT**                       | PBS + 0.5% Triton X-100 + 1% DMSO          |
| **PBDT + goat serum**         | PBDT + 10% goat serum for blocking         |
| **Primary antibody solution** | Primary antibody in PBDT + 2% goat serum   |
| **DAPI solution**             | DAPI 1:1000 in ddH₂O                       |
| **Glycerol clearing**         | 25%, 50%, 70% glycerol in PDT or PBS       |

**Stocks:** 

- BSA 2%
- Triton X-100 10%
- DMSO 100%
- PBS 100%
- Goat serum (GS) 100%

### Calculations/Dilutions
Calculate the following dilutions for the reagents you will be using. When total volume is not specified, think about how many tubes you will be using.

| Reagent  |        | volume |
| -------- | ------ | ------ |
| **PBDT** |        |        |
|          | PBS    |        |
|          | BSA    |        |
|          | TX-100 |        |
|          | DMSO   |        |
|          | total  | 30ml   |

| Reagent |        | volume |
| ------- | ------ | ------ |
| **PDT** |        |        |
|         | PBS    |        |
|         | TX-100 |        |
|         | DMSO   |        |
|         | total  | 30ml   |

| Reagent     |       | volume |
| ----------- | ----- | ------ |
| **PBDT+GS** |       |        |
|             | PBDT  |        |
|             | GS    |        |
|             | total |        |

**Experiment 1**

| Reagent  |       | volume |
| -------- | ----- | ------ |
| **1°AB** |       |        |
|          | PBDT  |        |
|          | GS    |        |
|          | SV2   |        |
|          | Actub |        |
|          | total |        |

| Reagent  |       | volume |
| -------- | ----- | ------ |
| **2°AB** |       |        |
|          | PBDT  |        |
|          | 1     |        |
|          | 2     |        |
|          | total |        |

**Experiment 2**

| Reagent  |            | volume |
| -------- | ---------- | ------ |
| **1°AB** |            |        |
|          | PBDT       |        |
|          | GS         |        |
|          | Calretinin |        |
|          | total      |        |

| Reagent  |       | volume |
| -------- | ----- | ------ |
| **2°AB** |       |        |
|          | PBDT  |        |
|          | 1     |        |
|          | total |        |


The rest of the calculations will be done during the practical.
# Analyzing your data
# Analyzing your data //hidden
(still working on this so ignore for now)

In this section we will look at how we are going to analyse your data. We will be using an awesome open source python image visualisation tool called [napari](https://napari.org/stable/). This means that anyone can modify it, develop modules and plugins for a specific application. With the rise of vibe-coding developing your own software is becoming trivial. 
## Installing the tool
1) Install [git](https://git-scm.com/install/)
2) Install [python/anaconda](https://www.anaconda.com/download/success)
3) The tool we will use can be downloaded here: [ARGUS](https://github.com/daggermaster3000/ARGUS). Follow the instructions from the README file to install it.
4) Test everything is working
## Experiment 1
The analysis of this experiment will illustrate how we quantitatively assess images. You will generate a few representative samples from each group and visually assess the integrity of each labelled structure.
Run the ARGUS code, the viewer should open (can be a bit slow on some machines)

We start by opening the folder containing our experiment.
![[Pasted image 20260914165609.png]]

You will find that the widgets are very cramped, use their title to drag them somewhere else and expand them comfortably.

![[Pasted image 20260914170002.png]]

Go through your samples select one and press open. The image should load.
Adjust the contrast in this pane:
![[Pasted image 20260914170213.png|476]]
You can go through the stack using the z slider:
![[Pasted image 20260914170440.png|433]]
Next, you can press the cube in this panel:
![[Pasted image 20260914170525.png]]
to load 3D view. Go ahead and inspect of few of your samples.
You can take screenshots of the viewer in the file menu and copy/paste to your power point
![[Pasted image 20260914170922.png|486]]

### Annotating brain regions
![[Pasted image 20260916112205.png|492]]
## Experiment 2

## Experiment 3

## Plotting and statistics
# References
## Literature
Bielas, S. L., Silhavy, J. L., Brancati, F., Kisseleva, M. V., Al-Gazali, L., Sztriha, L., Bayoumi, R. A., Zaki, M. S., Abdel-Aleem, A., Rosti, R. O., Kayserili, H., Swistun, D., Scott, L. C., Bertini, E., Boltshauser, E., Fazzi, E., Travaglini, L., Field, S. J., Gayral, S., … Gleeson, J. G. (2009). Mutations in *INPP5E*, encoding inositol polyphosphate-5-phosphatase E, link phosphatidyl inositol signaling to the ciliopathies. *Nature Genetics*, 41(9), 1032–1036. [10.1038/ng.423](https://doi.org/10.1038/ng.423)

Kaslin, J., & Brand, M. (2013). Cerebellar development and neurogenesis in zebrafish. In M. Manto, J. D. Schmahmann, F. Rossi, D. L. Gruol, & N. Koibuchi (Eds.), *Handbook of the Cerebellum and Cerebellar Disorders* (pp. 1441–1462). Springer. [10.1007/978-94-007-1333-8_63](https://doi.org/10.1007/978-94-007-1333-8_63)

Kaslin, J., Kroehne, V., Benato, F., Argenton, F., & Brand, M. (2013). Development and specification of cerebellar stem and progenitor cells in zebrafish: from embryo to adult. *Neural Development*, 8, 9. [10.1186/1749-8104-8-9](https://doi.org/10.1186/1749-8104-8-9)

Kimmel, C. B., Ballard, W. W., Kimmel, S. R., Ullmann, B., & Schilling, T. F. (1995). Stages of embryonic development of the zebrafish. *Developmental Dynamics*, 203(3), 253–310. [10.1002/aja.1002030302](https://doi.org/10.1002/aja.1002030302)

Park, S. M., Jang, H. J., & Lee, J. H. (2019). Roles of primary cilia in the developing brain. *Frontiers in Cellular Neuroscience*, 13, 218. [10.3389/fncel.2019.00218](https://doi.org/10.3389/fncel.2019.00218)

Stringer, C., Wang, T., Michaelos, M., & Pachitariu, M. (2021). Cellpose: a generalist algorithm for cellular segmentation. *Nature Methods*, 18(1), 100–106. [10.1038/s41592-020-01018-x](https://doi.org/10.1038/s41592-020-01018-x)

Yopak, K. E., Pakan, J. M. P., & Wylie, D. (2017). The cerebellum of nonmammalian vertebrates. In J. H. Kaas (Ed.), *Evolution of Nervous Systems* (2nd ed., Vol. 1, pp. 373–385). Elsevier. [10.1016/B978-0-12-804042-3.00015-4](https://doi.org/10.1016/B978-0-12-804042-3.00015-4)

Zhang, R., Tang, J., Li, T., Zhou, J., & Pan, W. (2022). *INPP5E* and coordination of signaling networks in cilia. *Frontiers in Molecular Biosciences*, 9, 885592. [10.3389/fmolb.2022.885592](https://doi.org/10.3389/fmolb.2022.885592)

## Web resources
- [MicroscopyU introduction to fluorescence microscopy](https://www.microscopyu.com/techniques/fluorescence/introduction-to-fluorescence-microscopy)
- [MicroscopyU introductory confocal concepts](https://www.microscopyu.com/techniques/confocal/introductory-confocal-concepts)
- [MicroscopyU resolution](https://www.microscopyu.com/microscopy-basics/resolution)
- [FPbase spectra viewer](https://www.fpbase.org/spectra/) — plot excitation and emission spectra of fluorophores together
- [The Zebrafish Book stages of embryonic development (ZFIN)](https://zfin.org/zf_info/zfbook/stages/)
- [ZeClinics understanding zebrafish development stages](https://www.zeclinics.com/blog/understanding-zebrafish-development-stages/)
- [TeachMeAnatomy the cerebellum](https://teachmeanatomy.info/neuroanatomy/structures/cerebellum/)
- [University of Washington Joubert syndrome](https://depts.washington.edu/joubert/joubertsyndrome.php)

## Software
- [napari](https://napari.org/stable/) multidimensional image viewer for Python
- [ARGUS](https://github.com/daggermaster3000/ARGUS) the analysis tool used in this course
- [git](https://git-scm.com/install/) and [Anaconda](https://www.anaconda.com/download/success) needed to install ARGUS
