"""Snake class for the Snake Game"""

from turtle import Turtle
import random
import art

from food import Food

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


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
        new_segment.fillcolor(random.choice(list(art.COLORS.values())))
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

    def extend(self, color):
        """Add a new segment to the snake."""
        # Deepcopy the last segment in the snake
        new_segment = self.segments[-1].clone()
        new_segment.hideturtle()
        new_segment.goto(self.segments[-1].position())
        new_segment.showturtle()

        # Set the color of the new segment to the color of the food
        new_segment.color(color)

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
