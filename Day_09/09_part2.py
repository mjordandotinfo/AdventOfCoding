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

""" for i in range(pre_len, len(myList) - 1):
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
        break """


num = 88311122
temp_list = []



def findWeakness(myList1):
    for i in range(len(myList1)):
        n1 = myList1[i]
        temp_list.append(myList1[i])
        for j in range(i + 1, len(myList1) - 1):
            n1 += myList1[j]
            temp_list.append(myList1[j])
            if n1 > num:
                break
            elif n1 == num:
                print(temp_list)
                temp_list.sort()
                print(temp_list)

                tmp = 0
                for a in temp_list:
                    tmp += a

                print(tmp)

                return(temp_list[0] + temp_list[len(temp_list)-1])
        temp_list.clear()
    
#num = 127
print(findWeakness(myList))

#11103535

#print(num)

