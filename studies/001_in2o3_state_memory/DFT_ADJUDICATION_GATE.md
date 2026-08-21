# DFT adjudication gate

## Why DFT is bounded

The published S4/S1 methanol-STY ratio is `0.32/0.36 = 0.889`. Mapping that ratio onto one transition-state free-energy difference at 573 K is only a diagnostic and gives a scale of roughly 5.8 meV. The experiment has not yet separated active area, state population, coverage, and intrinsic kinetics, so a single calculated barrier cannot legitimately be said to explain the ~11% mass-specific rate difference.

For this project, first-stage DFT therefore asks whether alternative surface-state mechanisms produce materially different paired predictions, rather than fitting the observed residual.

## Mechanistic questions

### D00 — model survival

Compare ordinary bixbyite, a periodic Zr-fluorite computational comparator, and a localized fluorite-like Zr first shell embedded in a bixbyite host. A local motif advances only if it survives relaxation without global fluorite conversion, artificial remote-atom freezing, or spontaneous phase separation.

### D01 — H-pair thermodynamics

At matched facet, vacancy count, hydroxylation, and H inventory, compare the free energy of forming an In-H/OH pair. Advance a hydrogen-coverage mechanism for a paired shift of at least 0.10 eV; stop expansion if all shifts are below 0.05 eV.

### D02 — direct CO2 vacancy healing

Compare `CO2 + V_O -> CO + O_lattice` for near-Zr and far-Zr vacancies. Advance a direct healing mechanism only for a location-specific energetic/barrier shift of at least 0.10 eV. If all surface-healing values are similar, test one bounded vacancy-migration path rather than expanding the reaction network.

### D03 — H2COOH scission

On matched hydroxylated In2O3(110)-type surfaces, compare the barrier for `H2COOH* -> H2CO* + OH*`. Advance a direct methanol-network mechanism only for a paired shift of at least 0.10 eV at matched redox and hydroxyl inventory.

## Frozen interpretation matrix

| D01 | D02 | D03 | Interpretation |
|---|---|---|---|
| large | small | small | hydrogen thermodynamics/coverage |
| small | large | small | vacancy healing or defect supply |
| small | small | large | direct methanol-network rewiring |
| large | large | any | coupled H–defect mechanism; microkinetic integration required |
| small | small | small | return to morphology, delayed activation, segregation, or another state variable |
| model fails | — | — | localized fluorite-like surface hypothesis not structurally licensed |

Here `large` means at least 0.10 eV in Stage 1 and `small` means below 0.05 eV. Intermediate results remain unresolved.

## Prohibited inference

> A calculated barrier difference explains the observed 0.32 versus 0.36 STY.

That statement is not licensed until independent active-area, transient, and surface-state contributions are separated.
