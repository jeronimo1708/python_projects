# This program greets users, takes input from user asking for city they grew up in and the name of a pet.
# It combines the two names and shows the band name.
# Input cursor should show on a new line

print("Welcome to your band name generator")
print()
city = input("Which city did you grow up in?\n")
print()
pet_name = input("What is or would be the name of your pet?\n")
print()
print(f"Your band name is {city.title()} {pet_name.title()}")
