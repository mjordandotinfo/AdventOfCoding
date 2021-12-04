f = open("C:/Users/mattr/Documents/Advent-Coding/Day_11/11_input.txt", "r")
content = f.read()
f.close()
prev = content.splitlines()

width = len(prev[0])
height = len(prev)

cur = prev.copy()

for i in range(height):
    prev[i] = list(prev[i])
    cur[i] = list(cur[i])

x = 0
y = 0



adjacent = 0




def check_adjacent(x, y, lst):
    empty = 0
    occupied = 0
    #top mid
    if y - 1 >= 0:
        if prev[y-1][x] == "#":
            occupied += 1
        elif prev[y-1][x] == "L":
            empty += 1
        #top left
        if x - 1 >= 0:
            if prev[y-1][x-1] == "#":
                occupied += 1
            elif prev[y-1][x-1] == "L":
                empty += 1
        #top right
        if x + 1 < width:
            if prev[y-1][x+1] == "#":
                occupied += 1
            elif prev[y-1][x+1] == "L":
                empty += 1
    #mid left
    if x - 1 >= 0:
        if prev[y][x-1] == "#":
            occupied += 1
        elif prev[y][x-1] == "L":
            empty += 1
    #mid right
    if x + 1 < width:
        if prev[y][x+1] == "#":
            occupied += 1
        elif prev[y][x+1] == "L":
            empty += 1
    #bot mid
    if y + 1 < height:
        if prev[y+1][x] == "#":
            occupied += 1
        elif prev[y+1][x] == "L":
            empty += 1
        #bot left
        if x - 1 >= 0:
            if prev[y+1][x-1] == "#":
                occupied += 1
            elif prev[y+1][x-1] == "L":
                empty += 1
        #bot right
        if x + 1 < width:
            if prev[y+1][x+1] == "#":
                occupied += 1
            elif prev[y+1][x+1] == "L":
                empty += 1

    return empty, occupied

def copylist(dest, src):
    for x in range(width):
        for y in range(height):
            dest[y][x] = src[y][x]

def printlist(lst):
    for y in range(height):
        print(lst[y])
    return

counter = 0
while True:
    for x in range(width):
        for y in range(height):
            empty, occupied = check_adjacent(x,y,prev)
            if prev[y][x] == "L" and occupied == 0:
                cur[y][x] = "#"
            elif prev[y][x] == "#" and occupied >= 4:
                cur[y][x] = "L"
    
    if prev == cur:
        break
    else:
        counter += 1
        copylist(prev, cur)
            
#printlist(cur)
print(counter)


counter = 0
for x in range(width):
    for y in range(height):
        if cur[y][x] == "#":
            counter += 1

print(counter)
