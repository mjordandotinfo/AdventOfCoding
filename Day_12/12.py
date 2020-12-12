f = open("C:/Users/mattr/Documents/Advent-Coding/Day_12/12_input.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

heading = {0: "N", 90: "E", 180: "S", 270: "W"}
myDir = 90
pos = [0,0]

def move(d,v):
    if d == "N":
        pos[1] += v
    elif d == "E":
        pos[0] += v
    elif d == "S":
        pos[1] -= v
    elif d == "W":
        pos[0] -= v

for cmd in myList:
    ltr = cmd[0]
    val = int(cmd[1:])
    
    if ltr == "L":
        myDir -= val
        if myDir < 0:
            myDir += 360
        myDir = myDir % 360
    elif ltr == "R":
        myDir += val
        myDir = myDir % 360
    elif ltr == "F":
        move(heading[myDir],val)
    else:
        move(ltr,val)

print(pos)
print(abs(pos[0]) + abs(pos[1]))
