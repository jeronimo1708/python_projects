from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier"
FONT_SIZE = 15
FONT_WEIGHT = "bold"

class Score(Turtle):
    def __init__(self, pos) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(pos)        
        self.score = 0
        self.color("white")        
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=(FONT, FONT_SIZE, FONT_WEIGHT))
