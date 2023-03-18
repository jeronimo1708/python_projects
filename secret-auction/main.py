import os
from art import logo
from subprocess import call

print(logo)

game_on = True
storage = {}
max_bid = float("-inf")
max_bidder = str()

def clear():
    _ = call("clear" if os.name == 'posix' else 'cls')

while game_on:
    user = input("What is your name?\n").capitalize()
    bid = int(input("How much do you want to bid?\n"))
    if user not in storage:
        storage[user] = bid
    play_on = ""
    while play_on not in ["yes", "no"]:
        play_on = input("Are there any more bidders?\n").lower()
    if play_on == "no":
        game_on = False
    else:
        clear()

for k, v in storage.items():
    if v > max_bid:
        max_bid = v
        max_bidder = k
    
print(f"{max_bidder} has won the bid wars with a bid of {max_bid}")
    


    