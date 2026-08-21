# DFT handoff — localized Zr-fluorite motif in bixbyite In2O3

## Objective

Determine whether the experimentally inferred localized fluorite-like environment around Zr directly changes a surface reaction state or mainly changes defect supply/healing dynamics.

## Model ladder

- `BIX-0`: undoped bixbyite reference.
- `BIX-Zr6.25`: ordinary Zr-doped bixbyite control.
- `PER-Zr6.25`: globally periodic fluorite-like computational comparator.
- `LOC-Zr6.25`: same composition but localized fluorite-like Zr first shell in a bixbyite host.
- `EMB-Zr3.125`: larger bixbyite supercell with one isolated local motif.
- `EMB-Zr6.25`: larger supercell with two separated motifs.

`LOC` and `EMB` are candidate structures, not assumed catalyst states. They advance only after unconstrained local relaxation preserves both long-range bixbyite order and a fluorite-like Zr first shell.

## Paired-comparison rule

Within each mechanistic comparison hold fixed facet, slab thickness, lateral cell, vacancy count/depth, hydroxyl and H inventory, adsorbate count/site family, electronic-structure settings, and free-energy convention.

## Stage 1

1. H-pair thermodynamics: compare `H2(g) -> In-H* + OH*`.
2. Direct CO2 vacancy healing: compare `CO2 + V_O -> CO + O_lattice` for near-Zr and far-Zr vacancies.
3. H2COOH scission: compare `H2COOH* -> H2CO* + OH*` on matched hydroxylated surfaces.

Advance a mechanism for a paired shift >=0.10 eV. Treat <0.05 eV as a stop signal for expanding that branch. Intermediate results remain unresolved.

## Later triggers

Vacancy migration, H2 dissociation, interface/segregation calculations, microkinetics, and MLIP sampling are conditional follow-ups rather than default work.

## Prohibited inference

Do not state that one barrier explains the published S1/S4 mass-specific STY difference before experiment separates active-area, transient, and surface-state contributions.
