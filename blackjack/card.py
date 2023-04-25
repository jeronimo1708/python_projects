import random


class Card:

    def __init__(self, face, suite) -> None:
        self.face = face
        self.suite = suite
        self.faces = {"two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, "ten":10, "jack":10, "queen":10, "king":10, "ace":10}
        self.value = self.faces[self.face]        
        self.suites = ["hearts", "spades", "clubs", "diamond"]

    def __repr__(self) -> str:
        return f"Card is {self.face} of {self.suite}"
    
    def card_info(self):
        print(f"Card is {self.face} of {self.suite}")


    