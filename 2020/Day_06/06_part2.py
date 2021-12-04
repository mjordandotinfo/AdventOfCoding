f = open("C:/Users/mattr/Documents/Advent-Coding/Day_06/06_input.txt", "r")
content = f.read()
f.close()

myList = content.splitlines()
group = {}
members = 0

allYes = 0

for items in myList:
    if not (items == ""):
        members += 1
        for c in items:
            if not (c in group):
                group[c] = 1
            else:
                group[c] += 1

    else:
        for c in group:
            if group[c] == members:
                allYes += 1
        #if (val == members for val in group.values):
        #    allYes += 1

        #if all(val == members for val in group.values()):
        #print(group, members)
        #    allYes += 1

        members = 0
        group.clear()

for c in group:
    if group[c] == members:
        allYes += 1

print(allYes)