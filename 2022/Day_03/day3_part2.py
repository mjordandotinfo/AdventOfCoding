f = open('input.txt', 'r')

lines = [line.strip() for line in f]

def priority(char):
    ichar = ord(char)
    if ichar >= 65 and ichar <= 90:
        pri = ichar - 38
    else:
        pri = ichar - 96

    return pri

def findDupe(str1, str2):
    chars = []
    dupes = []
    for c in str1:
        if not c in chars:
            chars.append(c)
    
    for c in str2:
        if c in chars and not c in dupes:
            dupes.append(c)

    return ''.join(dupes)

total = 0
for i in range(0, len(lines), 3):
    dupes = findDupe(lines[i], lines[i+1])
    dupe = findDupe(dupes, lines[i+2])
    pri = priority(dupe)
    total += pri
    
print(total)

f.close()