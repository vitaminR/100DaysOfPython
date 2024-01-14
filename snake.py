"""Snake class for the Snake Game"""

from turtle import Turtle
import random

from food import Food

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

COLORS = {
    "Pinkish": "#f2668b",
    "Light-Blue": "#23c7d9",
    "Mint-Green": "#48d9a4",
    "Sunflower-Yellow": "#f2bf27",
    "Off-White": "#f2f1df",
    "Light-Pinkish": "#f2889b",
    "Lighter-Blue": "#33d7e9",
    "Light-Mint-Green": "#58e9b4",
    "Light-Sunflower-Yellow": "#f2cf37",
    "Light-Off-White": "#f2f1ef",
}


class Snake:
    def __init__(self, wall_width, wall_height):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.is_moving = True

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.fillcolor(random.choice(list(COLORS.values())))
        self.segments.append(new_segment)

    def move(self):
        if self.is_moving:
            for seg_num in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)

    def stop(self):
        self.is_moving = False

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
        """Add a new segment to the snake."""
        # Deepcopy the last segment in the snake
        new_segment = self.segments[-1].clone()
        new_segment.hideturtle()
        new_segment.goto(self.segments[-1].position())
        new_segment.showturtle()

        # Get the color of the last segment
        last_segment_color = self.segments[-1].color()[0]

        # Get the list of colors from the COLORS dictionary
        color_list = list(COLORS.values())

        # Find the index of the last segment's color in the color_list
        color_index = (
            color_list.index(last_segment_color)
            if last_segment_color in color_list
            else None
        )

        # If the color was found in the list, use the next color for the new segment
        # If the color was not found in the list, or it's the last color in the list, use the first color
        if color_index is not None and color_index < len(color_list) - 1:
            new_segment.color(color_list[color_index + 1])
        else:
            new_segment.color(color_list[0])

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
            self.head.xcor() > self.wall_width / 2 - 10
            or self.head.xcor() < -self.wall_width / 2 + 10
            or self.head.ycor() > self.wall_height / 2 - 10
            or self.head.ycor() < -self.wall_height / 2 + 10
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
