import unittest

from co2_discovery.dft_adjudication import current_gate, effective_barrier_difference


class DFTAdjudicationTests(unittest.TestCase):
    def test_s4_s1_diagnostic_is_few_mev(self):
        value = effective_barrier_difference(0.32 / 0.36, 573.0)
        self.assertGreater(value, 0.005)
        self.assertLess(value, 0.0065)

    def test_stage1_threshold_is_deliberately_larger(self):
        gate = current_gate()
        self.assertGreater(gate["stage1_advance_threshold_ev"], 10 * gate["diagnostic_effective_barrier_ev"])


if __name__ == "__main__":
    unittest.main()
