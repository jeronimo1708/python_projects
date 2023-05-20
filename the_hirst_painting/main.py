import colorgram
import random
from turtle import Turtle, Screen


# to extract colors from image.jpg
# Commented out after extracting and cleaning the colors in images.jpg
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
# for color in colors:
#     color = color.rgb
#     r = color[0]
#     b = color[1]
#     g = color[2]
#     rgb_color = (r, g, b)
#     rgb_colors.append(rgb_color)

# print(rgb_colors)

hirst_extracted_color_list = [
    (202, 110, 164),
    (240, 241, 245),
    (236, 243, 239),
    (149, 50, 75),
    (222, 136, 201),
    (53, 123, 93),
    (170, 41, 154),
    (138, 20, 31),
    (134, 184, 163),
    (197, 73, 92),
    (47, 86, 121),
    (73, 35, 43),
    (145, 149, 178),
    (14, 70, 98),
    (232, 165, 176),
    (160, 158, 142),
    (54, 50, 45),
    (101, 77, 75),
    (183, 171, 205),
    (36, 74, 60),
    (19, 89, 86),
    (82, 129, 148),
    (147, 19, 17),
    (27, 102, 68),
    (12, 64, 70),
    (107, 153, 127),
    (176, 208, 192),
    (168, 102, 99),
]

painting = Turtle()
screen = Screen()

screen.colormode(255)
painting.hideturtle()

rows, cols = 10, 10
x, y = 0.0, 0.0

# Setting start point
painting.penup()
painting.setheading(225)
painting.fd(250)
painting.setheading(0)

x, y = painting.position()

for _ in range(cols):
    for _ in range(rows):
        painting.color(random.choice(hirst_extracted_color_list))
        painting.dot(20)
        painting.penup()
        painting.fd(50)
    y += 50
    painting.goto(x, y)



# To have the screen not exit immediately
screen.exitonclick()
