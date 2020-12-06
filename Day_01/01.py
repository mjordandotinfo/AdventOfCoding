f = open("C:/Users/mattr/Documents/Advent-Coding/01_input.txt", "r")
content = f.read()
mylist = content.splitlines()

for i in range(len(mylist) - 1):
    for j in range(i + 1, len(mylist)):
        sum_values = int(mylist[i]) + int(mylist[j])
        if int(mylist[i]) + int(mylist[j]) == 2020:
            print(int(mylist[i]) * int(mylist[j]))
            break 

