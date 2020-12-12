import copy

f = open("C:/Users/mattr/Documents/Advent-Coding/Day_11/11_input.txt", "r")
content = f.read()
f.close()
prev = content.splitlines()

width = len(prev[0])
height = len(prev)

for i in range(height):
    prev[i] = list(prev[i])

cur = copy.deepcopy(prev)


#pont = 0[y, x]
d1 = [-1,-1] #top left
d2 = [-1,0]  #top mid
d3 = [-1,1]  #top right
d4 = [0,-1]  #mid left
d5 = [0,1]   #mid right
d6 = [1,-1]  #bot left
d7 = [1,0]   #bot mid
d8 = [1,1]   #bot right

deltas = [d1,d2,d3,d4,d5,d6,d7,d8]

def printlist(lst):
    for y in range(height):
        print(lst[y])
    return

def check_adj(x,y):
    occupied = 0
    tmpDelta = [0, 0]
    for delta in deltas:
        tmpDelta[0] = delta[0]
        tmpDelta[1] = delta[1]
        while(not (x + tmpDelta[1] < 0 or y + tmpDelta[0] < 0 or x + tmpDelta[1] >= width or y + tmpDelta[0] >= height)):            
            if prev[y + tmpDelta[0]][x + tmpDelta[1]] == "#":
                occupied += 1
                break
            elif prev[y + tmpDelta[0]][x + tmpDelta[1]] == "L":
                break
            else:
                tmpDelta[0] += delta[0]
                tmpDelta[1] += delta[1]

    return occupied

counter = 0
#printlist(cur)
while True:
    for x in range(width):
        for y in range(height):
            if prev[y][x] == "L" and check_adj(x,y) == 0:
                cur[y][x] = "#"

            elif prev[y][x] == "#" and check_adj(x,y) >= 5:
                cur[y][x] = "L"
    
    if prev == cur:
        break
    else:
        #print()
        #printlist(cur)
        counter += 1
        prev = copy.deepcopy(cur)

print(counter)

counter = 0
for x in range(width):
    for y in range(height):
        if cur[y][x] == "#":
            counter += 1

print(counter)
