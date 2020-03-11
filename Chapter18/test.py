from MyCard import Card
from MyDeck import Deck
from MyHand import Hand
from find_defining_class import *

card1 = Card(2, 11)
print(card1)
deck = Deck()
print(deck)
hand = Hand('new hand')
print(hand.cards)
print(hand.label)
deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print(hand)
print(find_defining_class(hand, 'shuffle'))


