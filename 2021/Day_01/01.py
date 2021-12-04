mylist = open("C:/Users/mattr/Documents/Advent-Coding/2021/Day_01/01_input.txt", "r").read().splitlines()

prevDepth = mylist[0]
count = 0
for depth in mylist[1:]:
    #print(f"{prevDepth}, {depth}")
    if int(prevDepth) < int(depth):
        #print("count")
        count += 1
    prevDepth = depth

print(count)