import time
import random
from turtle import Screen

from crosser import Crosser
from cars import Car
from levels import Level

COLORS = ["red", "green", "blue", "yellow", "purple"]
DENOMINATOR = 100

cars_list = []


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Crosser object
crosser = Crosser()
level = Level()

# Listening for keyboard input
screen.listen()
screen.onkeypress(crosser.up, "Up")

count = 0
game_on = True
while game_on:
    # Screen is updated at the beginning of the loop
    screen.update()
    time.sleep(0.01)
    # Car is only generated when count % variable is equal to 0
    # This is to control the speed in which the cars are generated
    # When the condition matches, car is generated and stored in the cars list
    # The for loop moves all the cars in the list one by one
    if count % DENOMINATOR == 0:
        car = Car(random.randint(-250, 270), random.choice(COLORS))
        cars_list.append(car)
    for car in cars_list:
        car.move()

    # Removing all the cars that are out of the screen from the cars list and the screen
    for car in cars_list:
        if car.xcor() <= -320:
            car.hideturtle()
            cars_list.remove(car)

        # Check if the crosser makes contact with any cars
        if crosser.distance(car) < 20:
            level.game_over()
            game_on = False

    # Win condition
    # When the crosser crosse 290 on the y axis, reset everything and increase the level
    # Level difficulty increase means more cars are generated for that level
    if crosser.ycor() >= 290:
        print("You win!")
        level.increase_level()
        crosser.reset()
        DENOMINATOR -= 20


    count += 1

    # Add count at the end of the loop
    count += 1


# Exit screen on click
screen.exitonclick()
