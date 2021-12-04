
def read_data(data):
    D = {}

    for i in range(len(data)):
        if data[i] == "":
            break
        else:
            [num, rule] = data[i].split(": ")
            ors = rule.split(" | ") #[subrule, subrule]
            #print(test)
            for j in range(len(ors)):
                ors[j] = ors[j].split(" ")
                for k in range(len(ors[j])):
                    ors[j][k] = ors[j][k].strip("\"")
            #print(ors)
            D[num] = ors

    return D, data[i+1:]

def resolve(rules, resList):
    for rule in rules: #for index in rules
    #print(rule)
        for subrule in rules[rule]:
            #print(subrule)
            for i in range(len(subrule)):
                if subrule[i] in resList:
                    subrule[i] = rules[subrule[i]][0][0]

    resList = check_resolved(rules)
    return resList

def check_resolved(rules):
    resList = []
    for rule in rules:
        resolved = True
        for subrule in rules[rule]:
            if resolved:
                for i in subrule:
                    if i.isnumeric():
                        resolved = False
                        break
        if resolved:
            for subrule in rules[rule]:
                temp = ""
                for i in subrule:
                    temp += i
                subrule.clear()
                subrule.append(temp)
            resList.append(rule)

    return resList

def print_rules(rules):
    for rule in rules:
        print(rule, rules[rule])
    return

def main():
    #f = open("C:/Users/mattr/Documents/Advent-Coding/Day_19/19_input.txt", "r")
    f = open("C:/Users/mattr/Documents/Advent-Coding/Day_19/test.txt", "r")
    input = f.read().splitlines()
    rules, msgs = read_data(input)

    #print(rules)
    #print(msgs)
    resList = check_resolved(rules)
    
    print(resList)
    tempD = {}
    resList = resolve(rules, resList)
    #rules = resolve(rules, resList)
    # for rule in rules: #for index in rules
    #     #print(rule)
    #     for subrule in rules[rule]:
    #         #print(subrule)
    #         for i in range(len(subrule)):
    #             if subrule[i] in resList:
    #                 subrule[i] = rules[subrule[i]][0][0]
    #                 #print(rules[subrule[i]])
    #             #print(subrule[i])
        
    #     #if check_resolved()

    #resList = check_resolved(rules)
    print_rules(rules)
    print(resList)


    #rules = resolve(rules, resList)
    #resList = check_resolved(rules)
    #print_rules(rules)
    #print(resList)


    return 0
    # for rule in rules:
    #     resolved = True
    #     for subrule in rules[rule]:
    #         if resolved:
    #             for i in subrule:
    #                 if i.isnumeric():
    #                     resolved = False
    #                     break
    #     if resolved:
    #         resList.append(rule)

    

if __name__ == "__main__":
    main()

