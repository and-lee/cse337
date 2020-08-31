# ANDREA LEE
# 111738212
# ANDRLEE
#
# CSE 337 (Fall 2019)
# Unit Homework 2

def validate(filename):
    # file name = string representing the name of a plain-text data file
    # return: dictionary
    # keys = strings
    # values = lists | dictionaries
    errors = {} # return
    rooms = {} # dictionary
    file = open(filename, "r") # open file to read
    details = {}
    end_str = "---" # separator
    # ROOM number = id
    # TITLE & DESC ignored/not used
    # EXIT 4 integers split(). int = room number ROOM identifier. -1 = no exit
    # ITEMS /optional/ string split(). string = item
    # PUZZLE /optional/ 1 string = item needed to solve puzzle
    # parse entire data file. use dict to hold data for each room. key = id number. values = dict
    for line in file: # read file line by line
        line = line.rstrip() # chomp
        class_type = line.split()[0] # first word identifier type
        rest = line[len(class_type)+1:] # content after identifier
        if class_type == "ROOM": # room: id, title, desc, exit, items, puzzle
            id = int(rest) # room id
            rooms.setdefault(id, {}) # key = id            
        else:
            if line == end_str: # new room
                rooms[id] = details # assign values to the room
                details = {} # clear dictionary
            else:
                if class_type == "EXITS":
                    details[class_type] = list(map(int, rest.split())) # list of ints that represent room ids
                elif class_type == "ITEMS" or class_type == "PUZZLE":
                    details[class_type] = rest.split() # list of strings that represent items
                else: # room title & desc = strings
                    details.setdefault(class_type, "")
                    details[class_type] += rest
    rooms[id] = details # last line, last room
    file.close() # close file after done reading
    
    # PHANTOM ROOMS
    # get all room ids. compare with room exits. if exit id DNE = phantom
    # phantoms = list of integers
    all_exits = set()
    for room in rooms:
        exits = set(rooms[room]["EXITS"])
        exits.discard(-1)
        all_exits |= exits
    errors['phantoms'] = list(all_exits - set(rooms.keys()))
    
    # MISSING ITEMS
    # get all items. if a puzzle required item(s) is not in items = missing
    # missing = list of strings
    all_items = set()
    all_puzzles = set()
    for room in rooms:
        if "ITEMS" in rooms[room]:
            all_items |= set(rooms[room]["ITEMS"])
        if "PUZZLE" in rooms[room]:
            all_puzzles |= set(rooms[room]["PUZZLE"])
    errors['missing'] = list(all_puzzles - all_items)
    
    # MISMATCHED EXITS
    # exits = [4]: [0] = north, [1] = east, [2] = south, [3] = west
    # opposite exit = (direction # + 2) % 4
    errors['mismatches'] = [] # mismatches = list of tuples
    for room in rooms: # for each room check each of its four exit directions
        exits = rooms[room]["EXITS"]
        for e in exits:
            if e != -1: # exit not -1
                if e not in rooms.keys(): # check exit room exists # if e in errors['phantoms']:
                    errors['mismatches'].append((room, exits.index(e), "unknown")) # exit room DNE = (room id, exit direction index, "unknown")
                else: # if e in rooms.keys(): # if exit room exits
                    if room != rooms[e]["EXITS"][(exits.index(e)+2) % 4]: # if room's reciprocal exits does not match
                        errors['mismatches'].append((room, exits.index(e), "mismatch")) # (room id, exit direction index, "mismatch")
    
    return errors


# DO NOT DELETE THE FOLLOWING LINES OF CODE! YOU MAY
# CHANGE THE FUNCTION CALLS TO TEST YOUR WORK WITH
# DIFFERENT INPUT VALUES.
if __name__ == "__main__":
    print('validate("map1.txt") produces:', validate("map1.txt"),sep="\n")
    print()
    print('validate("map2.txt") produces:', validate("map2.txt"),sep="\n")
    print()
    print('validate("map3.txt") produces:', validate("map3.txt"),sep="\n")
    print()
    print('validate("map4.txt") produces:', validate("map4.txt"),sep="\n")
    print()
    print()

