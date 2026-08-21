# Google Drive status — 2026-08-21

Verified through the connected Drive integration:

- `README_HOW_TO_EXTRACT.md` describes a 12-part split archive reconstructed from the original ~23.67 GiB ZIP.
- The note reports successful `unzip -t` validation of 11,327 entries with no data corruption.
- `SHA256SUMS.txt` contains SHA-256 values for `.z01` through `.z11` and the final `.zip` part.
- `RUN_SPLIT_ZIP_MANIFEST.md` is present.
- A search for the derived `archive_manifest` did not yet find `archive_manifest.csv`, `archive_candidates.csv`, or `archive_summary.json`.

Therefore the large-data upload/integrity gate is passed; the selective-indexing gate remains open.
