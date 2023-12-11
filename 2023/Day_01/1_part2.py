f = open('./2023/Day_01/test_2.txt', 'r')
# f = open('./2023/Day_01/input.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
test_string = 'eightwothree'

result = 0
for line in lines:
    print(f'{line=}')

    # for each written number, find all duplicates of it in the string
    indices = []
    for num_int, num_str in enumerate(numbers):
        # print(f'{num_str=}')
        i = -1
        while line.find(num_str,i+1) != -1:
            # print(f'{num_str=} - {i=} - {line.find(num_str,i+1)=}')
            i = line.find(num_str,i+1)
            indices.append((i, str(num_int)))
    
    # find all numeric numbers and sort
    indices += [(i, str(c)) for i, c in enumerate(line) if c.isnumeric()]
    indices.sort()

    # add the front and back together
    result += int(indices[0][1] + indices[-1][1])
    print(f'{indices=} - {result=}')

print(result)

