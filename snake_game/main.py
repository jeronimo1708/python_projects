import time
from turtle import Turtle, Screen

from snake import Snake

# Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(fun=snake.move_right, key="d")
screen.onkey(fun=snake.move_left, key="a")
screen.onkey(fun=snake.move_down, key="s")
screen.onkey(fun=snake.move_up, key="w")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
