# snake.py
from turtle import Turtle
import random
from art import COLORS

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """
    Snake class for the Snake game. Manages the snake's appearance, movement,
    growth, and collision detection.
    """

    def __init__(self, wall_width, wall_height):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.speed = 1

    def create_snake(self):
        """
        Initializes the snake with a set number of segments at the start of the game.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the specified position.
        """
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.fillcolor(random.choice(list(COLORS.values())))
        self.segments.append(new_segment)

    def move(self):
        """
        Moves the snake forward by moving each segment to the position of the previous segment.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE * self.speed)

    def extend(self, color):
        """
        Adds a new segment to the end of the snake with the specified color.
        """
        self.add_segment(self.segments[-1].position())
        self.segments[-1].color(color)

    def change_direction(self, direction):
        """
        Changes the direction of the snake's head to the specified angle.
        """
        if direction == "up" and self.head.heading() != 270:
            self.head.setheading(90)
        elif direction == "down" and self.head.heading() != 90:
            self.head.setheading(270)
        elif direction == "left" and self.head.heading() != 0:
            self.head.setheading(180)
        elif direction == "right" and self.head.heading() != 180:
            self.head.setheading(0)

    def detect_collision_with_food(self, food):
        """
        Checks if the snake's head is close enough to the food to consider it eaten.
        """
        return self.head.distance(food) < 15

    def detect_collision_with_wall(self):
        """
        Checks if the snake's head has collided with the wall boundaries.
        """
        x, y = self.head.xcor(), self.head.ycor()
        return not (
            -self.wall_width / 2 + 10 < x < self.wall_width / 2 - 10
            and -self.wall_height / 2 + 10 < y < self.wall_height / 2 - 10
        )

    def detect_collision_with_tail(self):
        """
        Checks if the snake's head has collided with any segment of its tail.
        """
        return any(self.head.distance(segment) < 10 for segment in self.segments[1:])
