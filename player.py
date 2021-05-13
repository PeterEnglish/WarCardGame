import card

my_card = card.Card("Spades","Five")


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'



new_player = Player('Jose')

print(new_player)

new_player.add_cards([my_card, my_card, my_card])

print(new_player)

new_player.remove_one()

print(new_player)