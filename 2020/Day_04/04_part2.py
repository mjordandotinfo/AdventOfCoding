import ctypes
import json

f = open("C:/Users/mattr/Documents/Advent-Coding/Day_04/04_input.txt", "r")
content = f.read()
f.close()

myList = content.splitlines()

tempDict = dict()
pairs = []
reqd = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
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

    for key in reqd: 
        val = items.get(key, "none") 
        if not (key in items):
            valid = False
        elif key == "byr":
            if val.isdigit():
                if len(val) != 4 or (int(val) < 1920 or int(val) > 2002):
                    valid = False
            else:
                valid = False
        elif key == "iyr":
            if val.isdigit():
                if len(val) != 4 or (int(val) < 2010 or int(val) > 2020):
                    valid = False
            else:
                valid = False
        elif key == "eyr":
            if val.isdigit():
                if len(val) != 4 or (int(val) < 2020 or int(val) > 2030):
                    valid = False
            else:
                valid = False
        elif key == "hgt":
            if val.endswith("cm") or val.endswith("in"):
                if val.endswith("cm") and (int(val[:len(val) - 2]) < 150 or int(val[:len(val) - 2]) > 193):
                    valid = False
                elif val.endswith("in") and (int(val[:len(val) - 2]) < 59 or int(val[:len(val) - 2]) > 76):
                    valid = False
            else:
                    valid = False
        elif key == "hcl":
            if len(val.lstrip("#")) != 6 or val.rstrip("0123456789abcdef") != "#":
                valid = False
        elif key == "ecl":
            if not (val in eyes):
                valid = False
        elif key == "pid":
            if (not val.isdigit()) or (not (len(val) == 9)):
                valid = False

    if valid:
        numValid += 1

print([numValid, len(parsedList)])
    
    


