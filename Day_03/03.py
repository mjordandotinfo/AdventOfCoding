f = open("C:/Users/mattr/Documents/Advent-Coding/Day_03/03_input.txt", "r")
content = f.read()
myList = content.splitlines()

height = len(myList)
width = len(myList[0])

row = 0
col = 0
trees = 0
totalTrees = []

x = [1, 3, 5, 7, 1]
y = [1, 1, 1, 1, 2]

for i in range(0, len(x)):
    row = 0
    col = 0
    trees = 0

    for row in range(0, height, y[i]):
        if myList[row][col] == "#":
            trees += 1

        col += x[i]

        if col >= width:
            col = col % width
        
    totalTrees.append(trees)

trees = 1
for i in range(0, len(x)):
    trees = trees * totalTrees[i]

print(totalTrees)

print(trees)
