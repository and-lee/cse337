# Andrea Lee
# 111738212
# andrlee
#
# CSE 337 (Fall 2019)
# Minor Homework 1, Problem 1

def burger(order):
    # ONLY 1 protein B/T/V, 0-5 toppings, 0-2 condiments
    # toppings/condiments can be repeated and still count towards limit
    # any order
    
    protein_cost = 0
    topping_num = 0
    condiment_num = 0
    protein = "BTV"
    toppings = "ltopjcbsmf"
    condiments = "kuyaq"
    for e in order:
        if e not in protein+toppings+condiments: # invalid character
            return "unrecognized order code"
        
        if e in toppings:
            topping_num+=1
        if e in condiments:
            condiment_num+=1
        if e in protein:
            if e == "B":
                protein_cost+=2
            if e == "T":
                protein_cost+=2.5
            if e == "V":
                protein_cost+=2.25
        if topping_num>5 or condiment_num>2 or protein_cost>2.5: # 1 protein, 0-5 toppings, 0-2 condiments
            return "invalid order"
    if protein_cost == 0: # 0 protein
        return "invalid order"
    return protein_cost + (0.5 * topping_num)


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('burger("Bck"):', burger("Bck")) # simple cheeseburger
    print()
    print('burger("Tpmlmy"):', burger("Tpmlmy")) # turkey burger w/ stuff
    print()
    print('burger("altop"):', burger("altop")) # error: no protein
    print()
    print('burger("VtojsT"):', burger("VtojsT")) # error: too many protein choices
    print()
    print('burger("lsucjV"):', burger("lsucjV")) # okay; protein at end
    print()
    print('burger("Bqcbksmfy"):', burger("Bqcbksmfy")) # error: too many condiments
    print()
    print('burger("Toxpk"):', burger("Toxpk")) # error: invalid character (x)
    print()
    print('burger("Vqltopjm"):', burger("Vqltopjm")) # error: too many toppings
    print()

