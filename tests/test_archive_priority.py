import unittest

from co2_discovery.archive_priority import score_archive_path


class ArchivePriorityTests(unittest.TestCase):
    def test_state_xas_file_ranks_above_generic_dft_file(self):
        self.assertGreater(score_archive_path("Figure_6/S4/In_K_XANES.dat"), score_archive_path("misc/notes.txt"))


if __name__ == "__main__":
    unittest.main()
