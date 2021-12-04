f = open("C:/Users/mattr/Documents/Advent-Coding/Day_02/02_input.txt", "r")
content = f.read()
myList = content.splitlines()

numValid = 0

for rule in myList:
    charCount = 0
    frontChar = int(rule.split("-")[0]) - 1
    rule = rule.split("-")[1]
    backChar = int(rule.split(" ")[0]) - 1
    rule = rule.split(" ", 1)[1]
    myChar = rule.split(":")[0]
    rule = rule.split(" ")[1]
    
    if (rule[frontChar] == myChar or rule[backChar] == myChar) and rule[frontChar] != rule[backChar]:
        numValid += 1

print(numValid, len(myList))

