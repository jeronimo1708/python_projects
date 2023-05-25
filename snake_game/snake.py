from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    def __init__(self) -> None:
        self.snake_list = []
        for i in range(len(POSITIONS)):
            positions = POSITIONS[i]
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(positions)
            self.snake_list.append(snake)

        self.head = self.snake_list[0]

    def move(self):
        for snake_part in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_part - 1].xcor()
            new_y = self.snake_list[snake_part - 1].ycor()
            self.snake_list[snake_part].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
