import sys

print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______
*******************************************************************************
''')
print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice = input("You want to go Left or Right?\n").lower()
while choice not in ["left", "right"]:
    choice = input("You want to go Left or Right?\n").lower()
if choice == "right":
    print("Fall into a hole. Game Over.")
    sys.exit()
else:
    choice = input("There is a river ahead. Type Wait if you want to wait for a boat or Swim, if you want to swim across\n").lower()
while choice not in ["wait", "swim"]:
    choice = input("There is a river ahead. Type Wait if you want to wait for a boat or Swim, if you want to swim across\n").lower()
if choice == "swim":
    print("Attacked by trout. Game Over.")
    sys.exit()
else:
    choice = input("You safely crossed the river. There are two doors, Which one you want to open? Type 1 or 2 to proceed").lower()
while choice not in ["1", "2", "one", "two"]:
    choice = input("You safely crossed the river. There are two doors, Which one you want to open? Type 1 or 2 to proceed").lower()
if choice in ["1", "one"]:
    print("Eaten by beasts. Game Over.")
    sys.exit()
else:
    print("You win!")


