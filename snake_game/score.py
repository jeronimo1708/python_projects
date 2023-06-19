import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = 15
FONT_WEIGHT = "normal"

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)        
        self.score = 0
        self.high_score = self.load_high_score()
        self.color("white")        
        self.update_score()
        print(os.getcwd())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT, 15, FONT_WEIGHT))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=(FONT, 15, FONT_WEIGHT))

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.score))

    def load_high_score(self):
        with open("high_score.txt", "r") as f:
            high_score = int(f.read())
        return high_score
