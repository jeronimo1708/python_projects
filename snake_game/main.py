import time
from turtle import Screen

from snake import Snake
from food import Food
from score import Score

END_LOCATION_X = 280
END_LOCATION_Y = 280

# Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

# The tracer annd update are screen methonds of turtle library
# When tracer is set to 0, the animations are cancelled
# The update method shows the animations that have passed whenever it is called
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.move_right, key="d")
screen.onkey(fun=snake.move_left, key="a")
screen.onkey(fun=snake.move_down, key="s")
screen.onkey(fun=snake.move_up, key="w")


game_on = True
while game_on:
    # In the game loop, I am waiting to refresh animations every 0.1 seconds to make it appear smooth.
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with the food
    # If the snake head comes within 15 pixels of food, then count it as a collision
    # When collision happens, the food should go to a new random location
    # the snake length should increase
    # Score should be updated

    if snake.head.distance(food) < 15:
        food.reposition_food()
        snake.extend()
        score.increase_score()

    # Detect collision with wall

    if snake.head.position()[0] > END_LOCATION_X or snake.head.position()[0] < -END_LOCATION_X or snake.head.position()[1] > END_LOCATION_Y or snake.head.position()[1] < -END_LOCATION_Y:
        score.game_over()
        game_on = False

    # Detect collision with tail
    # If head touches body then trigger game over sequence
    for snake_part in snake.snake_list[1::]:
        if snake.head.distance(snake_part) < 10:
            score.game_over()
            game_on = False



screen.exitonclick()
