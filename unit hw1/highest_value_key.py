# ANDREA LEE
# 111738212
# ANDRLEE
#
# CSE 337 (Fall 2019)
# Unit Homework 1

def highest_value_key(data):
    # data = non-empty dictionary with non-negative integer value keys
    # return: list containing ALL keys with the highest value
    highest_values = []
    highest = max(data.values()) # get maximum value of dict
    for key in data: # itterate through dict to get keys
        if data[key] == highest:
            highest_values.append(key) # append key to list
    return highest_values[0] if len(highest_values) == 1 else highest_values


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    d1 = {18: 8, 'Zeus': 8, 1: 4, 'Hermes': 25, 'Ares': 7, 2: 7}
    print("Given the dictionary", d1)
    print("The highest-valued key is", highest_value_key(d1))
    print()

    d2 = {10: 23, 'Hera': 8, 11: 23, 2: 13}
    print("Given the dictionary", d2)
    print("The highest-valued key is", highest_value_key(d2))
    print()

    d3 = {12: 21, 19: 2, 'Hermes': 15, 6: 11, 17: 10, 16: 2, 13: 22, 18: 25, 11: 4, 15: 15, 2: 20, 9: 10, 20: 17}
    print("Given the dictionary", d3)
    print("The highest-valued key is", highest_value_key(d3))
    print()

    d4 = {15: 20, 6: 22, 'Ares': 22, 11: 21}
    print("Given the dictionary", d4)
    print("The highest-valued key is", highest_value_key(d4))
    print()


