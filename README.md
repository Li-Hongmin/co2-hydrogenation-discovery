# CO2 Hydrogenation Discovery

Mechanism-first research workspace for AI-assisted discovery in CO2 hydrogenation catalysis.

## Current system

Zr-doped cubic In2O3 for CO2 hydrogenation to methanol, with raw laboratory data now available for multiple Zr loadings.

## Research strategy

The project does not treat AI as a generic activity predictor. AI is used to maintain competing mechanistic hypotheses, identify discriminating observations, freeze falsifiable predictions before new outcomes are available, and select the smallest decisive experiment or calculation.

### Current milestones

1. **Catalytic-state recovery mismatch.** Published S1→S3→S4 point estimates show complete recovery of mean In redox state after CO2-only reoxidation but incomplete recovery of methanol function. The earlier single-peak XRD-width/activity closure is retained only as a clue, not as causal evidence.
2. **Matched-redox regeneration.** The experimental program asks whether different regeneration paths can reach the same operando redox endpoint while producing different morphology, surface chemistry, or catalytic function.
3. **Matched-redox hysteresis.** A reversible CO2-composition loop is designed to test whether identical external conditions and matched ensemble-average redox spectra can retain different methanol rates because of a slower hidden state variable.
4. **Bounded DFT adjudication.** DFT is not used to fit the unresolved ~11% S1/S4 mass-specific rate difference. It tests large paired contrasts in H-pair thermodynamics, direct CO2 vacancy healing, H2COOH scission, and—only when triggered—vacancy migration or interface reconstruction.
5. **Raw-data kinetic-validity gate.** Four extracted Zr-doped laboratory flow ramps (two 5% Zr runs plus 10% and 20% Zr) show a reproducible 30→50→80→30 mL min−1 response at fixed nominal 20/60/20 N2/H2/CO2, 300 °C and 20 bar. Run-normalized STY rises on average by 18.3% at 50 mL min−1 and 32.1% at 80 mL min−1, then returns to the initial 30 mL min−1 rate with mean return/initial ratio 1.0047. The present laboratory STY is therefore not yet licensed as a flow-invariant intrinsic kinetic observable; transport/contact-time/product-state effects must be adjudicated before small mechanism-level rate differences are fitted.

See `studies/001_in2o3_state_memory/LAB_FLOW_DEPENDENCE_GATE.md` and `outputs/zr_flow_stage_summary.csv` for the raw-data result and interpretation boundary.

## Immediate decision order

1. Resolve the flow/transport/contact-time gate with a crossed W/F × superficial-velocity experiment.
2. Only after a transport-valid rate observable is defined, return to the S1/S4 delayed-reactivation and matched-redox state questions.
3. Trigger expensive surface DFT only for a residual experimentally identified state coordinate, not for the unresolved mass-specific STY difference.

## Evidence boundary

The full experimental/DFT archive associated with the 2026 Nature Communications Zr/Sn-In2O3 study is stored separately in Google Drive because of its size. Large raw data are intentionally excluded from GitHub. Small derived summaries and deterministic analysis code are committed here.

## Repository policy

- Separate observations, derived quantities, interpretations, and unresolved hypotheses.
- Preserve explicit stop rules for failed mechanisms.
- Do not infer statistical significance from published point estimates without replicate uncertainty.
- Do not expand DFT/MLIP campaigns before an experimentally unresolved structural coordinate is identified.
- Do not call mass-specific STY an intrinsic kinetic observable until flow/transport/contact-time validity has been established in the relevant operating window.
- Keep large raw archives out of Git.
