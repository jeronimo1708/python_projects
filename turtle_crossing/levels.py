from turtle import Turtle

ALIGNMENT = "center"
FONT = 15
FONT_WEIGHT = "normal"

class Level(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)        
        self.level = 1
        self.color("black")        
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=(FONT, 15, FONT_WEIGHT))

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(f"Level : {self.level}", align=ALIGNMENT, font=(FONT, 15, FONT_WEIGHT))