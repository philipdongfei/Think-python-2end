from Card import Card, Deck, Hand
from find_defining_class import *

card1 = Card(2, 11)
print(card1)
deck = Deck()
deck.shuffle()
print(deck)
print("#"*20)
deck.sort()
print(deck)

'''

hand = Hand('new hand')
print(hand.cards)
print(hand.label)
deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)
print(find_defining_class(hand, 'shuffle'))
'''


