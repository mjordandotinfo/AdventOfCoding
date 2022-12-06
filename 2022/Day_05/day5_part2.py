f = open('./2022/Day_05/input.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

def getStacks(lines):
    n = int((len(lines[0]) + 1) / 4)
    stacks = [[] for i in range(n)]
    for line in lines:
        if line:
            for i in range(n):
                char = line[i*4 + 2 - 1]
                if char.isalpha():
                    stacks[i].insert(0,char)
        else:
            break
    
    return stacks

def getInstructions(lines, stacks):
    for line in lines:
        [amt, src, dst] = [int(x) for x in line.split() if x.isnumeric()]
        crates = []
        for _ in range(amt):
            crates.insert(0, stacks[src-1].pop())
        
        stacks[dst-1] += crates

    return ''.join([x[len(x)-1] for x in stacks])
    
stacks = getStacks(lines)
maxStack = max([len(x) for x in stacks])
code = getInstructions(lines[maxStack+2:], stacks)

print(code)
