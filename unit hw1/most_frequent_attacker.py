# ANDREA LEE
# 111738212
# ANDRLEE
#
# CSE 337 (Fall 2019)
# Unit Homework 1

from highest_value_key import highest_value_key
from consolidate_sources import consolidate_sources

def most_frequent_attacker(addresses):
    # addresses = string name of plain text file that includes path information
    # return: list of keys with the largest value
    return highest_value_key(consolidate_sources(addresses))


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("The most frequent attacks in test-log-1.txt came from:")
    print(most_frequent_attacker("test-log-1.txt"))
    print()

    print("The most frequent attacks in test-log-2.txt came from:")
    print(most_frequent_attacker("test-log-2.txt"))
    print()

    print("The most frequent attacks in test-log-3.txt came from:")
    print(most_frequent_attacker("test-log-3.txt"))
    print()

    print("The most frequent attacks in test-log-4.txt came from:")
    print(most_frequent_attacker("test-log-4.txt"))
    print()


