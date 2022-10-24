import random

cards = []
suits = ['spades', 'clubs', 'hearts', 'diamond']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
for suit in suits:
    for rank in ranks:
        cards.append((suit, rank))


def shuffle():
    random.shuffle(cards)


def deal(num):
    cards_dealt = []
    for i in range(num):
        cards_dealt.append(cards.pop())
    return cards_dealt


shuffle()
print(deal(2))
