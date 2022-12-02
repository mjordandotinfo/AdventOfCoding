f = open("input.txt", "r")
#f = open("./Day_02/test.txt", "r")

pts = {
    'A': 1,
    'B': 2,
    'C': 3
}

rps = {
    'A': 'C', # Rock    (X)  beats scissor (C)
    'B': 'A', # Paper   (Y)  beats rock    (A)
    'C': 'B', # Scissor (Z)  beats paper   (B)
}



def choosePlay(opp, player):
    if player == 'Z': #win
        for key, val in rps.items():
            if opp == val:
                return key

    decrypt = {
        'X': rps[opp],    #lose
        'Y': opp, #draw
    }

    return decrypt[player]

total = 0
for line in f:
    [opp, player] = line.split(" ")
    player = choosePlay(opp, player[0])
    round = 3 #draw
    if rps[player] == opp: #win
        round = 6
    elif rps[opp] == player: #lose
        round = 0 
    total += round + pts[player]
    
    
print(total)

f.close()