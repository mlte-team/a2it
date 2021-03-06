# measure_cpu.py
# Unit tests for 'measurement' module.

import sys
import argparse

sys.path.append("../")

from mlte.measurement import cpu_utilization

# Script exit codes
EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def parse_arguments() -> int:
    """
    Parse commandline arguments.
    :return The process ID to monitor
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("pid", type=int, help="The ID of the process to monitor.")
    args = parser.parse_args()
    return args.pid


def monitor(pid: int):
    """
    Monitor `pid` until exit.
    :param pid The ID of the process
    """
    stats = cpu_utilization(pid)
    print(stats)


def main() -> int:
    pid = parse_arguments()
    try:
        monitor(pid)
    except Exception as e:
        print(e)
        return EXIT_FAILURE
    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
