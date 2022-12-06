f = open('./2022/Day_04/input.txt', 'r')
lines = [line.strip() for line in f]

#print(len(lines))
total = 0
for line in lines:
    [one, two] = line.split(",")
    one = [int(x) for x in one.split("-")]
    two = [int(x) for x in two.split("-")]

    one = [i for i in range(one[0], one[1]+1)]
    two = [i for i in range(two[0], two[1]+1)]

    for num in one:
        if num in two:
            total += 1
            break

print(total)



