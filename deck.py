import card
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight","Nine", "Ten", "Jack", "Queen", "King", "Ace" }

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Create the card object
                created_card = card.Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    
  


new_deck = Deck()


first_card = new_deck.all_cards[0]
print(first_card)

bottom_card = new_deck.all_cards[-1]
print(bottom_card)

new_deck.shuffle()

print(new_deck.all_cards[-1])

my_card = new_deck.deal_one()
print(my_card)

print(len(new_deck.all_cards))


