# gear.py
"""the paddle and ball logic"""

from turtle import Turtle, Screen

TOP_WALL = 390
BOTTOM_WALL = -390
LEFT_WALL = 390
RIGHT_WALL = -390


# paddle class
class Paddle:
    def __init__(self, screen, location, up_key, down_key):
        self.paddle_block = Turtle()
        self.paddle_block.color("white")
        self.paddle_block.penup()
        self.paddle_block.shape("square")
        self.paddle_block.shapesize(stretch_wid=5, stretch_len=1)
        self.location = location
        self.up_pressed = False  # Initialize up_pressed
        self.down_pressed = False  # Initialize down_pressed
        self.screen = screen  # Use the passed Screen object
        self.screen.onkeypress(self.set_up_pressed, up_key)
        self.screen.onkeyrelease(self.set_up_not_pressed, up_key)
        self.screen.onkeypress(self.set_down_pressed, down_key)
        self.screen.onkeyrelease(self.set_down_not_pressed, down_key)

    def set_up_pressed(self):
        self.up_pressed = True

    def set_up_not_pressed(self):
        self.up_pressed = False

    def set_down_pressed(self):
        self.down_pressed = True

    def set_down_not_pressed(self):
        self.down_pressed = False

    def loc(self):
        if self.location == "left":
            self.paddle_block.setposition(-500, 0)
        elif self.location == "right":
            self.paddle_block.setposition(500, 0)

    def paddle_move(self):
        if (
            self.up_pressed and self.paddle_block.ycor() < TOP_WALL
        ):  # Check if up key is pressed and paddle is below the top wall
            new_y = self.paddle_block.ycor() + 20
            self.paddle_block.sety(new_y)
        elif (
            self.down_pressed and self.paddle_block.ycor() > BOTTOM_WALL
        ):  # Check if down key is pressed and paddle is above the bottom wall
            new_y = self.paddle_block.ycor() - 20
            self.paddle_block.sety(new_y)

    # ball class


class Ball:
    def __init__(self):
        self.ball = Turtle()  # Create a new Turtle object for the ball
        self.ball.shape("circle")  # Set the shape to circle
        self.ball.color("red")  # Set the color to white
        self.ball.penup()  # Lift the pen up
