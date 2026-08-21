from __future__ import annotations


def fractional_recovery(reference: float, damaged: float, recovered: float) -> float:
    """Fraction of a reference-to-damaged loss recovered in a final state."""
    denominator = reference - damaged
    if denominator == 0:
        raise ValueError("reference and damaged values must differ")
    return (recovered - damaged) / denominator


def published_s1_s3_s4_recovery() -> dict[str, float]:
    """Derived from published point estimates; not uncertainty-aware."""
    return {
        "mean_in_redox_recovery": fractional_recovery(2.9, 2.4, 2.9),
        "in_o_coordination_recovery": fractional_recovery(5.8, 4.9, 5.7),
        "methanol_function_recovery": fractional_recovery(0.36, 0.28, 0.32),
    }
