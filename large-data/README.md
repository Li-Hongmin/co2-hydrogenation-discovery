# Large-data boundary

Large experimental and DFT archives are stored outside GitHub.

Current primary archive: `Dataset_Experimental_and_DFT`, associated with the Zr/Sn-In2O3 CO2-to-methanol study. The Google Drive copy is stored as a 12-part split ZIP because the original archive is approximately 23.67 GiB.

Expected parts:

- `Dataset_Experimental_and_DFT_split.z01` … `.z11` (2 GiB each)
- `Dataset_Experimental_and_DFT_split.zip` (final part, approximately 1.67 GiB)
- `SHA256SUMS.txt`

The Drive-side extraction note reports that the reconstructed archive passed `unzip -t` for 11,327 entries. Raw archive parts must never be committed to GitHub.

The next derived artifacts to commit are a small archive manifest and ranked candidate-file list identifying GC/MS, operando XRD, In/Zr XAS, Figure-6/S1-S5, and DFT vacancy/local-environment data.
