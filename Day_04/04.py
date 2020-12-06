import ctypes
import json

f = open("C:/Users/mattr/Documents/Advent-Coding/Day_04/04_input.txt", "r")
content = f.read()
f.close()

myList = content.splitlines()

tempDict = dict()
pairs = []
reqd = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
key = ""
val = ""
numValid = 0
valid = True

parsedList = []

for items in myList:
    if not (items == ""):
        pairs = items.split(" ", -1)
        
        for i in pairs:
            [key, val] = i.split(":")
            tempDict.update({key:val})

    else:
        parsedList.append(tempDict.copy())
        tempDict.clear()

parsedList.append(tempDict.copy())

for items in parsedList:
    valid = True
    for x in reqd:  
        if not (x in items):
            valid = False
    if valid:
        numValid += 1

print([numValid, len(parsedList)])
    
    


