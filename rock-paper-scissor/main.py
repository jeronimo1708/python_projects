import sys
import random

rock = '''   
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

paper = '''
            _______
        ---'   ____)____
                ______)
                _______)
                _______)
        ---.__________)
        '''

scissors = '''
                _______
            ---'   ____)____
                    ______)
                __________)
                (____)
            ---.__(___)
            '''

options = [rock, paper, scissors]
print("Rock, Paper, Scissors")
game_on = True
play = ""
while play not in ["y", "n"]:
    play = input("Would you like to begin?(y/n)").lower()
    if play == "n":
        sys.exit()
while game_on:
    print("Choose rock, paper or scissor")
    player_choice = ""
    while player_choice not in ["0", "1", "2"]:
        player_choice = input("Choose 0 -> rock, 1 -> paper, 2-> scissors")
    player_choice = int(player_choice)
    player_choice_pic = options[player_choice]
    print(f"You chose {player_choice_pic}")
    computer_choice = random.randint(0, 2)
    computer_choice_pic = options[computer_choice]
    print(f"Computer chose {computer_choice_pic}")
    if player_choice == 0 and computer_choice == 2:
        print("You win")
    elif player_choice == 2 and computer_choice == 0:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win")
    elif player_choice < computer_choice:
        print("You lose")
    else:
        print("Its a Tie!")

    play_on = ""
    while play_on not in ["y", "n"]:
        play_on = input("Would you like to play again?(y/n)").lower()
        if play_on == "n":
            game_on = False


# Rules
# rock beats scissors
# scissors beat paper
# paper beats rock

    




                




