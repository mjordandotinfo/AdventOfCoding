f = open('./2022/Day_04/input.txt', 'r')
lines = [line.strip() for line in f]

#print(len(lines))
total = 0
for line in lines:
    [one, two] = line.split(",")
    one = [int(x) for x in one.split("-")]
    two = [int(x) for x in two.split("-")]

    if not (one[0] <= two[0]) + (one[1] >= two[1]) == 1:
        total += 1
    elif not (two[0] <= one[0]) + (two[1] >= one[1]) == 1:
        total += 1 

print(total)



