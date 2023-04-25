from player import Player
from deck_of_cards import Deck_of_Cards


class Dealer():
    def __init__(self) -> None:
        self.name = "Dealer"
        self.hand = []
        self.hand_value = 0

    def calculate_hand_value(self):
        self.hand_value = 0
        for card in self.hand:
            self.hand_value += card.value
