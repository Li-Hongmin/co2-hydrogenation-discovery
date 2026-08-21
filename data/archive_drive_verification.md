# Drive archive verification

Checked 2026-08-21 through the connected Google Drive.

The extraction note states that the original `Dataset_Experimental_and_DFT` archive is approximately 23.67 GiB and has been split into 12 parts for cloud transfer:

- `.z01` through `.z11`: 2 GiB each;
- final `.zip`: approximately 1.67 GiB;
- all 12 parts required.

The Drive-side note reports that the parts were recombined and `unzip -t` passed for 11,327 entries with no data corruption.

A Drive-side `SHA256SUMS.txt` records checksums for every part. This GitHub repository intentionally records only metadata and derived manifests; the raw split archive remains in Drive.

Next required derived files: `archive_manifest.csv`, `archive_candidates.csv`, and `archive_summary.json`. These should be generated locally from the split ZIP central directory and then committed here; they are not yet present in Drive as of this verification.
