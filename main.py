
import colorgram
import random
from turtle import Turtle, Screen

# Create color list from picture color palette.
colors = colorgram.extract("hirst_2587800b.jpg", 10)
color_list = []

for color in colors:
    rgb = [color.rgb.r, color.rgb.g, color.rgb.b]
    color_list.append(rgb)

# Set up turtle.
turk = Turtle()
turk.shape("turtle")
turk.speed("normal")

# Set up screen.
screen = Screen()
screen.bgcolor("#A4D4F0")
start_x = -925
start_y = -490
screen.colormode(255)


def position(x, y):
    turk.penup()
    turk.setpos(x, y)
    turk.setheading(0)
    turk.pendown()


def row_n_dots(n, direction="right"):
    if direction == "right":
        turk.setheading(0)
    elif direction == "left":
        turk.setheading(180)
    elif direction == "down":
        turk.setheading(270)
    else:
        turk.setheading(90)

    for n in range(0, n - 1):
        turk.dot(50, random.choice(color_list))
        turk.penup()
        turk.forward(110)
        turk.pendown()
        turk.dot(50, random.choice(color_list))


def shift_up(distance=100):
    turk.setheading(90)
    turk.forward(distance)
    turk.setheading(180)


def hirst_dots(dots_per_row=5):
    row_n_dots(dots_per_row)

    turk.dot(50, random.choice(color_list))
    turk.penup()
    turk.setheading(90)
    turk.forward(100)
    turk.dot(50, random.choice(color_list))
    turk.setheading(180)
    turk.forward(110)

    row_n_dots(dots_per_row)


position(start_x, start_y)
for i in range(1, 12):
    row_n_dots(18, "right")
    position(start_x, start_y + (i * 100))

##############################
# Screen Exit is last command!
screen.exitonclick()
