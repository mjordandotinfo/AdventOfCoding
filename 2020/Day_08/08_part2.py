f = open("C:/Users/mattr/Documents/Advent-Coding/Day_08/08_input.txt", "r")
content = f.read()
f.close()

myList = content.splitlines()

checkList = [0] * len(myList)

acc = 0
i = 0

for swap in range(0, len(myList) - 1):
    print("testing index ", swap)
    checkList = [0] * len(myList)
    acc = 0
    original = myList[swap]
    if myList[swap].split(" ")[0] == "jmp":
        myList[swap] = "nop " + myList[swap].split(" ")[1]

    i = 0
    while True:
        if i >= len(myList):
            break

        cmd, val = myList[i].split(" ")
    
        if checkList[i]:
            #print("repeating ", i)
            break
        else:
            checkList[i] += 1

        #print(cmd, val)
        if cmd == "acc":
            if val[0] == "-":
                acc -= int(val.lstrip("-+"))
            else:
                acc += int(val.lstrip("-+"))
            i += 1
        elif cmd == "jmp":
            if val[0] == "-":
                i -= int(val.lstrip("-+"))
            else:
                i += int(val.lstrip("-+"))
        else:
            i += 1
    
    if i >= len(myList):
        break

    if all(item == 1 for item in checkList):
        break
    else:
        myList[swap] = original

print(acc)