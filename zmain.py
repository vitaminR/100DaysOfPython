"""main module for the Snake Game"""
from turtle import Screen
import time
from game import Game
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def main():
    # Set up the screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=1200, height=1200)
    screen.title("Snake Game")
    screen.tracer(0)

    # Create
    snake = Snake()
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

        snake.move()

        # Detect collision with food
        if snake.detect_collision_with_food(food):
            food.refresh()
            snake.extend()
            game.scoreboard.increase_score()

        # Detect collision with wall
        if snake.detect_collision_with_wall():
            game.is_on = False
            game.scoreboard.game_over()

        # Detect collision with tail
        if snake.detect_collision_with_tail():
            game.is_on = False
            game.scoreboard.game_over()

    # Keep the window open until it's clicked
    screen.exitonclick()


if __name__ == "__main__":
    main()
