"""Snake class for the Snake Game"""

from turtle import Turtle
import random

from food import Food

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

COLORS = [
    "#f2668b",  # Pinkish
    "#23c7d9",  # Light-Blue
    "#48d9a4",  # Mint-Green
    "#f2bf27",  # Sunflower-Yellow
    "#f2f1df",  # Off-White
    "#f2889b",  # Light-Pinkish
    "#33d7e9",  # Lighter-Blue
    "#58e9b4",  # Light-Mint-Green
    "#f2cf37",  # Light-Sunflower-Yellow
    "#f2f1ef",  # Light-Off-White
]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)

        # Choose a random color for the new segment
        new_segment.fillcolor(random.choice(COLORS))

        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # Function to change snake direction upwards
    def go_up(self):
        if self.segments[0].heading() != 270:  # Prevent backward movement
            self.segments[0].setheading(90)  # Heading north

    # Function to change snake direction downwards
    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)  # Heading south

    # Function to change snake direction leftwards
    def go_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)  # Heading west

    # Function to change snake direction rightwards
    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)  # Heading east

    def extend(self):
        # Add a new segment to the snake
        new_segment = Turtle("square")
        new_segment.penup()

        # Get the color of the last segment
        last_segment_color = self.segments[-1].fillcolor()

        # Find the index of this color in the color list
        color_index = next(
            (
                i
                for i, (_, _, color) in enumerate(COLORS)
                if color == last_segment_color
            ),
            None,
        )

        # If the color was found in the list, use the next color for the new segment
        if color_index is not None and color_index < len(COLORS) - 1:
            new_segment.color(COLORS[color_index + 1][2])
        else:
            # If the color was not found in the list, use the first color
            new_segment.color(COLORS[0][2])

        # Move the new segment to the position of the last segment
        new_segment.goto(self.segments[-1].position())

        # Add the new segment to the list of segments
        self.segments.append(new_segment)

    def detect_collision_with_food(self, food):
        """returns True if the snake head is within 15 pixels of the food turtle, otherwise returns False"""
        if self.head.distance(food) < 15:
            return True
        else:
            return False

    def detect_collision_with_wall(self):
        """returns True if the snake head is outside the screen, otherwise returns False"""
        if (
            self.head.xcor() > 560
            or self.head.xcor() < -560
            or self.head.ycor() > 560
            or self.head.ycor() < -560
        ):
            return True
        else:
            return False

    def detect_collision_with_tail(self):
        """returns True if the snake head collides with any of the snake's tail segments, otherwise returns False"""
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
