f = open('./2022/Day_06/input.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

for line in lines:
    window = 14
    for i in range(len(line)-window-1):
        if len(set(line[i:window+i])) == window:
            print(window+i)
            break
    