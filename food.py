import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.move_to_new_location()
        self.refresh()

    def move_to_new_location(self):
        """Move the food to a new random location on the screen."""
        random_x = random.randint(-560, 560)
        random_y = random.randint(-410, 410)
        self.goto(random_x, random_y)

    def refresh(self):
        """Refresh the food by moving it to a new location."""
        self.move_to_new_location()
