def l_parens(s):
    return [i for i in range(len(s)) if s[i] == "("]

def r_parens(s):
    return [i for i in range(len(s)) if s[i] == ")"]

def find_pair(s):
    left = list(reversed(l_parens(s)))
    right = r_parens(s)

    #the highest priority parens pair will always be the first index in a reverse list of left parens that is lower than the first right parens
    for i in range(len(left)):
        if left[i] < right[0]:
            return(left[i], right[0])

    return [-1,-1]

def spec_eval(s):
    splits = s.split()
    try:
        #check for addition
        add = splits.index("+")
        #pop off the expression
        exp = splits.pop(add-1) + splits.pop(add-1) + splits.pop(add-1)
    except ValueError:
        #multiplication
        add = 1
        #pop off the expression
        exp = splits.pop(0) + splits.pop(0) + splits.pop(0)

    sep = " "
    #if after popping there is still more math to do, go recursive
    if len(splits):
        #evaluate the expression and insert it back in
        splits.insert(add-1, str(eval(exp)))
        return spec_eval(sep.join(splits))
    else:
        #returns when no more math to do
        return eval(exp)

def main():
    f = open("C:/Users/mattr/Documents/Advent-Coding/Day_18/18_input.txt", "r")
    myList = f.read().splitlines()
    f.close()
    total = 0
    
    #for each input line
    for data in myList:
        #if there are parens, find them
        while data.find("(") > -1:
            #get the priority parens
            pair = find_pair(data)

            #evaluate parens using whatever weird rule
            val = spec_eval(data[pair[0]+1:pair[1]])

            #cut out the parens and insert the result
            dsplit = data.split(data[pair[0]:pair[1]+1])
            data = dsplit[0] + str(val) + dsplit[1]

        total += spec_eval(data)

    print(total)
    return 0

if __name__=="__main__":
    main()