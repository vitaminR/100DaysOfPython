# from turtle import Turtle, Screen
from turtle import *
import random
import math
import time
from snake import Snake
from game import Game


def main():
    # Create a Game object
    game = Game()

    # Set up the screen
    screen = Screen()
    screen.listen()

    # Bind keys to movement functions
    screen.onkey(game.snake.go_up, "w")
    screen.onkey(game.snake.go_down, "s")
    screen.onkey(game.snake.go_left, "a")
    screen.onkey(game.snake.go_right, "d")

    # Add your game loop here
    while True:
        screen.update()
        time.sleep(0.1)
        for seg_num in range(len(game.snake.segments) - 1, 0, -1):
            new_x = game.snake.segments[seg_num - 1].xcor()
            new_y = game.snake.segments[seg_num - 1].ycor()
            game.snake.segments[seg_num].goto(new_x, new_y)
        game.snake.segments[0].forward(20)

    screen.exitonclick()


if __name__ == "__main__":
    main()
