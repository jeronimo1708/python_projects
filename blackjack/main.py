import sys

from card import Card
from deck_of_cards import Deck_of_Cards
from table import Table
from dealer import Dealer
from player import Player
from chips import Chips

num_of_players = ""
player_list = []


def get_number_of_players(num_of_players, player_list):
    is_int = False
    while not is_int:
        try:
            num = int(input("How many players are playing?\n"))
            is_int = True
        except ValueError:
            print("You have not entered a valid number. Please try again!")
    return num


def create_players():
    name = ""
    name = input("Enter Player Name: \n")
    chips = int(input("How many chips do you want to buy in with? (Default is 100)"))
    player = Player(name, Chips(chips))
    player_list.append(player)


def show_cards(hand):
    for card in hand:
        print(card)


def show_one_card(hand):
    for card in hand:
        print(card)
        break


# To be used when natural check is implemented
def natural_check(hand):
    total = 0
    for card in hand:
        total += card.value
    if total == 21:
        return True
    else:
        return False


def hit(person):
    person.hand.extend(deck.deal(1))
    person.calculate_hand_value()
    print(f"{person.name} Hand -> {person.hand}")
    print(f"{person.name} Hand Value -> {person.hand_value}")


def stand():
    pass


def win_lose_check(dealer, player):
    if dealer.hand_value > player.hand_value:
        print("Dealer Wins")
    else:
        print(f"{player.name} wins")
        table.won_players.append(player)
        table.remove(player)


def over_twenty_one_check(player):
    if player.hand_value > 21:
        print(
            f"Player {player.name} has {player.hand} and its value is {player.hand_value} which is over 21!"
        )
        print(f"Player {player.name} lost! Wait for next round")
        return True
    else:
        return False


game_on = True
while game_on:
    dealer = Dealer()
    create_players()
    table = Table(player_list)
    new_game = True
    while new_game:
        # Deal cards to the dealer and all players in the current game.
        deck = Deck_of_Cards()
        deck.shuffle()
        dealer.hand.extend(deck.deal(2))
        dealer.calculate_hand_value()
        for player in player_list:
            player.hand.extend(deck.deal(2))

        # If dealer has a natural check'
        # Need to implement natural system later.

        # dealer_natural_check = natural_check(dealer.hand)
        # if dealer_natural_check:
        #     for player in player_list:
        #         if not natural_check(player.hand):

        # Show all player cards
        for player in table.players:
            print(f"{player.name} has {player.hand}")

        # Show first dealer card
        print(f"dealer has {dealer.hand[0]}")

        # take turns

        for player in table.players:
            print(f"{player.name}'s turn")
            player.calculate_hand_value()
            print(f"Hand Value {player.hand_value}")
            hit_or_stand = ""
            while hit_or_stand not in ("h", "s"):
                hit_or_stand = input("Do you want to hit or stand?(h/s)").lower()
            if hit_or_stand == "h":
                keep_hitting = True
                while keep_hitting:
                    hit(player)
                    if over_twenty_one_check(player):
                        standby_player = table.players.remove(player)
                        table.lost_players.append(standby_player)
                        break

                    hit_again = ""
                    while hit_again not in ("y", "n"):
                        hit_again = input("Do you want to keep hitting?(y/n)").lower()
                        if hit_again == "n":
                            keep_hitting = False

            else:
                stand()

        # Dealers Play
        if table.players:
            print(f"Dealer has {dealer.hand}")
            print(f"Dealer hand Value is {dealer.hand_value}")
            while dealer.hand_value < 17:
                hit(dealer)
                over_twenty_one_check(dealer)
            for remaining_players in table.players:
                win_lose_check(dealer, remaining_players)

        break
    break
