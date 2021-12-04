f = open("C:/Users/mattr/Documents/Advent-Coding/Day_13/test2.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

ready = int(myList[0])
lines = [int(line) for line in myList[1].split(",") if line != "x"]
deltas = {}
delta = 0
max_delta = 0




for line in myList[1].split(","):
    if not bool(deltas):
        deltas[int(line)] = delta
        delta += 1
    elif line != "x":
        deltas[int(line)] = delta
        max_delta += delta
        delta = 1
    else:
        delta += 1

print(lines, deltas, max_delta)

ready = 0
#ready = 100000000000000
t = lines[0] - ready % lines[0] + ready

print(t)

def check_next(index,time):
    line = lines[index]
    check = time + deltas[lines[index]]
    if (check) % line == 0:
        if index == len(lines) - 1:
            return 0
        else:
            #print("index: ", index, time)
            return line * check_next(index + 1, check)
    else:
        return 1

step = lines[0]  
while True:
    check = check_next(1,t)
    if check == 0:
        break
    elif check != 1:
        step += step * check
    
    t += step

print(t)



#updated target
    #if next bus mod taget plus bus delta == 0 check next bus
    #else update target


# low_wait = -1
# bus = -1
# wait = -1

# t = 0



# for line in lines:
#     wait = line - (ready % line)
#     departure = wait + ready
#     if low_wait == -1 or wait < low_wait:
#         low_wait = wait
#         bus = line
#         print(low_wait, bus)

# print(low_wait*bus)