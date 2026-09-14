# Project overview
In this project we will analyse the neural circuits of the cerebellum as well as brain morphology in zebrafish carrying a mutation in the *inpp5e* gene (a causative gene for the ciliopathy Joubert Syndrome). We will use immunofluorescence to analyse granule cells and their axons (parallel fibers), eurydendroid cell clusters in the cerebellum as well as axonal connections in the cerebellum of *inpp5e* mutants compared to controls.
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
**Figure 2: MRI images of the molar tooth sign (https://depts.washington.edu/joubert/joubertsyndrome.php)**

JBTS patients also present with additional phenotypes such as retinal defects, kidney cysts, axonal tract malformations and scoliosis.

*Inpp5e* mutations have been reported to cause deficiencies in ciliary transduction, cilia stability and ciliopathies (Bielas et al., 2009; Zhang et al., 2022). 
## The vertebrate cerebellum
The cerebellum is found in the hindbrain and is involved in the maintenance of balance and posture, voluntary movement coordination, motor learning and some cognitive functions. It contains half of the mature neurons of the adult brain even though being only 10% of the whole brain. In human the cerebellum is separated into two hemispheres that are connected by a thin midline area called the **vermis**. It consists of an outer layer of gray matter called the cerebellar cortex surrounding inner white matter. It is connected to the brain through the **cerebellar peduncles**.
![[Pasted image 20260909133844.png]]
**Figure 3: The human cerebellum (from https://teachmeanatomy.info/neuroanatomy/structures/cerebellum/)**

In zebrafish the layout is a bit different, however the neural circuits remain conserved (across all jawed vertebrates). It is made up of the calcula cerebelli, corpus cerebelli and vestibulolateral lobe (caudal lobe and eminentia granularis)
![[Pasted image 20260910083713.png|226]]
**Figure 4: Zebrafish cerebellum (from Kaslin et al., 2013)**

The cerebellar circuits receive inputs from two excitatory fibers, climbing fibers (CFs) that synapse onto Purkinje cells and mossy fibers (MFs) that synapse onto granule cells (GCs). PCs send information to deep cerebellar nuclei (DCN) in the white matter, which send information to other areas of the brain via the cerebellar peduncles. Zebrafish cerebellum lacks white matter and DCN. PCs project to eurydendroid cells (ECs), which send information to other areas of the brain.
![[Pasted image 20260910084513.png|359]]
**Figure 5: Cerebellar neural circuits in human and zebrafish (by A.Noble based on Yopak et al., 2017)**

## Zebrafish
Zebrafish larvae are optically transparent as well as a rapid developmental timeline, making them an attractive model for microscopy experiments and studying developmental biology. By treating the larvae with 1-phenyl-2-thiourea (PTU) we can block melanin pigmentation removing obstruction caused by pigmented cells.

### Developmental stages
Zebrafish development is divided into 8 distinct periods, each having specific biological processes and milestones.
![[Pasted image 20260911155839.png]]
**Figure 6: Zebrafish developmental stages. (From [https://www.zeclinics.com/blog/understanding-zebrafish-development-stages/]())**

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
More details here: [https://zfin.org/zf_info/zfbook/stages/]()

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
Next, we will discuss the essential steps of a staining protocol
1. Fixation
2. Permeabilization
3. Blocking
4. Primary staining
5. Secondary staining
6. Counter stain
7. Clearing and mounting
#### Fixation
The first step is called fixation. It allows us to lock proteins into place to take a snapshot of the living state. This will prevent degradation, proteins from diffusing away or changing shape. This is generally done with one of the following:
- Paraformaldehyde (PFA), crosslinks proteins together by forming methylene bridges between amino groups on adjacent proteins. This builds a stable mesh that holds antigens in position
- Methanol 
- Trichloroacetic acid (TCA), precipitates proteins and can expose some epitopes better. Harsher on the sample
Keep in mind that there is a trade-off: too little fixation and the tissue is destroyed during the experimental process or antigens will diffuse. Too much and the epitope will be masked. Fixation is antibody dependant and therefore has to be optimised and validated empirically.

#### Washing
Washing removes a chemical agent (eg. PFA,primary antibody,...) before the next one is added (usually between every step). It clears residual PFA after fixation, which would otherwise crosslink the ABs. After antibody incubation steps it removes unbound antibodies (lower background signal). Usually done with PBS (phosphate-buffered saline), that keeps the sample in physiological conditions to not osmotically shock or denature the tissue. A detergent (Triton X-100 or Tween-20) is added to the wash solution to keep the sample membrane permeable. In general more/longer washes gives cleaner images.
#### Permeabilization
Antibodies being quite large (150 kDa) need a little help to penetrate the sample and access the antigen. Treating with Triton x-100, acetone or proteinase K helps the antibody penetrate the sample.

 - **Triton X-100 / Tween-20**: detergents that dissolve lipid membranes, creating pores. Triton is stronger and Tween is milder.
- **Cold acetone/methanol**: extract lipids and permeabilize, done cold (e.g. −20 °C) to be gentler and preserve morphology.
- **Proteinase K**: an enzyme that partially digests protein, loosening the fixed mesh. Powerful for dense/older tissue but easy to overdo: too much destroys morphology. Usually followed by a brief re-fixation to re-stabilize. (We won't do that)

**Trade-off:** more permeabilization = better antibody access but worse structural preservation. Older/larger samples need more and delicate structures need less.

#### Blocking
Antibodies stick weakly and non-specifically to non specific surfaces in the sample. Blocking floods these non specific sites with a generic protein (like BSA) so the only strong binding site left is the specific target. 

#### Primary antibody incubation
The antibody is incubated @4 °C overnight. This slows everything down and favours high affinity binding over weak non-specific sticking. The main parameter we control here is dilution. Too concentrated will give a lot of background signal, to dilute will give too weak of a signal. We normally determine this by titration through a process called antibody validation.

#### Secondary antiboy incubatiuon
Similar to the primary incubation step. The secondary is raised agains the primary's species (eg. goat (<- primary's host species) anti-rabbit (<- secondary's host species)) (see appendix for more on how they are made) and carries a fluorophore. Fluorophore photobleach, so this step is done in the dark to preserve signal. 

#### Nuclear counterstain
This step is optional. Generally, DAPI is used to bind DNA and label nuclei.

#### Clearing and mounting
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
**Figure 9: Fluorophore absorption and emission profiles (From: [https://www.microscopyu.com/techniques/fluorescence/introduction-to-fluorescence-microscopy](Absolute banger of a knowledge base))**

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
**Figure 11: Nipkow disk configuration (From: https://www.microscopyu.com/techniques/confocal/introductory-confocal-concepts)**

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
- For more details: https://www.microscopyu.com/microscopy-basics/resolution
# Designing the experiment
The aims of the project are the following:

| Aim                                          | Biological question                                                                | Markers / channels                                                 | Analysis                                                                                              | Quantification                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **1. General cerebellar circuit morphology** | Is the overall organisation and morphology of cerebellar circuits altered?         | **AcTub**: axonal tracts<br>**SV2**: synaptic neuropil<br>**DAPI**: nuclei | Visual / qualitative assessment of cerebellar architecture                                            | **Qualitative**                                                                 |
| **2. Eurydendroid cells in the cerebellum**  | Are Eurydendroid cell number, distribution, and associated axonal bundles altered? | **Calretinin**: Eurydendroid cells<br>**DAPI**: nuclei                | Cell segmentation/counting with **Cellpose** + manual region annotation; assessment of axonal bundles | **Cell count per hemisphere**<br>**Axonal bundle integrity**<br>**Axonal bundle width** |
| **3. Whole-brain morphology**                | Are the relative sizes of major brain regions altered?                             | **DAPI** from both stainings                                       | Manual anatomical delineation of **forebrain, midbrain, and hindbrain**                               | **Area measurements** for each region                                           |

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

The BC43 has four laser lines. Decide which target goes in which channel, then fill in the dye you will use and the antibody it is conjugated to. You can go to this website to help you visualise the ex/em peaks: [https://www.fpbase.org/spectra/](). We will not use all of the channels. 

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

## PFA-Fixed Larvae

1. Wash larvae **4 × 5 min in PBS**.
   - Larvae can be stored at **4°C for several days** after this step.
   - Only continue with the following steps if proceeding directly to antibody staining.
2. Wash **1 × 5 min with ddH₂O**.
3. Permeabilize with **prechilled acetone** for **7 min at −20°C**.
   - The time can be extended for larvae **older than 3 dpf** to increase permeability.
4. Wash **1 × 5 min with ddH₂O**.
5. Wash **1 × 5 min with PBS**.

---

## MeOH-Fixed Larvae

1. Rehydrate larvae through decreasing MeOH concentrations:
   - **50% MeOH/PBS**, 5 min
   - **25% MeOH/PBS**, 5 min
2. Wash **4 × 5 min with PBS**.
   - Larvae can be stored at **4°C for several days** until staining.

---

## TCA-Fixed Larvae

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

---

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
- Tx-100 10%
- DMSO 100%
- PBS 100%
- Goat serum (GS) 100%
### Calculations/Dilutions
Calculate the following dilutions for the reagents you will be using. When total volume is not specified, think about how many tubes you will be using.

| Reagent |        | volume |
| ------- | ------ | ------ |
| PBDT    |        |        |
|         | PBS    |        |
|         | BSA    |        |
|         | TX-100 |        |
|         | DMSO   |        |
|         | total  | 30ml   |

| Reagent |        | volume |
| ------- | ------ | ------ |
| PDT     |        |        |
|         | PBS    |        |
|         | TX-100 |        |
|         | DMSO   |        |
|         | total  | 30ml   |

| Reagent |       | volume |
| ------- | ----- | ------ |
| PBDT+GS |       |        |
|         | PBDT  |        |
|         | GS    |        |
|         | total |        |
**Experiment 1**

| Reagent |       | volume |
| ------- | ----- | ------ |
| 1°AB    |       |        |
|         | PBDT  |        |
|         | GS    |        |
|         | SV2   |        |
|         | Actub |        |
|         | total |        |

| Reagent |       | volume |
| ------- | ----- | ------ |
| 2°AB    |       |        |
|         | PBDT  |        |
|         | 1     |        |
|         | 2     |        |
|         | total |        |
**Experiment 2**

| Reagent |            | volume |
| ------- | ---------- | ------ |
| 1°AB    |            |        |
|         | PBDT       |        |
|         | GS         |        |
|         | Calretinin |        |
|         | total      |        |

| Reagent |       | volume |
| ------- | ----- | ------ |
| 2°AB    |       |        |
|         | PBDT  |        |
|         | 1     |        |
|         | total |        |
The rest of the calculations will be done during the practical.
# Analyzing your data
In this section we will look at how we are going to analyse your data. We will be using an awesome open source python image visualisation tool called [napari](https://napari.org/stable/). This means that anyone can modify it, develop modules and plugins for a specific application. With the rise of vibe-coding developing your own software is becoming trivial. 
## Installing the tool
1) Install git https://git-scm.com/install/
2) Install python/anaconda [https://www.anaconda.com/download](https://www.anaconda.com/download/success)
3) The tool we will use can be downloaded here: https://github.com/daggermaster3000/ARGUS Follow the instructions from the README file to install it.
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


## Experiment 2

## Experiment 3

## Plotting and statistics
# References

