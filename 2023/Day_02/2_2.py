f = open('input.txt', 'r')
# f = open('test.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

power = 0
for i, line in enumerate(lines):
    max = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    game = line.split(':')[1].split(';')
    for round in game:
        for draw in round.strip().split(','):
            color = draw.strip().split()
            if max[color[1]] < int(color[0]):
                max[color[1]] = int(color[0])

    power += max['red'] * max['green'] * max['blue']

print(power)

