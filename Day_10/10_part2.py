f = open("C:/Users/mattr/Documents/Advent-Coding/Day_10/10_input.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

for i in range(len(myList)):
    myList[i] = int(myList[i])

myList.append(0)
myList.sort()
myList.append(myList[len(myList)-1] + 3)

streak = 1
total = 1
for i in range(1, len(myList)):
    diff = myList[i] - myList[i - 1]
    if diff == 1:
        streak += 1
    elif diff == 3:
        streak = streak - 2
        if streak >= 1:
            n = (2*streak**3 - 9*streak**2 + 25*streak - 6)/6
            total = total * n
        streak = 1

print(total)