# Raw-data milestone — kinetic-validity gate from reversible total-flow dependence

## Result

The extracted laboratory archive contains **four Zr-doped In2O3 flow-ramp runs spanning three Zr loadings**: two independent 5% Zr runs plus one 10% Zr and one 20% Zr run. In each case the reactor is held at approximately 300 °C and 20 bar with the same nominal inlet composition (20/60/20 N2/H2/CO2), while total flow is changed approximately 30 → 50 → 80 → 30 mL min−1.

To avoid switch transients, the plateau analysis discards the first 1.5 h after each flow change and the final 0.5 h before the next change. The final return-to-30 stage is evaluated after the same 1.5 h settling interval. This excludes, for example, the isolated high-STY transient immediately before the 50→80 switch in 5% Zr run III.

| Catalyst / run | STY at 30 | STY at 50 | STY at 80 | Return 30 | 50/30 | 80/30 | return/initial |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5Zr II | 563.9 | 654.9 | 732.5 | 558.1 | 1.161 | 1.299 | 0.990 |
| 5Zr III | 568.2 | 695.4 | 776.4 | 579.1 | 1.224 | 1.366 | 1.019 |
| 10Zr I | 505.6 | 589.2 | 657.4 | 502.7 | 1.165 | 1.300 | 0.994 |
| 20Zr I | 500.4 | 590.6 | 660.4 | 508.2 | 1.180 | 1.320 | 1.016 |

STY units are mg MeOH g_material−1 h−1.

Across all four flow ramps, increasing total flow from 30 to 50 mL min−1 increases run-normalized STY by **18.3% on average** (range 16.1–22.4%). Increasing flow to 80 mL min−1 increases STY by **32.1% on average** (range 29.9–36.6%). Returning to 30 mL min−1 restores the initial STY almost exactly: mean return/initial ratio **1.0047**, range 0.990–1.019.

The response is therefore not a one-run anomaly and is not confined to one Zr loading. A log–log fit of plateau STY against flow gives an apparent flow exponent of approximately 0.27 (5Zr II), 0.32 (5Zr III), 0.27 (10Zr), and 0.28 (20Zr).

At the same time, CO2 conversion falls systematically as flow increases. Representative initial→80 mL min−1 changes are approximately 0.93→0.47% for 5Zr, 0.86→0.44% for 10Zr, and 0.79→0.40% for 20Zr. Carbon balances remain near their run baselines and the rate returns after restoring the original flow, arguing against a simple carbon-accounting artifact or irreversible activation as the sole explanation.

## Orthogonal XRD check across Zr loading

The ex situ c650 XRD patterns for 5, 10 and 20% Zr were also refit with the same local pseudo-Voigt procedure at four prominent In2O3 reflections. This is not an instrument-corrected crystallite-size analysis; it is used only to ask whether the three materials are structurally identical at the level of observed peak position/width.

At the ~30.6° reflection, observed FWHM is approximately 0.754° (5Zr), 0.741° (10Zr), and 0.822° (20Zr). The 20Zr peak is also shifted to lower 2θ (~30.550° versus ~30.602° for 5Zr). Similar broadening/shift is present at the other fitted reflections. Thus 20Zr is measurably different in observed diffraction profile from the lower-Zr samples, yet its normalized flow response is nearly the same: 50/30 = 1.180 and 80/30 = 1.320.

This does **not** rule out external mass transfer, because transport can remain similar across these materials and the observed width is not a particle-size measurement. It does, however, make a sample-specific irreversible structural activation explanation less attractive: a common reversible flow/contact-time phenomenon persists across materials with distinguishable diffraction profiles.

The fitted peak values are stored in `outputs/zr_xrd_peak_fit_summary.csv`. Instrument broadening and microstrain have not been separated, so these FWHM values must not be converted into definitive crystallite sizes.

## Licensed interpretation

Under an ideal differential intrinsic-kinetics interpretation at fixed inlet partial pressures, temperature, catalyst mass and pressure, mass-specific rate should be approximately invariant to total flow once heat/mass-transfer and product/contact-time effects are negligible. The repeated, reversible ~18–32% flow response across three Zr loadings therefore shows that the laboratory STY in this operating window is **not yet licensed as a flow-invariant intrinsic kinetic observable**.

This result is stronger than the earlier 5Zr-only observation because the same directional and near-quantitative response recurs across 5, 10 and 20% Zr materials. It suggests a common reactor/contact-time phenomenon or a common product-chemical-potential/state response rather than an idiosyncratic catalyst activation event.

The data do **not** identify which of the following mechanisms dominates:

1. external film mass transfer or another superficial-velocity-dependent transport effect;
2. axial contact-time/product inhibition, including H2O and/or methanol accumulation;
3. a reversible catalyst-state response coupled to product chemical potentials or residence time;
4. a reactor thermal/measurement effect not captured by the logged bulk temperature and pressure.

## Why this changes the project

The state-memory and DFT branches require an intrinsic-rate interpretation at some point. Until the flow dependence is adjudicated, small differences such as the published S1/S4 mass-specific STY difference cannot safely be assigned to a surface barrier, vacancy topology, or morphology-normalized intrinsic rate. The kinetic-validity gate therefore moves **ahead of** expensive mechanism fitting.

The important point is not that all existing mechanistic conclusions are wrong. It is that the raw laboratory archive itself provides a direct warning that rate per catalyst mass is sensitive to reactor throughput even below 1% conversion. Any later claim of an intrinsic state effect must survive this reactor-level control.

## Cheapest decisive experiment

Run a crossed transport/contact-time design, beginning with 5% Zr and confirming the resolved result on one additional Zr loading:

- **Superficial-velocity contrast at matched W/F:** scale catalyst mass proportionally with total flow (for example 30 mL min−1 with mass W and 60 mL min−1 with mass 2W), while keeping inlet composition, T, P, particle size and dilution protocol fixed. A persistent rate-per-mass change at matched W/F supports an external-velocity/film-transfer contribution.
- **Contact-time contrast at approximately matched superficial velocity:** change W/F through catalyst mass or bed dilution while holding total flow/velocity approximately fixed. A rate change here supports product/contact-time or state relaxation rather than film transfer alone.
- **Trace-H2O perturbation at the high-flow condition:** after transport checks, add a controlled low H2O partial pressure. If high-flow STY moves toward the low-flow value with a coherent surface-state response, water/product inhibition becomes a strong mechanism candidate.
- **Particle-size series:** retain as an orthogonal transport control if the first two contrasts do not close the effect.

A transport-valid operating window should be defined before using STY differences for DFT barrier adjudication or a matched-redox state-memory claim.

## Evidence boundary

The 5% Zr response is independently repeated twice; 10% and 20% Zr each provide one additional flow ramp. This is strong descriptive replication of the phenomenon but not a balanced factorial study across dopant loading. The 5% Sn triplicate files in the same extracted archive are long stability/deactivation experiments at approximately 30 mL min−1 rather than matched flow ramps, so they are not a valid direct control for the flow effect.

Derived values are stored in `outputs/zr_flow_stage_summary.csv`; the original large experimental archive remains outside GitHub.
