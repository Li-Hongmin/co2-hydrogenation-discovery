# Current raw-data blocker

The Drive upload/integrity gate is complete. The remaining blocker is only selective indexing: `archive_manifest.csv`, `archive_candidates.csv`, and `archive_summary.json` have not yet appeared in Drive. Once present, the raw-data audit can begin without moving the full 23.67 GiB archive into GitHub.
