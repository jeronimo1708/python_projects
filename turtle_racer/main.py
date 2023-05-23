import sys
import random
from turtle import Turtle, Screen

# TO DO: Need to fix start positions of all turtles when the game is restarted.

all_turtles = []
colors = ["red", "blue", "green", "yellow", "purple", "pink"]


screen = Screen()
screen.setup(width=600, height=600)


def get_user_input():
    user_input = ""
    while user_input not in colors:
        user_input = screen.textinput(
            title="Place Bet",
            prompt='Choose which turtle you think will win the race. ("red", "blue", "green", "yellow", "purple", "pink")',
        )
    return user_input


def draw_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setposition(x=250, y=300)
    finish_line.pendown()
    finish_line.setheading(270)
    finish_line.fd(600)


def create_turtles():
    for color in colors:
        tortoise = Turtle(shape="turtle")
        tortoise.penup()
        tortoise.color(color)
        all_turtles.append(tortoise)


def set_turtles_to_start(start_y):
    for tortoise in all_turtles:
        tortoise.setposition(x=start_x, y=start_y)
        start_y += 90


def game(game_on):
    while game_on:
        for tortoise in all_turtles:
            tortoise.fd(random.randint(1, 10))
            # print(f"{tortoise.color()} positon is {tortoise.position()}")
            if tortoise.position()[0] >= 250:
                if tortoise.pencolor() == user_input:
                    print(
                        f"You've won! Your choice of {tortoise.pencolor().upper()} turtle won the race!"
                    )
                else:
                    print(
                        f"You've lost! Turtle of color {tortoise.pencolor().upper()} has beat your choice of {user_input.upper()} turtle in the race!"
                    )
                game_on = False
    return game_on


def play_again():
    play_again = ""
    while play_again.lower() not in ("y", "n"):
        play_again = screen.textinput(
            title="Play Again?", prompt="Would you like to play again? (y/n)"
        )
    return play_again


play_game = True
while play_game:
    game_on = False
    user_input = get_user_input()
    if user_input:
        game_on = True
    while game_on:
        start_x = -280
        start_y = -220
        draw_finish_line()
        create_turtles()
        set_turtles_to_start(start_y)
        game_on = game(game_on)
    play_again = play_again()
    if play_again == "n":
        sys.exit()
    else:
        screen.clearscreen()


screen.exitonclick()
