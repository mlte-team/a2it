# measure_mean_latency
# Example script for mean latency measurement.

import sys

sys.path.append("../")

import time
import numpy as np

from mlte.measurement import mean_latency

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


class Model:
    """A dummy model class."""

    def __init__(self):
        pass

    def __call__(self, duration: float):
        """Sleep for a duration specified in ms."""
        time.sleep(duration / 1000)


class InputGenerator:
    """A dummy input generator."""

    def __init__(self):
        pass

    def __call__(self) -> float:
        """Return a uniformly-distributed duration (ms)"""
        return np.random.normal(loc=100.0)


def main() -> int:
    m = Model()
    g = InputGenerator()
    l = mean_latency(m, g, trials=100)
    print(f"Mean latency: {l:.2f}ms")
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
