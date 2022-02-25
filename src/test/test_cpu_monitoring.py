# test_cpu_monitoring.py
# Unit tests for 'monitoring' module.

import sys
import argparse

sys.path.append("../")

from mlte.monitoring import monitor_cpu

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
    stats = monitor_cpu(pid)
    print(f"Avg: {stats.avg:.1f}%\nMin: {stats.min:.1f}%\nMax: {stats.max:.1f}%")


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
