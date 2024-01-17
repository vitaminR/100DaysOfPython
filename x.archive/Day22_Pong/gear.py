# gear.py
"""the paddle and ball logic"""

from turtle import Turtle

# Constants for wall positions
TOP_WALL = 390
BOTTOM_WALL = -390
LEFT_WALL = 390
RIGHT_WALL = -390


# Paddle class
class Paddle:
    def __init__(self, screen, location, up_key, down_key):
        # Paddle initialization
        self.paddle_block = Turtle()
        self.paddle_block.color("white")
        self.paddle_block.shape("square")
        self.paddle_block.shapesize(stretch_wid=5, stretch_len=1)

        # Paddle position and key bindings
        self.location = location
        self.up_pressed = False
        self.down_pressed = False
        self.screen = screen
        self.screen.onkeypress(self.set_up_pressed, up_key)
        self.screen.onkeyrelease(self.set_up_not_pressed, up_key)
        self.screen.onkeypress(self.set_down_pressed, down_key)
        self.screen.onkeyrelease(self.set_down_not_pressed, down_key)
        print(f"Paddle created at {location} side")  # Print paddle creation

    def set_up_pressed(self):
        self.up_pressed = True
        print("Up key pressed")  # Debugging print statement

    def set_up_not_pressed(self):
        self.up_pressed = False
        print("Up key released")  # Debugging print statement

    def set_down_pressed(self):
        self.down_pressed = True
        print("Down key pressed")  # Debugging print statement

    def set_down_not_pressed(self):
        self.down_pressed = False
        print("Down key released")

    def loc(self):
        # Set initial location of the paddle
        if self.location == "left":
            self.paddle_block.setposition(-400, 0)
        elif self.location == "right":
            self.paddle_block.setposition(400, 0)
        print(f"Paddle set at {self.paddle_block.pos()}")  # Print paddle position

    def paddle_move(self):
        # Move paddle based on key presses
        if self.up_pressed and self.paddle_block.ycor() < TOP_WALL:
            new_y = self.paddle_block.ycor() + 20
            self.paddle_block.sety(new_y)
            print("Moved paddle up")  # Print paddle movement
        elif self.down_pressed and self.paddle_block.ycor() > BOTTOM_WALL:
            new_y = self.paddle_block.ycor() - 20
            self.paddle_block.sety(new_y)
            print("Moved paddle down")  # Print paddle movement


# Ball class
class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        print("Ball created")  # Print ball creation

        # Additional ball logic for movement and collision
        self.ball.dx = 0.2
        self.ball.dy = 0.2
        self.ball.setposition(0, 0)

    def move(self):
        new_x = self.ball.xcor() + self.ball.dx
        new_y = self.ball.ycor() + self.ball.dy
        self.ball.goto(new_x, new_y)
