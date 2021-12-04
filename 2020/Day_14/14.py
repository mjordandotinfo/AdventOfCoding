f = open("C:/Users/mattr/Documents/Advent-Coding/Day_14/14_input.txt", "r")
myList = [x.split(" = ") for x in f.read().splitlines()]
f.close()

mask = ""

def mask2dec(mask):
    val1 = 0
    val0 = 0

    for i in range(len(mask)):
        if mask[i] == "1":
            val1 += 2 ** (35 - i)
        
        if mask[i] != "0":
            val0 += 2 ** (35 - i)
    
    return val1, val0

mask0 = -1
mask1 = -1
total = 0
mem = {}

for data in myList:
    if data[0] == "mask":
        mask1, mask0 = mask2dec(data[1])
    else:
        mem[int(data[0][4:].rstrip("]"))] = (int(data[1]) | mask1) & mask0

for key in mem:
    total += mem[key]

print(total)