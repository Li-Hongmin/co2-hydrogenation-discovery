from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit

TARGETS = (30.6, 35.5, 51.0, 60.7)


def pseudo_voigt(x, amplitude, center, fwhm, eta, background, slope):
    gamma = fwhm / 2.0
    lorentz = 1.0 / (1.0 + ((x - center) / gamma) ** 2)
    gaussian = np.exp(-4.0 * np.log(2.0) * ((x - center) / fwhm) ** 2)
    return background + slope * (x - center) + amplitude * (eta * lorentz + (1.0 - eta) * gaussian)


def fit_peak(path: Path, target: float) -> dict[str, float]:
    data = np.loadtxt(path)
    x, y = data[:, 0], data[:, 1]
    mask = (x > target - 0.8) & (x < target + 0.8)
    xx, yy = x[mask], y[mask]
    center0 = float(xx[np.argmax(yy)])
    background0 = float(np.percentile(yy, 10))
    p0 = [float(yy.max() - background0), center0, 0.25, 0.5, background0, 0.0]
    lower = [0.0, target - 0.4, 0.03, 0.0, -np.inf, -np.inf]
    upper = [np.inf, target + 0.4, 1.5, 1.0, np.inf, np.inf]
    popt, pcov = curve_fit(pseudo_voigt, xx, yy, p0=p0, bounds=(lower, upper), maxfev=50000)
    errors = np.sqrt(np.diag(pcov))
    return {
        "target_2theta_deg": target,
        "center_2theta_deg": float(popt[1]),
        "observed_fwhm_deg": float(popt[2]),
        "pseudo_voigt_eta": float(popt[3]),
        "fwhm_fit_se_deg": float(errors[2]),
    }


def main() -> None:
    source = Path("large-data/in2o3_zenodo/in2o3_s3_s4_and_lab_activity/14_Figure_S4_XRD_In2O3_xSn_xZr")
    files = {
        "5Zr": source / "In2O3_5Zr_c650.ASC",
        "10Zr": source / "In2O3_10Zr_c650.ASC",
        "20Zr": source / "In2O3_20Zr_c650.ASC",
    }
    rows = []
    for sample, path in files.items():
        for target in TARGETS:
            row = {"sample": sample, **fit_peak(path, target)}
            rows.append(row)
    out = Path("outputs/zr_xrd_peak_fit_summary.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)


if __name__ == "__main__":
    main()
