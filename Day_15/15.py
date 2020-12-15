input = [7,12,1,0,16,2]
spoken = {} #number: [prev1, prev2]

for i in range(len(input)):
    spoken[input[i]] = [i+1, -1]

print(spoken)

speak = input[-1]
for i in range(len(spoken) + 1,30000001):
    prev = speak
    if spoken[prev][1] == -1:
        speak = 0
    else:
        speak = spoken[prev][0] - spoken[prev][1]

    if speak in spoken:
        spoken[speak][1] = spoken[speak][0]
        spoken[speak][0] = i 
    else:
        spoken[speak] = [i, -1]

print(speak)