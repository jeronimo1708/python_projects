from turtle import Turtle

class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.reset()

    def up(self):
        self.fd(10)

    def reset(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -270)