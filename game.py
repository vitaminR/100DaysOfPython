from snake import Snake
from food import Food


class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        # Update the game state here
        pass

    def is_game_over(self):
        # Check for game over conditions here
        return False
