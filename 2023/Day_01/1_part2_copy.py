# f = open('./2023/Day_01/test_2.txt', 'r')
f = open('input.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
test_string = 'eightwothree'

result = 0
for line in lines:
    data = line
    data = data.replace('zero', 'zero0zero')
    data = data.replace('one', 'one1one')
    data = data.replace('two', 'two2two')
    data = data.replace('three', 'three3three')
    data = data.replace('four', 'four4four')
    data = data.replace('five', 'five5five')
    data = data.replace('six', 'six6six')
    data = data.replace('seven', 'seven7seven')
    data = data.replace('eight', 'eight8eight')
    data = data.replace('nine', 'nine9nine')
    # print(f'{data=}')
    indices = [(i, str(c)) for i, c in enumerate(data) if c.isnumeric()]
    # print(f'{indices=}')
    result += int(indices[0][1] + indices[-1][1])

# result = 0
# for line in lines:
#     print(f'{line=}')

#     # for each written number, find all duplicates of it in the string
#     indices = []
#     for num_int, num_str in enumerate(numbers):
#         # print(f'{num_str=}')
#         i = -1
#         while line.find(num_str,i+1) != -1:
#             # print(f'{num_str=} - {i=} - {line.find(num_str,i+1)=}')
#             i = line.find(num_str,i+1)
#             indices.append((i, str(num_int)))
    
#     # find all numeric numbers and sort
#     indices = [(i, str(c)) for i, c in enumerate(line) if c.isnumeric()]
#     indices.sort()

#     # add the front and back together
#     result += int(indices[0][1] + indices[-1][1])
#     print(f'{indices=} - {result=}')

print(result)

