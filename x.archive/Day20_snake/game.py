# game.py
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen


class Game:
    """
    Game class for the Snake game. Orchestrates the game loop and interactions
    between game components (snake, foods, scoreboard).
    """

    def __init__(self, screen, wall_width, wall_height):
        self.screen = screen
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.snake = Snake(screen.window_width(), screen.window_height())
        self.foods = [Food() for _ in range(3)]  # Handling multiple Food instances
        self.scoreboard = Scoreboard()
        self.is_game_on = False
        self.setup_controls()

    def setup_controls(self):
        """
        Configures keyboard controls for the game.
        """
        self.screen.listen()
        self.screen.onkey(lambda: self.snake.change_direction("up"), "Up")
        self.screen.onkey(lambda: self.snake.change_direction("down"), "Down")
        self.screen.onkey(lambda: self.snake.change_direction("left"), "Left")
        self.screen.onkey(lambda: self.snake.change_direction("right"), "Right")

    def play_game(self):
        """
        Starts and runs the main game loop.
        """
        self.is_game_on = True
        while self.is_game_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            for food in self.foods:  # Check collision with each food instance
                if self.snake.detect_collision_with_food(food):
                    food.refresh()
                    self.snake.extend(food.get_color())
                    self.scoreboard.increase_score()

            if (
                self.snake.detect_collision_with_wall()
                or self.snake.detect_collision_with_tail()
            ):
                self.is_game_on = False
                self.scoreboard.game_over()

    def start(self):
        """
        Initiates the game.
        """
        self.play_game()
        self.screen.exitonclick()
