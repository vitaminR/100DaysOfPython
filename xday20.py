# from turtle import Turtle, Screen
from turtle import *
import random
import math
import time

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0, 0)

# Move the window to the left side of the screen
root = screen.getcanvas().winfo_toplevel()
root.geometry("+0+0")


# Bryan Brinkman's color palette
color_list_with_names = [
    ("Pinkish", "#f2668b", (242, 102, 139)),
    ("Light Blue", "#23c7d9", (35, 199, 217)),
    ("Mint Green", "#48d9a4", (72, 217, 164)),
    ("Sunflower Yellow", "#f2bf27", (242, 191, 39)),
    ("Off White", "#f2f1df", (242, 241, 223)),
]

# Slightly varied color palette
varied_colors = [
    ("Light Pinkish", "#f2889b"),
    ("Lighter Blue", "#33d7e9"),
    ("Light Mint Green", "#58e9b4"),
    ("Light Sunflower Yellow", "#f2cf37"),
    ("Light Off White", "#f2f1ef"),
]

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# Create initial snake segments
for i, pos in enumerate(starting_pos):
    new_segment = Turtle("square")
    new_segment.color(color_list_with_names[i][1])
    new_segment.penup()
    new_segment.goto(pos)
    segments.append(new_segment)
    time.sleep(1)


# Function to change snake direction upwards
def go_up():
    if segments[0].heading() != 270:  # Prevent backward movement
        segments[0].setheading(90)  # Heading north


# Function to change snake direction downwards
def go_down():
    if segments[0].heading() != 90:
        segments[0].setheading(270)  # Heading south


# Function to change snake direction leftwards
def go_left():
    if segments[0].heading() != 0:
        segments[0].setheading(180)  # Heading west


# Function to change snake direction rightwards
def go_right():
    if segments[0].heading() != 180:
        segments[0].setheading(0)  # Heading east


# Bind keys to movement functions
screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")
screen.onkey(go_left, "a")
screen.onkey(go_right, "d")

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

screen.exitonclick()
