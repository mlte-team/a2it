# measurement.py
# Measure machine learning model properties.

import time
import subprocess
from subprocess import SubprocessError

# -----------------------------------------------------------------------------
# CPU Measurement
# -----------------------------------------------------------------------------


class CPUStatistics:
    """
    The CPUStatistics class encapsulates data
    and functionality for tracking and updating
    CPU consumption statistics for a running process.
    """

    def __init__(self, avg: float, min: float, max: float):
        """
        Initialize a CPUStatistics instance
        :param avg The average utilization
        :param min The minimum utilization
        :param max The maximum utilization
        """
        self.avg = avg
        self.min = min
        self.max = max

    def __str__(self) -> str:
        """Return a string representation of CPUStatistics."""
        s = ""
        s += f"Average: {self.avg:.1f}%\n"
        s += f"Minimum: {self.min:.1f}%\n"
        s += f"Maximum: {self.max:.1f}%"
        return s


def _get_cpu_usage(pid: int) -> float:
    """
    Get the current CPU usage for the process with `pid`.
    :param pid The identifier of the process
    :return The current CPU utilization as percentage
    """
    try:
        stdout = subprocess.check_output(["ps", "-p", f"{pid}", "-o", "%cpu"]).decode(
            "utf-8"
        )
        return float(stdout.strip().split("\n")[1].strip())
    except SubprocessError:
        return -1.0
    except ValueError:
        return -1.0


def measure_cpu(pid: int, poll_interval: int = 1) -> CPUStatistics:
    """
    Monitor the CPU utilization of process at `pid` until exit.
    :param pid The process identifier
    :param poll_interval The poll interval in seconds
    :return The collection of CPU usage statistics
    """
    stats = []
    while True:
        util = _get_cpu_usage(pid)
        if util < 0.0:
            break
        stats.append(util)
        time.sleep(poll_interval)

    return CPUStatistics(sum(stats) / len(stats), min(stats), max(stats))


# -----------------------------------------------------------------------------
# Memory Measurement
# -----------------------------------------------------------------------------


class MemoryStatistics:
    """
    The MemoryStatistics class encapsulates data
    and functionality for tracking and updating memory
    consumption statistics for a running process.
    """

    def __init__(self, avg: float, min: int, max: int):
        """
        Initialize a MemoryStatistics instance.
        :param average The average memory consumtion (bytes)
        :param peak The peak memory consumption
        """
        # The statistics
        self.avg = avg
        self.min = min
        self.max = max

    def __str__(self) -> str:
        """Return a string representation of MemoryStatistics."""
        s = ""
        s += f"Average: {int(self.avg)}\n"
        s += f"Minimum: {self.min}\n"
        s += f"Maximum: {self.max}"
        return s


def _get_memory_usage(pid: int) -> int:
    """
    Get the current memory usage for the process with `pid`.
    :param pid The identifier of the process
    :return The current memory usage in KB
    """
    # sudo pmap 917 | tail -n 1 | awk '/[0-9]K/{print $2}'
    try:
        with subprocess.Popen(
            ["pmap", f"{pid}"], stdout=subprocess.PIPE
        ) as pmap, subprocess.Popen(
            ["tail", "-n", "1"], stdin=pmap.stdout, stdout=subprocess.PIPE
        ) as tail:
            used = subprocess.check_output(
                ["awk", "/[0-9]K/{print $2}"], stdin=tail.stdout
            )
        return int(used.decode("utf-8").strip()[:-1])
    except ValueError:
        return 0


def measure_memory(pid: int, poll_interval: int = 1) -> MemoryStatistics:
    """
    Monitor memory consumption of process at `pid` until exit.
    :param pid The process identifier
    :param interval The poll interval, in seconds
    :return The collection of memory usage statistics
    """
    stats = []
    while True:
        kb = _get_memory_usage(pid)
        if kb == 0:
            break
        stats.append(kb)
        time.sleep(poll_interval)

    return MemoryStatistics(sum(stats) / len(stats), min(stats), max(stats))
