# ANDREA LEE
# 111738212
# ANDRLEE
#
# CSE 337 (Fall 2019)
# Unit Homework 1

from count_failed_addresses import count_failed_addresses

def consolidate_sources(logname):
    # logname = string name of a log file
    # return: dictionary
    # keys = strings representing three octets of a dotted-quad IP address
    # values = integers
    octet_dict = {}
    sources = count_failed_addresses(logname) # key = ip address, value = count
    for key in sources:
        octets = key.split(".") # array containing octets of an ip address
        three_octet = ".".join(octets[0:3]) # get three octets
        octet_dict.setdefault(three_octet, 0) # add octet to dic
        octet_dict[three_octet] += sources[key] # increment count
    return octet_dict


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the consolidated dictionary:")
    print(consolidate_sources("test-log-4.txt"))
    print()

