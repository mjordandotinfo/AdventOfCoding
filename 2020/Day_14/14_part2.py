f = open("C:/Users/mattr/Documents/Advent-Coding/Day_14/test2.txt", "r")
myList = [x.split(" = ") for x in f.read().splitlines()]
f.close()

mask = ""

def mask2dec(mask):
    val1 = 0
    valX = []

    for i in range(len(mask)):
        if mask[i] == "1":
            val1 += 2 ** (35 - i)
        elif mask[i] == "X":
            valX.append(35 - i + 1)
    
    return val1, valX

def writeMem(addr, val, xmask):
    allMasks = []
    realMasks = []
    combos = 2**len(xmask)

    for i in range(0, combos):
        allMasks.append(bin(i).split("0b")[1])

    for i in range(0, combos):
        mask = allMasks[i]
        for pos in xmask:
            

    print(allMasks)

mask0 = -1
maskX = -1
total = 0
mem = {}

for data in myList:
    if data[0] == "mask":
        #mask = data[1]
        mask1, maskX = mask2dec(data[1])
        print(maskX)
    else:
        addr = int(data[0][4:].rstrip("]")) | mask1
        writeMem(addr, data[1], maskX)
        #data[1] = (int(data[1]) | mask1) & mask0
        #data[1] = int(data[1]) & mask0
        #print(data[1])
        #mem[int(data[0][4:].rstrip("]"))] = (int(data[1]) | mask1) & mask0

#for key in mem:
#    total += mem[key]

print(total)