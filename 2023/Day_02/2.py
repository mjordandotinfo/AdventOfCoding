f = open('input.txt', 'r')
# f = open('test.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

bag = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0
for i, line in enumerate(lines):
    works = True
    # game = i + 1
    game = line.split(':')[1].split(';')
    # print(game)
    for round in game:
        # print(round.strip())
        for draw in round.strip().split(','):
            color = draw.strip().split()
            if bag[color[1]] < int(color[0]):
                # print(f'NOPE {i+1=} {round=}')
                works = False

    if works:
        total += i+1

print(total)
    

    #rounds = [[strip_round.strip() for strip_round in round.strip().split(',')] for round in line.split(':')[1].split(';')]
    # print(rounds)
    # print(line.split(':')[1].split(';'))

