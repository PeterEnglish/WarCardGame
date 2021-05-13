import player
import deck

player_one = player.Player("One")
player_two = player.Player("Two")


new_deck = deck.Deck()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


game_on = True
round_num = 0
while game_on:
    round_num += 1
    print(f"Rounds {round_num}")


    if len(player_one.all_cards) == 0:
        print('Player One out of Cards! Player Two wins!')
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print('Player Two out of Cards! Player One wins!')
        game_on = False
        break


    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    while at_war:
        if(player_one_cards[-1].value >player_two_cards[-1].value):
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif(player_one_cards[-1].value <player_two_cards[-1].value):
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False

        else:
            print('WAR!')
            if(len(player_one.all_cards)< 3):
                print('Player One Unable to declare war!')
                print('Player Two Wins!')
                game_on = False
                break

            if(len(player_two.all_cards)< 3):
                print('Player Two Unable to declare war!')
                print('Player One Wins!')
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())








