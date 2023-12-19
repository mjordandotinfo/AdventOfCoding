import re

f = open('input.txt', 'r')
# f = open('test.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()
lines.append("") # append a couple extra blank rows to make the logic work
lines.append("")

# initalize symbol window
i = 0
symbols = dict()
symbols['top'] = set()
symbols['mid'] = {c.start() for c in re.finditer('[^0-9,.]', lines[0])}
symbols['bot'] = {c.start() for c in re.finditer('[^0-9,.]', lines[1])}

# more initialization
total = 0
numbers = dict()

# iterate over file
for i in range(len(lines)-2):
    # build number window
    for num in re.finditer('[0-9]+', lines[i]):
        numbers['top'] = set(range(num.start()-1,num.end()+1))
        numbers['mid'] = set([num.start()-1,num.end()])
        numbers['bot'] = set(range(num.start()-1,num.end()+1))

        # check for overlap of windows
        for key, val in symbols.items():
            if not set(numbers[key]).isdisjoint(symbols[key]):
                # print(num.group(), key)
                total += int(num.group())
                break

    # move symbol window
    i += 1
    symbols['top'] = symbols['mid']
    symbols['mid'] = symbols['bot']
    symbols['bot'] = {c.start() for c in re.finditer('[^0-9,.]', lines[i+1])}

print(total)
