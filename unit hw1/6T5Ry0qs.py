# CSE 337 (Fall 2019)
# Unit Homework 1

from highest_value_key import highest_value_key
from consolidate_sources import consolidate_sources
from most_frequent_attacker import most_frequent_attacker
from count_failed_addresses import count_failed_addresses

import os

if __name__ == "__main__":
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if ".log" in f or ".txt" in f:
            print(f + " produced the dictionary:")
            print(count_failed_addresses(f))
            print()

            print(f + " produced the consolidated dictionary:")
            print(consolidate_sources(f))
            print()

            print("The most frequent attacks in " + f + " came from:")
            print(most_frequent_attacker(f))
            print("\n\n\n\n\n")