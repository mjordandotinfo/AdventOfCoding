f = open("C:/Users/mattr/Documents/Advent-Coding/Day_08/08_input.txt", "r")
content = f.read()
f.close()

myList = content.splitlines()

checkList = [0] * len(myList)

acc = 0
i = 0
while True:
    cmd, val = myList[i].split(" ")
    
    if checkList[i]:
        print("repeating ", i)
        break
    else:
        checkList[i] += 1

    print(cmd, val)
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

print(acc)