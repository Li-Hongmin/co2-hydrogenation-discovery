from __future__ import annotations


PRIORITY_TERMS = (
    "figure 6", "fig6", "state 1", "state 2", "state 3", "state 4", "s1", "s2", "s3", "s4",
    "gc", "ms", "methanol", "sty", "xanes", "exafs", "xrd", "zr k", "in k", "vacancy", "dft",
)


def score_archive_path(path: str) -> int:
    text = path.lower().replace("_", " ").replace("-", " ")
    return sum(1 for term in PRIORITY_TERMS if term in text)
