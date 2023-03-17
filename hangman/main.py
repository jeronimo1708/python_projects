import random
import sys
from stages import stages, logo
from words import word_list

print(logo)
chosen_word = word_list[random.randint(0, len(word_list)-1)]
guessed_list = [""] * len(chosen_word)

game_on = True
lives = 6

def win_check(guessed_list):
    if "" in guessed_list:
        return True
    else:
        print(f"You Win! The word was -> {''.join(guessed_list)}")
        return False
    
while game_on:
    guess = input("Guess a letter").lower()
    if guess in guessed_list:
        print("You have already guessed this word!")
    elif guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if guess == letter:
                guessed_list[index] = guess                        
            game_on = win_check(guessed_list)
            if not game_on:
                sys.exit()
        print(f"Correct! Here is your guesses -> {guessed_list}")    
            
    else:
        lives -= 1
        if lives > 0:
            print(stages[lives])
            print(f"That is not right. You have {lives} lives left")
        else:
            game_on = False
            print(stages[lives])
            print("You have no lives left! Game Over")
            