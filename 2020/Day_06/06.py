f = open("C:/Users/mattr/Documents/Advent-Coding/Day_06/06_input.txt", "r")
content = f.read()
f.close()

myList = content.splitlines()
group = []

uniqueYes = 0

for items in myList:
    if not (items == ""):
        for c in items:
            if not (c in group):
                group.append(c)
                uniqueYes += 1

    else:
        group.clear()

print(uniqueYes)