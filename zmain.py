"""main module for the Snake Game"""
import tkinter as tk
from turtle import Screen, Terminator
import time
from game import Game
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import create_wall


def CustomScreen():
    screen = Screen()

    def window_is_open():
        try:
            screen.getcanvas()
            return True
        except Terminator:
            return False

    screen.window_is_open = window_is_open
    return screen


def main():
    # Create the turtle screen
    screen = CustomScreen()

    screen.bgcolor("black")

    # Get the size of the monitor
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position of the turtle window
    turtle_window_width = 1200  # replace with the width of your turtle window
    turtle_window_height = 900  # replace with the height of your turtle window
    position_x = (screen_width - turtle_window_width) // 2
    position_y = (screen_height - turtle_window_height) // 2

    # Set the position of the turtle window
    root = screen.getcanvas().winfo_toplevel()
    root.geometry(
        f"{turtle_window_width}x{turtle_window_height}+{position_x}+{position_y}"
    )

    wall_width, wall_height = create_wall(turtle_window_width, turtle_window_height)

    # Create the snake
    snake = Snake(wall_width, wall_height)

    # Create the food
    food = Food()
    scoreboard = Scoreboard()
    game = Game(snake, food, scoreboard)

    # Set up key bindings for snake movement
    screen.listen()
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_up, "w")
    screen.onkey(snake.go_down, "Down")
    screen.onkey(snake.go_down, "s")
    screen.onkey(snake.go_left, "Left")
    screen.onkey(snake.go_left, "a")
    screen.onkey(snake.go_right, "Right")
    screen.onkey(snake.go_right, "d")

    game.start_game()

    # Start the game loop
    while game.is_game_on:
        screen.update()
        time.sleep(0.1)

        if game.is_game_on:
            snake.move()

        # Detect collision with food
        if snake.detect_collision_with_food(food):
            food.refresh()
            snake.extend()
            game.scoreboard.increase_score()

        # Detect collision with wall
        if snake.detect_collision_with_wall():
            game.is_game_on = False
            game.scoreboard.game_over()
            snake.stop()

        # Detect collision with tail
        if snake.detect_collision_with_tail():
            game.is_game_on = False
            game.scoreboard.game_over()
            snake.stop()

    # Keep the window open until it's clicked
    screen.exitonclick()


if __name__ == "__main__":
    main()
