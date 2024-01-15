# food.py
import random
from turtle import Turtle
from art import COLORS


class Food(Turtle):
    """
    Food class for the Snake game. Handles the food's appearance,
    placement, and color changes in the game.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(list(COLORS.values())))
        self.speed("fastest")
        self.refresh()

    def move_to_new_location(self):
        """
        Move the food to a new random location on the screen.
        """
        random_x = random.randint(
            -280, 280
        )  # Adjusted to a smaller range for default screen size
        random_y = random.randint(
            -280, 280
        )  # Adjusted to a smaller range for default screen size
        self.goto(random_x, random_y)

    def refresh(self):
        """
        Refresh the food by moving it to a new location and changing its color.
        """
        self.move_to_new_location()
        self.color(random.choice(list(COLORS.values())))

    def get_color(self):
        """
        Return the current color of the food.
        """
        return self.fillcolor()
