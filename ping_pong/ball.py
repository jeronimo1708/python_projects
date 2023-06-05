import random
from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.move_x = 10
        self.move_y = -10
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)        

    def bounce(self):
        self.move_y = -1 * self.move_y

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


            


        
