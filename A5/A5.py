"""
-------------------------
# Student Name: Ryan Rodricks
# Student ID: 190499940
# Student email: rodr9940@mylaurier.ca
#-------------------------
"""

from pqueue import pQueue


class Process:
    def __init__(self, PID, time, arrival):
        assert isinstance(PID, int) and len(str(PID)) == 10, "Invalid PID"
        assert isinstance(arrival, int) and arrival >= 0, "Invalid arrival"
        assert isinstance(time, int) and time >= 0, "Invalid time"

        self.PID = PID
        self.arrival = arrival
        self.time = time

    def __str__(self):
        return "[{}]({},{})".format(self.arrival, self.PID, self.time)

    def key(self):
        return self.PID

    def __eq__(self, other):
        return self.arrival == other.arrival and self.time == other.time and self.PID == other.PID

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.arrival > other.arrival:
            return True
        elif self.arrival < other.arrival:
            return False
        elif self.time > other.time:
            return True
        elif self.time < other.time:
            return False
        elif self.PID > other.PID:
            return True

        return False

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        if self.arrival < other.arrival:
            return True
        elif self.arrival > other.arrival:
            return False
        elif self.time < other.time:
            return True
        elif self.time > other.time:
            return False
        elif self.PID < other.PID:
            return True
        return False

    def __le__(self, other):
        return self < other or self == other


def read_processes(filename):
    processes = []
    x = ""
    with open(filename, "r") as f:
        for line in f:
            processes.append(line.strip("\n"))

    return processes


def schedule(filename, scheduler_type):
    list = []


    return


def schedule_FIFO(processes):
    # your code here
    return


def schedule_SJF(processes):
    # your code here
    return
