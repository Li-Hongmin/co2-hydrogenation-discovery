from __future__ import annotations

import csv
import sys
from pathlib import Path

from co2_discovery.archive_priority import score_archive_path


def main(path: str) -> None:
    rows = []
    with Path(path).open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            archive_path = row.get("path") or row.get("name") or row.get("filename") or ""
            row["priority_score"] = score_archive_path(archive_path)
            rows.append(row)
    for row in sorted(rows, key=lambda item: int(item["priority_score"]), reverse=True)[:100]:
        print(row)


if __name__ == "__main__":
    main(sys.argv[1])
