def l_parens(s):
    return [i for i in range(len(s)) if s[i] == "("]

def r_parens(s):
    return [i for i in range(len(s)) if s[i] == ")"]

def find_pair(s):
    left = list(reversed(l_parens(s)))
    right = r_parens(s)

    for i in range(len(left)):
        if left[i] < right[0]:
            return(left[i], right[0])

    return [-1,-1]

def spec_eval(s):
    splits = s.split()
    exp = splits.pop(0) + splits.pop(0) + splits.pop(0)
    sep = " "
    if len(splits):
        return spec_eval(str(eval(exp)) + " " + sep.join(splits))
    else:
        return eval(exp)

def main():
    f = open("C:/Users/mattr/Documents/Advent-Coding/Day_18/18_input.txt", "r")
    myList = f.read().splitlines()
    f.close()
    total = 0
    
    for data in myList:
        while data.find("(") > -1:
            pair = find_pair(data)
            val = spec_eval(data[pair[0]+1:pair[1]])
            dsplit = data.split(data[pair[0]:pair[1]+1])
            data = dsplit[0] + str(val) + dsplit[1]
            #print(data)

        total += spec_eval(data)

    print(total)
    return 0

if __name__=="__main__":
    main()