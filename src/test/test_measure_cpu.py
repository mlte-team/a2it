# test_measure_cpu.py
# Unit tests for `measurement` module.

import os
import sys

sys.path.append("../")

import unittest
import threading
import subprocess

from mlte.measurement import measure_cpu


def support_path() -> str:
    """Get the absolute path to the support directory."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "support/")


def spin_for(seconds: int):
    """Run the spin.py program for `seconds`."""
    path = os.path.join(support_path(), "spin.py")
    prog = subprocess.Popen(["python", path, f"{seconds}"])
    thread = threading.Thread(target=lambda: prog.wait())
    thread.start()
    return prog


class TestMeasureCpu(unittest.TestCase):
    def test(self):
        prog = spin_for(5)

        stat = measure_cpu(prog.pid)
        self.assertTrue(len(str(stat)) > 0)


if __name__ == "__main__":
    unittest.main()
