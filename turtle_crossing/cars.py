from turtle import Turtle

class Car(Turtle):
    def __init__(self, y_axis, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=1.5)
        self.setheading(180)
        self.goto(300, y_axis)
        self.speed(0)

    def move(self):
        self.fd(2)
