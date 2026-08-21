# CO2 Hydrogenation Discovery

Mechanism-first research workspace for AI-assisted discovery in CO2 hydrogenation catalysis.

## Current system

Zr-doped cubic In2O3 (`In1.9Zr0.1O3.05`) for CO2 hydrogenation to methanol.

## Research strategy

The project does not treat AI as a generic activity predictor. AI is used to maintain competing mechanistic hypotheses, identify discriminating observations, freeze falsifiable predictions before new outcomes are available, and select the smallest decisive experiment or calculation.

### Current milestones

1. **Catalytic-state recovery mismatch.** Published S1→S3→S4 point estimates show complete recovery of mean In redox state after CO2-only reoxidation but incomplete recovery of methanol function. The earlier single-peak XRD-width/activity closure is retained only as a clue, not as causal evidence.
2. **Matched-redox regeneration.** The experimental program asks whether different regeneration paths can reach the same operando redox endpoint while producing different morphology, surface chemistry, or catalytic function.
3. **Matched-redox hysteresis.** A reversible CO2-composition loop is designed to test whether identical external conditions and matched ensemble-average redox spectra can retain different methanol rates because of a slower hidden state variable.
4. **Bounded DFT adjudication.** DFT is not used to fit the unresolved ~11% S1/S4 mass-specific rate difference. It tests large paired contrasts in H-pair thermodynamics, direct CO2 vacancy healing, H2COOH scission, and—only when triggered—vacancy migration or interface reconstruction.

## Evidence boundary

The full experimental/DFT archive associated with the 2026 Nature Communications Zr/Sn-In2O3 study is stored separately in Google Drive because of its size. Large raw data are intentionally excluded from GitHub.

## Repository policy

- Separate observations, derived quantities, interpretations, and unresolved hypotheses.
- Preserve explicit stop rules for failed mechanisms.
- Do not infer statistical significance from published point estimates without replicate uncertainty.
- Do not expand DFT/MLIP campaigns before an experimentally unresolved structural coordinate is identified.
- Keep large raw archives out of Git.
