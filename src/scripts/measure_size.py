# measure_size.py
# Measure model size.

import sys
import argparse

sys.path.append("../")

from mlte.measurement import model_size


EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def parse_arguments() -> str:
    """
    Parse commandline arguments.
    :return The path to the model
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="The path to the model.")
    args = parser.parse_args()
    return args.path


def measure(path: str):
    """
    Measure the size of the model.
    :param path The path to the model
    """
    size = model_size(path)
    print(f"Size: {size} bytes")


def main() -> int:
    path = parse_arguments()
    try:
        measure(path)
    except Exception:
        return EXIT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
