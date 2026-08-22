# Raw-data milestone — kinetic-validity gate from reversible total-flow dependence

## Result

Raw laboratory catalytic tests for nominal 5 at-% Zr-doped In2O3 contain two independent runs (II and III) in which the reactor was held at 300 °C and 20 bar with the same nominal inlet composition (20/60/20 N2/H2/CO2) while total flow was changed approximately 30 → 50 → 80 → 30 mL min−1.

To avoid gas-switch transients, the analysis discards the first 1.5 h after each flow change and the final 0.5 h before the next change. The final return-to-30 stage is evaluated after the same 1.5 h settling interval. No single transient point is used to define a plateau.

| Run | Stage | Mean STY (mg MeOH g−1 h−1) | Mean CO2 conversion (%) | Mean carbon balance (%) | STY / initial 30 |
|---|---|---:|---:|---:|---:|
| II | 30 initial | 563.9 | 0.929 | 94.67 | 1.000 |
| II | 50 | 654.9 | 0.648 | 95.80 | 1.161 |
| II | 80 | 732.5 | 0.465 | 95.35 | 1.299 |
| II | 30 return | 558.1 | 0.901 | 95.89 | 0.990 |
| III | 30 initial | 568.2 | 0.933 | 98.43 | 1.000 |
| III | 50 | 695.4 | 0.668 | 100.57 | 1.224 |
| III | 80 | 776.4 | 0.479 | 100.22 | 1.366 |
| III | 30 return | 579.1 | 0.922 | 99.29 | 1.019 |

Across the two runs, increasing total flow from 30 to 50 mL min−1 increases the run-normalized STY by **19.3% on average**; 30 to 80 mL min−1 increases it by **33.3% on average**. Returning to 30 mL min−1 restores the original rate to within about ±2% (mean ratio 1.004). The apparent log–log flow exponent over the 30–80 mL min−1 stages is approximately 0.27 in run II and 0.32 in run III.

At the same time, conversion decreases from approximately 0.93% at 30 mL min−1 to 0.65–0.67% at 50 mL min−1 and 0.47–0.48% at 80 mL min−1. Carbon balance remains close to the run baseline and does not move in the direction needed to explain the STY increase as a carbon-accounting artifact.

## Licensed interpretation

Under an ideal differential intrinsic-kinetics interpretation at fixed inlet partial pressures, temperature, catalyst mass and pressure, mass-specific rate should be approximately invariant to total flow once heat/mass-transfer and product/contact-time effects are negligible. The repeated, reversible 19–33% flow response therefore shows that the laboratory STY in this operating window is **not yet licensed as a flow-invariant intrinsic kinetic observable**.

This observation does **not** identify the cause. The live explanations are:

1. external film mass transfer or another superficial-velocity-dependent transport effect;
2. axial contact-time/product inhibition, including H2O and/or methanol accumulation;
3. a reversible catalyst-state response coupled to product chemical potentials or residence time;
4. a reactor thermal/measurement effect not captured by the logged bulk temperature and pressure.

The near-complete recovery of the original 30 mL min−1 STY after the 80 mL min−1 stage argues against irreversible catalyst activation during the flow ramp as the sole explanation.

## Why this changes the project

The state-memory and DFT branches require an intrinsic-rate interpretation at some point. Until the flow dependence is adjudicated, small differences such as the published S1/S4 mass-specific STY difference cannot safely be assigned to a surface barrier, vacancy topology, or morphology-normalized intrinsic rate. The kinetic-validity gate therefore precedes expensive mechanism fitting.

## Cheapest decisive experiment

Run a crossed transport/contact-time design on the 5% Zr catalyst:

- **Superficial-velocity contrast at matched W/F:** scale catalyst mass proportionally with total flow (for example 30 mL min−1 with mass W and 60 mL min−1 with mass 2W), while keeping inlet composition, T, P, particle size and dilution protocol fixed. A persistent rate-per-mass change at matched W/F implicates an external-transport/velocity effect.
- **Contact-time contrast at approximately matched superficial velocity:** change W/F through catalyst mass or bed dilution while holding total flow/velocity approximately fixed. A rate change here implicates product/contact-time or state relaxation rather than film transfer alone.
- **Trace-H2O perturbation at the high-flow condition:** if high-flow STY decreases toward the low-flow value under controlled H2O addition without a structural change, product/water inhibition becomes a strong mechanism candidate.
- **Particle-size series:** retain as an orthogonal transport control if the first two contrasts do not close the effect.

A transport-free operating window should be defined before using STY differences for DFT barrier adjudication or a matched-redox state-memory claim.

## Evidence boundary

This result comes from two raw 5% Zr laboratory flow-ramp runs. It is replicated descriptively but does not yet provide enough independent runs for a strong inferential estimate of the flow exponent. The 5% Sn triplicate files in the same archive are long stability/deactivation tests at approximately 30 mL min−1 rather than matched flow ramps, so they are not a valid direct control for this question.
