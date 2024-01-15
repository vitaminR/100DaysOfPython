# art.py
"""art module for pong game"""

import turtle

# draw wall


def draw_wall():
    wall = turtle.Turtle()
    wall.penup()
    wall.goto(-250, -250)  # Starting point of the wall
    wall.pendown()
    wall.pensize(3)
    wall.color("white")

    for _ in range(4):
        wall.forward(500)  # Length of the wall
        wall.left(90)  # Turn left to draw the next side of the wall


draw_wall()

# draw scoreboard
