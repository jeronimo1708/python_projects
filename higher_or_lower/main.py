import os
import sys
from random import shuffle
from game_data import data


play_on = True
shuffle(data)
choice_mapping = {"a": 0, "b": 1}

# Functions for the program


def add_to_queue():
    """"""
    data_to_be_added = data.pop()
    queue.append(data_to_be_added)


def display_vs():
    print(
        f"Compare A: {queue[0]['name']} is a {queue[0]['description']} from {queue[0]['country']}"
    )
    print("vs")
    print(
        (
            f"Against B: {queue[1]['name']} is a {queue[1]['description']} from {queue[1]['country']}"
        )
    )


def player_input():
    choice = ""
    while choice not in ("a", "b"):
        choice = input("Who has more followers? A or B\n").lower()
    return choice


def compare_player_choice(choice):
    if choice == "a" and queue[0]["follower_count"] > queue[1]["follower_count"]:
        return True
    elif choice == "b" and queue[1]["follower_count"] > queue[0]["follower_count"]:
        return True
    else:
        return False


def play_again():
    choice = ""
    while choice not in ("y", "n"):
        choice = input("Do you want to play again? (y/n) \n").lower()
    return choice


# Program begins here......................

print("Welcome to higher-lower game")

while data:
    queue = []
    score = 0

    while play_on:
        # At start up, always add 2 elements to the empty queue.
        if not queue:
            for i in range(2):
                add_to_queue()
        game = False

        # Show player the options to select from.
        display_vs()

        # Take player input
        choice = player_input()

        # Check if player is correct and add the new item in the queue
        # If the player is incorrect, then end the game.
        if compare_player_choice(choice):
            queue.pop(0)
            add_to_queue()
            score += 1
            print(f"Your current score is {score}")
        else:
            print(
                f"Oops! That is incorrect! You managed to get {score} questions right!"
            )
            play_on = False

    choice = play_again()
    if choice == "n":
        os.system('clear')
        print("Thank you for playing")
        sys.exit()
    else:
        os.system('clear')
        play_on = True
