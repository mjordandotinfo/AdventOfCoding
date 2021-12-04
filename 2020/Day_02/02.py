f = open("C:/Users/mattr/Documents/Advent-Coding/Day_02/02_input.txt", "r")
content = f.read()
myList = content.splitlines()

numValid = 0

for rule in myList:
    charCount = 0
    myMin = int(rule.split("-")[0])
    rule = rule.split("-")[1]
    myMax = int(rule.split(" ")[0])
    rule = rule.split(" ", 1)[1]
    myChar = rule.split(":")[0]
    rule = rule.split(" ")[1]
    
    for char in rule:
        if char == myChar:
            charCount += 1
    if (charCount >= myMin and charCount <= myMax):
        numValid += 1

print(numValid, len(myList))