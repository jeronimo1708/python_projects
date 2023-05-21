from turtle import Turtle, Screen

etch = Turtle()
screen = Screen()

def move_forwards():
    etch.setheading(0)
    etch.forward(10)

def move_backwards():
    etch.setheading(180)
    etch.forward(10)

def move_down():
    etch.setheading(270)
    etch.forward(10)

def move_up():
    etch.setheading(90)
    etch.forward(10)

def move_clockwise():
    etch.right(25)
    etch.forward(10)

def move_counter_clockwise():
    etch.left(25)
    etch.forward(10)

def clear():
    etch.reset()

screen.listen()
screen.onkey(fun=move_forwards, key="d")
screen.onkey(fun=move_backwards, key="a")
screen.onkey(fun=move_down, key="s")
screen.onkey(fun=move_up, key="w")
screen.onkey(fun=clear, key="c")
screen.onkey(fun=move_clockwise, key="e")
screen.onkey(fun=move_counter_clockwise, key="q")

screen.exitonclick()