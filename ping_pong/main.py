from time import sleep
from turtle import Screen

from paddle import Paddle
from score import Score
from ball import Ball

COUNT = 0
WIDTH = 1000
HEIGHT = 1000
EDGES = 500
PADDLE_CONTACT_DISTANCE = 100
PADDLE_WIDTH_DISTANCE = 435
OUT_OF_BOUNDS = 470
PLAYER_1_SCORE_LOC = (-20, 475)
PLAYER_2_SCORE_LOC = (20, 475)
player_1_positions = (-450, 0)
player_2_positions = (450, 0)

screen = Screen()

# Screen setup for the ping pong game
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("ping-pong")
screen.tracer(0)


# Game Setup

# Create two paddle objects -- Done
# Create a Ball object --
# Create score object -- H

# Paddle should move when the ball crosses the line -- incorrect
# We can simply assign different keys for left and right paddle.


player_1_score = Score(PLAYER_1_SCORE_LOC)
player_2_score = Score(PLAYER_2_SCORE_LOC)
player_1_paddle = Paddle(player_1_positions)
player_2_paddle = Paddle(player_2_positions)

ball = Ball()
# Screen listeners. Listen for keystrokes
# In this game, the paddle can only move up and down
# "w" and "s" will move left paddle and "up" and "down" moves the right paddle
screen.listen()
screen.onkey(fun=player_1_paddle.move_down, key="s")
screen.onkey(fun=player_1_paddle.move_up, key="w")
screen.onkey(fun=player_2_paddle.move_down, key="Down")
screen.onkey(fun=player_2_paddle.move_up, key="Up")

game_on = True
while game_on:
    sleep(0.1)
    screen.update()

    # Collision with wall
    if ball.ycor() >= EDGES or ball.ycor() <= -1 * EDGES:
        ball.bounce()
    ball.move()

    # Collision with paddle
    if (
        ball.distance(player_1_paddle) < PADDLE_CONTACT_DISTANCE
        and ball.xcor() <= -1 * PADDLE_WIDTH_DISTANCE
        or ball.distance(player_2_paddle) < PADDLE_CONTACT_DISTANCE
        and ball.xcor() >= PADDLE_WIDTH_DISTANCE
    ):
        ball.bounce_x()
        ball.increase_count()

    # Out of bounds check

    if ball.xcor() >= OUT_OF_BOUNDS:
        ball.reset_position()
        player_1_score.increase_score()
    elif ball.xcor() <= -1 * OUT_OF_BOUNDS:
        ball.reset_position()
        player_2_score.increase_score()

    if ball.count % 5 == 0:
        ball.increase_speed()


# To exit
screen.exitonclick()
