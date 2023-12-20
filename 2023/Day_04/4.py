f = open('input.txt', 'r')
# f = open('test.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

total = 0
# For each card
for line in lines:
    # split off the winning numbers and numbers you have
    numbers = [side.split() for side in line.split(':')[1].split('|')]

    # find matches
    points = len(set(numbers[0]).intersection(set(numbers[1])))
    if points > 0:
        points = pow(2, points - 1)

    total += points

print(total)