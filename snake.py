# from turtle import Turtle, Screen
from turtle import *
import random
import math
import time

# from xmain import


color_list = [
    (1, "Pinkish", "#f2668b"),
    (2, "Light-Blue", "#23c7d9"),
    (3, "Mint-Green", "#48d9a4"),
    (4, "Sunflower-Yellow", "#f2bf27"),
    (5, "Off-White", "#f2f1df"),
    (6, "Light-Pinkish", "#f2889b"),
    (7, "Lighter-Blue", "#33d7e9"),
    (8, "Light-Mint-Green", "#58e9b4"),
    (9, "Light-Sunflower-Yellow", "#f2cf37"),
    (10, "Light-Off-White", "#f2f1ef"),
]

starting_pos = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create initial snake segments
        for i, pos in enumerate(starting_pos):
            new_segment = Turtle("square")
            new_segment.color(color_list[i][1])
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
            time.sleep(1)

    def move(self):
        # Function to change snake direction upwards
        def go_up():
            if self.segments[0].heading() != 270:  # Prevent backward movement
                self.segments[0].setheading(90)  # Heading north

        # Function to change snake direction downwards
        def go_down():
            if self.segments[0].heading() != 90:
                self.segments[0].setheading(270)  # Heading south

        # Function to change snake direction leftwards
        def go_left():
            if self.segments[0].heading() != 0:
                self.segments[0].setheading(180)  # Heading west

        # Function to change snake direction rightwards
        def go_right():
            if self.segments[0].heading() != 180:
                self.segments[0].setheading(0)  # Heading east
