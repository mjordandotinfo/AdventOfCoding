f = open("C:/Users/mattr/Documents/Advent-Coding/Day_09/09_input.txt", "r")
content = f.read()
f.close()

test = [35,
20,
15,
25,
47,
40,
62,
55,
65,
95,
102,
117,
150,
182,
127,
219,
299,
277,
309,
576]

myList = content.splitlines()

for i in range(len(myList)):
    myList[i] = int(myList[i])

pre_len = 25
num = 0
n1 = 0
n2 = 0
match = False

for i in range(pre_len, len(myList) - 1):
    num = myList[i]
    match = False
    for j in range(i - pre_len, i - 1):
        n1 = myList[j]
        for k in range(j + 1, i):
            n2 = myList[k]
            if n1 + n2 == num and n1 != n2:
                match = True
                break
        if match:
            break
    if not match:
        break
        

print(num)

