f = open("C:/Users/mattr/Documents/Advent-Coding/Day_12/12_input.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

pos = [0,0]
waypoint = [10,1]

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
            x = waypoint[0]
            y = waypoint[1]

            tmp = waypoint[0]
            waypoint[0] = waypoint[1]
            waypoint[1] = tmp

            if x > 0 and y > 0:
                if ltr == "L":
                    waypoint[0] *= -1
                else:
                    waypoint[1] *= -1
            elif x < 0 and y > 0:
                if ltr == "L":
                    waypoint[0] *= -1
                else:
                    waypoint[1] *= -1
            elif x < 0 and y < 0:
                if ltr == "L":
                    waypoint[0] *= -1
                else:
                    waypoint[1] *= -1
            elif x > 0 and y < 0:
                if ltr == "L":
                    waypoint[0] *= -1
                else:
                    waypoint[1] *= -1

            

            val -= 90
    
    print(pos[0], pos[1], waypoint[0], waypoint[1])

print(pos)
print(abs(pos[0]) + abs(pos[1]))
