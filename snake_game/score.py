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
        self.color("white")        
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT, 15, FONT_WEIGHT))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=(FONT, 15, FONT_WEIGHT))