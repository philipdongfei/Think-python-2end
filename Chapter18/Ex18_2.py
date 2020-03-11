#from MyDeck import Deck
#from MyHand import Hand
from Card import *

def main():
    deck = Deck()
    deck.deal_hands(4, 13)
    print(deck)

if __name__ == '__main__':
    main()

