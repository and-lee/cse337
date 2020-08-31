# ANDREA LEE
# 111738212
# ANDRLEE
#
# CSE 337 (Fall 2019)
# Unit Homework 1

def count_failed_addresses(logname):
    # logname = string name of a plain text file that includes path information
    # return: dictionary
    # keys = strings of corresponding IP addresses in dotted-quad format
    # values = positive integer
    failed_str = "Disconnected from" # string ip address follows
    file = open(logname, "r") # open read file
    failed = {} # dict
    for line in file: # read file line by line
        if line.find(failed_str) != -1: # if line contains string
            address = (line[line.index(failed_str)+len(failed_str)+1:]).split()[0] # get first word after string
            failed.setdefault(address, 0) # add address to dic
            failed[address] += 1 # increment count
    file.close()
    return failed


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print("test-log-1.txt produced the dictionary:")
    print(count_failed_addresses("test-log-1.txt"))
    print()

    print("test-log-2.txt produced the dictionary:")
    print(count_failed_addresses("test-log-2.txt"))
    print()

    print("test-log-3.txt produced the dictionary:")
    print(count_failed_addresses("test-log-3.txt"))
    print()

    print("test-log-4.txt produced the dictionary:")
    print(count_failed_addresses("test-log-4.txt"))
    print()


