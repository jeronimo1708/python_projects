import random
import sys
from art import logo


def play_again():
    play_again = ""
    while play_again not in ("y", "n"):
        play_again = input("Would you like to play again? (y/n)").lower()
    return play_again


def play_once_more(play_again):
    if play_again == "n":
        return False
    else:
        return True


def high_low_checker(num):
    if num > NUMBER:
        print("Too High")
    elif num < NUMBER:
        print("Too Low")


game = True
print(logo)
while game:
    EASY = 10
    HARD = 5
    DIFF = {"easy": EASY, "hard": HARD}
    NUMBER = random.randint(0, 101)

    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 & 100. Can you guess that number?")
    difficulty = ""
    while difficulty not in ("easy", "hard"):
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    print(f"You have {DIFF[difficulty]} attempts left")

    game_on = True
    while game_on:
        guess = int(input("Make a guess: "))
        if guess == NUMBER:
            print("You guessed correct! You Win.")
            game_on = False
        else:
            if DIFF[difficulty] == 0:
                print(f"You ran out of chances. The number was {NUMBER}")
                game_on = False
            else:
                DIFF[difficulty] -= 1
                high_low_checker(guess)
                print(
                    f"You have {DIFF[difficulty]} attempts remaining to guess the number"
                )
    game = play_once_more(play_again())
