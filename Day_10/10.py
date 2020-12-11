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

print(len(myList))

for i in range(1, len(myList)):
    diff = myList[i] - myList[i - 1]
    if diff == 1:
        jolt_1 += 1
    elif diff == 3:
        jolt_3 += 1
    elif diff > 3:
        print("uh oh")
        print(i, myList[i], myList[i+1])
        break
    else:
        print("wtf", i)

jolt_3 += 1

print(myList)
print(jolt_1 * jolt_3)