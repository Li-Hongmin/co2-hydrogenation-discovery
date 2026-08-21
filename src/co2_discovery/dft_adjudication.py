from __future__ import annotations

import math

BOLTZMANN_EV_K = 8.617333262e-5


def effective_barrier_difference(rate_ratio: float, temperature_k: float) -> float:
    """Diagnostic one-step free-energy scale corresponding to a rate ratio.

    This is a resolvability diagnostic only; it must not be interpreted as
    identifying an elementary rate-controlling barrier.
    """
    if rate_ratio <= 0 or temperature_k <= 0:
        raise ValueError("rate_ratio and temperature_k must be positive")
    return abs(BOLTZMANN_EV_K * temperature_k * math.log(rate_ratio))


def elementary_rate_factor(delta_barrier_ev: float, temperature_k: float) -> float:
    if temperature_k <= 0:
        raise ValueError("temperature_k must be positive")
    return math.exp(abs(delta_barrier_ev) / (BOLTZMANN_EV_K * temperature_k))


def current_gate() -> dict[str, float | str]:
    temperature_k = 573.0
    ratio = 0.32 / 0.36
    return {
        "temperature_k": temperature_k,
        "reported_s4_s1_sty_ratio": ratio,
        "diagnostic_effective_barrier_ev": effective_barrier_difference(ratio, temperature_k),
        "stage1_advance_threshold_ev": 0.10,
        "stage1_stop_threshold_ev": 0.05,
        "interpretation": "DFT discriminates mechanisms; it does not fit the unresolved mass-specific rate residual.",
    }
