def getSum(sumList):
    sum = 0
    for item in sumList:
        sum += item

    return sum

mylist = open("C:/Users/mattr/Documents/Advent-Coding/2021/Day_01/01_input.txt", "r").read().splitlines()
mylist = [int(x) for x in mylist]

prevWindow = list()
window = list()
prevWindow.append(mylist[0])
prevWindow.append(mylist[1])
prevWindow.append(mylist[2])
window.append(mylist[1])
window.append(mylist[2])
count = 0
for depth in mylist[3:]:
    #print(f"{prevDepth}, {depth}")
    window.append(depth)
    if getSum(prevWindow) < getSum(window):
        #print("count")
        count += 1
    prevWindow.pop(0)
    prevWindow.append(depth)
    window.pop(0)

print(count)

