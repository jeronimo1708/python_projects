import time
from turtle import Turtle, Screen

# Screen setup
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)


# Snake Setup
x = 0
snake_list = []
for i in range(3):
    snake = Turtle(shape="square")
    snake.penup()
    snake.color("white")
    snake.fd(x)
    x -= 20
    snake_list.append(snake)

screen.update()

def move_up():
    snake_list[0].setheading(90)

def move_right():
    snake_list[0].setheading(0)

def move_down():
    snake_list[0].setheading(270)

def move_left():
    snake_list[0].setheading(180)



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for snake_part in range(len(snake_list)-1, 0, -1):
        new_x = snake_list[snake_part-1].xcor()    
        new_y = snake_list[snake_part-1].ycor()           
        snake_list[snake_part].goto(new_x, new_y)

    snake_list[0].fd(20)

    screen.listen()
    screen.onkey(fun=move_right, key="d")
    screen.onkey(fun=move_left, key="a")
    screen.onkey(fun=move_down, key="s")
    screen.onkey(fun=move_up, key="w")


        


    


screen.exitonclick()