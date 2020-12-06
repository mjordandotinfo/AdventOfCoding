f = open("C:/Users/mattr/Documents/Advent-Coding/Day_05/05_input.txt", "r")
content = f.read()
myList = content.splitlines()

#print(myList[0][:7])

def alpha_to_bin(str1, zero, one):
    binstr = ""
    for c in str1:
        if c == zero:
            binstr += "0"
        elif c == one:
            binstr += "1"

    binvalue = int(binstr, 2)

    return [binstr, binvalue]

def calc_seat_ID(row, col):
    return (row * 8 + col)

highSeatID = 0
listSeatID = []

for ticket in myList:
    row = alpha_to_bin(ticket[:7], "F", "B")
    col = alpha_to_bin(ticket[7:], "L", "R")
    seatID = calc_seat_ID(row[1], col[1])
    
    if seatID > highSeatID:
        highSeatID = seatID

    listSeatID.append(seatID)

listSeatID.sort()

mySeat = 0

for i in range(len(listSeatID)-2):
    curID = listSeatID[i]
    nextID = listSeatID[i+1]

    if curID + 2 == nextID:
        mySeat = curID + 1
        break

print(mySeat)
