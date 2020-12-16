myList = open("C:/Users/mattr/Documents/Advent-Coding/Day_16/16_input.txt", "r").read().splitlines()

completedRules = {}
rules = {}
""" rules = {
    "rulename": [
        [min1, max1],
        [min2, max2],
        [x,x,x,x,x,x,x,x,x...], #valid columns in tickets
        column
    ]
} """

for item in myList:
    if item == "":
        break
    else:
        split = item.split(": ")
        minmax = [num.split("-") for num in split[1].split(" or ")]
        minmax[0] = [int(num) for num in minmax[0]]
        minmax[1] = [int(num) for num in minmax[1]]
        rules[split[0]] = minmax

myTicket = [int(val) for val in myList[22].split(",")]

def checkRule(ticket):
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

validTickets = []
error = 0
totalError = 0
for i in range(25,len(myList)):
    error = 0
    ticket = [int(val) for val in myList[i].split(",")]
    error += checkRule(ticket)
    totalError += error
    if not error:
        validTickets.append(ticket)

for rule in rules:
    name = rules[rule]
    min1 = rules[rule][0][0]
    min2 = rules[rule][1][0]
    max1 = rules[rule][0][1]
    max2 = rules[rule][1][1]
    rules[rule].append([])
    vallist = rules[rule][2]

    for i in range(0,len(myTicket)):
        for t in validTickets:
            valid = 1
            if not (t[i] in range(min1,max1+1) or t[i] in range(min2,max2+1)):
                valid = 0
                break
        vallist.append(valid)

def zeroOut(i, name):
    for rule in rules:
        if rule != name:
            rules[rule][2][i] = 0

def findNext():
    for rule in rules:
        if sum(rules[rule][2]) == 1:
            i = rules[rule][2].index(1)
            zeroOut(i, rule)
            rules[rule].append(i)
            #rules[rule][3] = i
            completedRules[rule] = rules.pop(rule)
            return 1
        
    return 0

for i in range(len(myTicket)):
    findNext()

answer = 1
for rule in completedRules:
    if rule.split(" ")[0] == "departure":
        answer *= myTicket[completedRules[rule][3]]

print(answer)

        



