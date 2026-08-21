import unittest

from co2_discovery.state_recovery import published_s1_s3_s4_recovery


class StateRecoveryTests(unittest.TestCase):
    def test_published_coordinate_mismatch(self):
        result = published_s1_s3_s4_recovery()
        self.assertAlmostEqual(result["mean_in_redox_recovery"], 1.0)
        self.assertAlmostEqual(result["in_o_coordination_recovery"], 8 / 9)
        self.assertAlmostEqual(result["methanol_function_recovery"], 0.5)


if __name__ == "__main__":
    unittest.main()
