f = open('./2022/Day_06/input.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

for line in lines:
    start = 0
    end = 4
    for i in range(len(line)-3):
        if len(set(line[start+i:end+i])) == 4:
            print(end+i)
            break
    