from __future__ import annotations

import csv
import math
import statistics
from pathlib import Path

STAGES = [
    ("30_initial", 30.0, 2.667, 10.167),
    ("50", 50.0, 10.167, 13.667),
    ("80", 80.0, 13.667, 17.167),
    ("30_return", 30.0, 17.167, None),
]
SETTLING_H = 1.5
PRE_SWITCH_BUFFER_H = 0.5


def _number(row: dict[str, str], key: str) -> float | None:
    try:
        value = float(row[key])
        return value if math.isfinite(value) else None
    except (KeyError, ValueError, TypeError):
        return None


def load_performance_csv(path: Path) -> list[dict[str, float | None]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        source = list(csv.DictReader(handle))
    rows = []
    for row in source:
        runtime = _number(row, "Runtime of Experiment in h")
        if runtime is None:
            continue
        rows.append({
            "runtime_h": runtime,
            "temperature_C": _number(row, "Temperature in °C"),
            "pressure_bar": _number(row, "Pressure in bar"),
            "conversion_pct": _number(row, "Conversion in %"),
            "co_selectivity_pct": _number(row, "CO Selectivty in %"),
            "meoh_selectivity_pct": _number(row, "MeOH Selectivity in %"),
            "sty_mg_g_h": _number(row, "Space Time Yield in mg_MeOH/(g_material*h)"),
            "carbon_balance_pct": _number(row, "Carbon Balance in %"),
            "meoh_rate_mmol_g_h": _number(row, "rate of MeOH formation in mmol_MeOH/(g_material*h)"),
        })
    return rows


def summarize_run(path: Path, run_id: str) -> list[dict[str, float | str | int | None]]:
    points = load_performance_csv(path)
    summaries = []
    for stage, flow, start, end in STAGES:
        lo = start + SETTLING_H
        hi = math.inf if end is None else end - PRE_SWITCH_BUFFER_H
        selected = [
            p for p in points
            if lo <= float(p["runtime_h"]) <= hi
            and p["temperature_C"] == 300.0
            and p["pressure_bar"] == 20.0
            and p["sty_mg_g_h"] is not None
        ]
        row: dict[str, float | str | int | None] = {
            "run": run_id,
            "stage": stage,
            "flow_ml_min": flow,
            "window_start_h": lo,
            "window_end_h": None if math.isinf(hi) else hi,
            "n_points": len(selected),
        }
        for key in (
            "sty_mg_g_h", "conversion_pct", "carbon_balance_pct",
            "meoh_selectivity_pct", "co_selectivity_pct", "meoh_rate_mmol_g_h"
        ):
            values = [float(p[key]) for p in selected if p[key] is not None]
            row[f"{key}_mean"] = statistics.mean(values) if values else None
            row[f"{key}_sd"] = statistics.stdev(values) if len(values) >= 2 else None
        summaries.append(row)

    baseline = float(summaries[0]["sty_mg_g_h_mean"])
    for row in summaries:
        sty = float(row["sty_mg_g_h_mean"])
        flow = float(row["flow_ml_min"])
        row["sty_ratio_to_initial30"] = sty / baseline
        if flow != 30.0:
            row["apparent_flow_exponent_alpha"] = math.log(sty / baseline) / math.log(flow / 30.0)
        else:
            row["apparent_flow_exponent_alpha"] = None
    return summaries


def write_summary(paths: list[tuple[str, Path]], output: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for run_id, path in paths:
        rows.extend(summarize_run(path, run_id))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return rows


if __name__ == "__main__":
    base = Path("large-data/in2o3_zenodo/in2o3_s3_s4_and_lab_activity/18_Figure_S12_S13_catalysis_lab")
    write_summary(
        [("II", base / "In2O3_5Zr_catalytic_test_II.csv"),
         ("III", base / "In2O3_5Zr_catalytic_test_III.csv")],
        Path("outputs/5zr_flow_stage_summary.csv"),
    )
