# f = open('./2023/Day_01/test.txt', 'r')
f = open('./2023/Day_01/input.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

result = 0
for line in lines:
    nums = [c for c in line if c.isnumeric()]
    result += int(nums[0] + nums[-1])

print(result)

