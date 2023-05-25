from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.reposition_food()

    def reposition_food(self):
        random_x = random.randint(-250,250)
        random_y = random.randint(-250,250)
        self.goto(random_x, random_y)
