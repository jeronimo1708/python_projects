from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, positions) -> None:
        super().__init__()
        self.penup()
        self.goto(positions)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

