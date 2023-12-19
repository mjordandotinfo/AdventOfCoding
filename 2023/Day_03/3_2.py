import re

f = open('input.txt', 'r')
# f = open('test.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()
lines.append("") # append a couple extra blank rows to make the logic work
lines.insert(0,"")

# initalize numbers window
i = 0
numbers = dict()

# more initialization
total = 0

# overlap checks for adjacency of symbols and numbers
def overlap(symbol_window, number_iter) -> list:
    # numbers['top'] = re.finditer('[0-9]+', lines[i-1])
    gears = []
    for num in number_iter:
        num_window = set(range(num.start(),num.end()))
        if not set(symbol_window).isdisjoint(num_window):
            # print(f'Gear: {num.group()}')
            gears.append(int(num.group()))

    return gears

# iterate over file
while i < len(lines)-1:
    # for every symbol
    for symbol in re.finditer('[^0-9,.]', lines[i]):
        # init symbol window
        symbol_top = set(range(symbol.start()-1, symbol.start()+2))
        symbol_mid = set([symbol.start()-1,symbol.start()+1])
        symbol_bot = set(range(symbol.start()-1, symbol.start()+2))
        gears = []

        # check for top overlap
        gears += overlap(symbol_top, re.finditer('[0-9]+', lines[i-1]))

        # check for mid overlap
        gears += overlap(symbol_mid, re.finditer('[0-9]+', lines[i]))
        
        # check for bottom overlap
        gears += overlap(symbol_bot, re.finditer('[0-9]+', lines[i+1]))

        # calc gear ratio
        if len(gears) == 2:
            total += gears[0] * gears[1]

    i += 1

print(total)
