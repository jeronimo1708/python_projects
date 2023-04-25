import random
from card import Card


class Deck_of_Cards:
    def __init__(self) -> None:
        self.faces = {
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "jack": 11,
            "queen": 12,
            "king": 13,
            "ace": 14,
        }
        self.suites = ["hearts", "spades", "clubs", "diamond"]
        self.deck = []
        for suite in self.suites:
            for face in self.faces.keys():
                card = Card(face, suite)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def get_top_card(self):
        return self.deck.pop()

    def get_bottom_card(self):
        return self.deck.pop(0)
    
    def deal(self, num_of_cards):
        cards = []
        for i in range(num_of_cards):
            cards.append(self.deck.pop())
        return cards

    def cards_left(self):
        return f"There are {len(self.deck)} cards left in the deck."

    def list_all_cards(self):
        for card in self.deck:
            print(card.card_info)
