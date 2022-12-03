f = open('input.txt', 'r')

lines = [line.strip() for line in f]

def priority(char):
    ichar = ord(char)
    if ichar >= 65 and ichar <= 90:
        pri = ichar - 38
    else:
        pri = ichar - 96

    return pri

total = 0
for line in lines:
    front = []
    l = len(line)
    for i in range(l):
        if i < l/2:
            if not line[i] in front:
                front.append(line[i])
        else:
            if line[i] in front:
                dupe = line[i]
                pri = priority(dupe)
                break

    total += pri
    #print(dupe, pri)
    
print(total)

f.close()