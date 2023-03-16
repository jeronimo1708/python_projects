import random
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("This program will create a strong 15 character random password")
print("Here is your strong password")
password = []
for i in range(8):
    character = lowercase_letters[random.randint(0, 25)]
    password.append(character)
for i in range(2):
    character = uppercase_letter[random.randint(0, 25)]
    password.append(character)
for i in range(3):
    character = uppercase_letter[random.randint(0, 9)]
    password.append(character)
for i in range(2):
    character = symbols[random.randint(0, 8)]
    password.append(character)
random.shuffle(password)
strong_password = "".join(password)
print(strong_password)




