from dataclasses import dataclass

f = open('input.txt', 'r')
# f = open('test.txt', 'r')
lines = [line.strip('\n') for line in f]
f.close()

@dataclass
class Card:
    card_num: int
    winners: list[int]
    numbers: list[int]
    score: int
    copies: int

    def score_card(self):
        points = len(set(self.winners).intersection(set(self.numbers)))
        # if points > 0:
        #     points = pow(2, points - 1)

        return points
    
    def __init__(self, line: str):
        card, numbers = line.split(':')
        self.card_num = int(card.split()[1])
        self.winners, self.numbers = [side.split() for side in numbers.split('|')]
        self.score = self.score_card()
        self.copies = 1

total = 0

# track copies for all cards
copies = {i: 0 for i in range(0+1,len(lines)+1)}

total = 0
for i, line in enumerate(lines):
    card = Card(line) # you never need to look back for the score of a card, so make it once and get rid of it
    copies[card.card_num] += 1 # get one original copy

    # add copies for each card below current card based on current card score
    for copy in range(card.card_num+1, card.card_num+card.score+1):
        copies[copy] += copies[card.card_num]

print(sum(copies.values())) 
