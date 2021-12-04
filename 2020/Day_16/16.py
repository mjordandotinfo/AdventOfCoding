myList = open("C:/Users/mattr/Documents/Advent-Coding/Day_16/16_input.txt", "r").read().splitlines()

#print(myList)

rules = {}

#get rules
for item in myList:
    if item == "":
        break
    else:
        split = item.split(": ")
        minmax = [num.split("-") for num in split[1].split(" or ")]
        minmax[0] = [int(num) for num in minmax[0]]
        minmax[1] = [int(num) for num in minmax[1]]
        rules[split[0]] = minmax

#for rule in rules:
#    for subrule in rules[rule]:
#        subrule = [int(val) for val in subrule]

#my ticket
myTicket = [int(val) for val in myList[22].split(",")]

print(myTicket)

def checkRule(ticket):
    ticketValid = True
    error = 0
    for val in ticket:
        for rule in rules:
            min1 = rules[rule][0][0]
            min2 = rules[rule][1][0]
            max1 = rules[rule][0][1]
            max2 = rules[rule][1][1]
            if not (val in range(min1,max1+1) or val in range(min2,max2+1)):
                error = val
            else:
                error = 0
                break
        
        if error:
            return error
                
    return error

error = 0
for i in range(25,len(myList)):
    ticket = [int(val) for val in myList[i].split(",")]
    error += checkRule(ticket)

print(error)
        



