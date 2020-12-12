f = open("C:/Users/mattr/Documents/Advent-Coding/Day_12/12_input.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

heading = {0: "N", 90: "E", 180: "S", 270: "W"}
myDir = 90
pos = [0,0]
waypoint = [10,1]

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
    
    if ltr == "N":
        waypoint[1] += val
    elif ltr == "E":
        waypoint[0] += val
    elif ltr == "S":
        waypoint[1] -= val
    elif ltr == "W":
        waypoint[0] -= val
    elif ltr == "F":
        pos[0] += waypoint[0] * val
        pos[1] += waypoint[1] * val
    else:
        while val > 0:
            if waypoint[0] > 0 and waypoint[1] > 0:
                if ltr == "L":
                    waypoint[1] *= -1
                else:
                    waypoint[0] *= -1
            elif waypoint[0] < 0 and waypoint[1] > 0:
                if ltr == "L":
                    waypoint[1] *= -1
                else:
                    waypoint[0] *= -1
            elif waypoint[0] < 0 and waypoint[1] < 0:
                if ltr == "L":
                    waypoint[1] *= -1
                else:
                    waypoint[0] *= -1
            elif waypoint[0] > 0 and waypoint[1] < 0:
                if ltr == "L":
                    waypoint[1] *= -1
                else:
                    waypoint[0] *= -1

            tmp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = tmp

            val -= 90

print(pos)
print(abs(pos[0]) + abs(pos[1]))
