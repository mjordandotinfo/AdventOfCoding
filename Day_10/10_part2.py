f = open("C:/Users/mattr/Documents/Advent-Coding/Day_10/10_input.txt", "r")
content = f.read()
f.close()
myList = content.splitlines()

for i in range(len(myList)):
    myList[i] = int(myList[i])

jolt_1 = 0
jolt_3 = 0

myList.append(0)
myList.sort()
myList.append(myList[len(myList)-1] + 3)

print(len(myList))

print(myList)

streak = 1
total = 1
for i in range(1, len(myList)):
    diff = myList[i] - myList[i - 1]
    if diff == 1:
        jolt_1 += 1
        streak += 1
    elif diff == 2:
        print("-2-")
    elif diff == 3:
        jolt_3 += 1
        
        streak = streak - 2
        if streak >= 1:
            print("streak of ", streak, " ended at ", i - 1)
            n = (2*streak**3 - 9*streak**2 + 25*streak - 6)/6
            print(n)
            total = total * n
        streak = 1
    elif diff > 3:
        print("uh oh")
        print(i, myList[i], myList[i+1])
        break
    else:
        print("wtf", i)

jolt_3 += 1


print(jolt_1, jolt_3)
print(total)