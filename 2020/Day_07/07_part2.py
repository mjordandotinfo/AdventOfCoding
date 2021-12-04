f = open("C:/Users/mattr/Documents/Advent-Coding/Day_07/07_input.txt", "r")
content = f.read()
f.close()

mybag = ["shiny gold"]
#nextBag = ['dotted indigo', 'light coral', 'bright orange', 'clear gold']

myList = content.splitlines()

#print(myList)

def getParentBags(childBags):
    parentBags = []
    
    
    if not childBags:
        #childBags is empty
        return []
    else:
        #childbags NOT empty
        for child in childBags:
            for bags in myList:
                #bagcheck = bags.split(" contain ")[1].find(child)
                if bags.split(" contain ")[1].find(child) != -1:
                    parentBags.append(bags.split(" contain ")[0].split(" bags")[0])

        childBags.extend(getParentBags(parentBags))
        return childBags

def getChildBags(parentBags):
    numchildren = 0
    for parent in parentBags:
        for bags in myList:
            if bags.split(" contain ")[0].find(parent) != -1:
                childbags = bags.split(" contain ")[1].split(",")
                for bag in childbags:
                    if bag == "no other bags.":
                        return 0
                    else:
                        mybag = bag.lstrip()
                        num = int(mybag.split(" ")[0])
                        style = mybag.split(" ")[1] + " " + mybag.split(" ")[2]
                        numchildren += num + num*getChildBags([style])
                        #print(numchildren)
    
    return numchildren

childBags = getChildBags(mybag)
print(childBags)
# parentBags = getParentBags(mybag)
# print(parentBags)
# print(len(parentBags))
# parentBags = list(dict.fromkeys(parentBags))
# print(parentBags)
# print(len(parentBags))
