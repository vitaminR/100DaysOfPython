from turtle import Turtle, Screen
from turtle import *
import random

# screen
screen = Screen()
screen.setup(900, 600)

# Move the window to the left side of the screen
root = screen.getcanvas().winfo_toplevel()
root.geometry("+0+0")

# player
player = Turtle()
player.shape("turtle")
player.color("green")
player.pensize(3)
player.speed(10)


# movement
def up():
    player.setheading(90)
    player.forward(10)


def down():
    player.setheading(270)
    player.forward(10)


def right():
    player.setheading(0)
    player.forward(10)


def left():
    player.setheading(180)
    player.forward(10)


# #square
# for _ in range(4):
#     right()
#     player.penup()
#     right()
#     player.pendown()


def magic_color():
    # return a string with random color string of 6 hex digits:
    return "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])


# # geometric art
# side = 3
# while not side == 10:
#     for _ in range(side):
#         player.forward(100)
#         player.setheading(player.heading() + -360 / side)
#     # choose random turtle color
#     player.color(magic_color())
#     side += 1

# geometric art
walks = 0
while not walks == 500:
    player.forward(38)
    player.setheading(player.heading() + random.randint(0, 360))
    # choose random turtle color
    player.color(magic_color())
    walks += 1


screen.exitonclick()
