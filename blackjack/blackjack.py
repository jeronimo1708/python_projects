from deck_of_cards import Deck_of_Cards


class BlackJack(Deck_of_Cards):
    def __init__(self) -> None:
        super().__init__()
        self.player_hand = []
        self.computer_hand = []
        self.player_total = 0
        self.computer_total = 0

    def deal(self, player):
        for i in range(2):
            player.append(self.get_top_card())

    def deal_one(self, player):
        for i in range(1):
            player.append(self.get_top_card())
