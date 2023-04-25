class Player:
    def __init__(self, name, chips) -> None:
        self.name = name
        self.chips = chips
        self.hand = []
        self.hand_value = 0

    # @property
    # def hand(self):
    #     return self._hand

    # @hand.setter
    # def hand(self, value):
    #     if self._hand != value:
    #         self.calculate_hand_value()
    #     self._hand = value

    def calculate_hand_value(self):
        self.hand_value = 0
        for card in self.hand:
            self.hand_value += card.value
