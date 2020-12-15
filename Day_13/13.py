f = open("C:/Users/mattr/Documents/Advent-Coding/Day_13/13_input.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

ready = int(myList[0])
lines = [int(line) for line in myList[1].split(",") if line != "x"]

print(lines)

low_wait = -1
bus = -1
wait = -1

for line in lines:
    wait = line - (ready % line)
    departure = wait + ready
    if low_wait == -1 or wait < low_wait:
        low_wait = wait
        bus = line
        print(low_wait, bus)

print(low_wait*bus)