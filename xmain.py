# from turtle import Turtle, Screen
from turtle import *
import random
import math
import time
from snake import Snake


# from xmain.py import color_list

# Screen setup


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0, 0)
# Bind keys to movement functions
screen.listen()
screen.onkey(Snake.move.go_up, "w")
screen.onkey(move.go_down, "s")
screen.onkey(move.go_left, "a")
screen.onkey(move.go_right, "d")

# Move the window to the left side of the screen
root = screen.getcanvas().winfo_toplevel()
root.geometry("+0+0")


# Main game loop
class Game:
    def __init__(self):
        self.snake = Snake()
        self.game_on = True

    def run_game(self):
        while self.game_on:
            screen.update()
            time.sleep(0.1)
            for seg_num in range(len(self.snake.segments) - 1, 0, -1):
                new_x = self.snake.segments[seg_num - 1].xcor()
                new_y = self.snake.segments[seg_num - 1].ycor()
                self.snake.segments[seg_num].goto(new_x, new_y)
            self.snake.segments[0].forward(20)


screen.exitonclick()
