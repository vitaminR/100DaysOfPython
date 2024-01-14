from turtle import Screen
import time


class Game:
    def __init__(self, snake, food, scoreboard):
        self.screen = Screen()
        self.snake = snake
        self.food = food
        self.scoreboard = scoreboard
        self.is_game_on = False

    def start_game(self):
        while self.screen.window_is_open():  # Check if the window is open
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()

            # Detect collision with food
            if self.snake.detect_collision_with_food(self.food):
                food_color = self.food.get_color()
                self.food.refresh()
                self.snake.extend(food_color)
                self.scoreboard.increase_score()

            # Detect collision with wall
            if self.snake.detect_collision_with_wall():
                self.is_game_on = False
                self.scoreboard.game_over()

            # Detect collision with tail
            if self.snake.detect_collision_with_tail():
                self.is_game_on = False
                self.scoreboard.game_over()

    def play_game(self):
        self.screen.listen()
        self.screen.onkey(self.snake.go_up, "Up")
        self.screen.onkey(self.snake.go_down, "Down")
        self.screen.onkey(self.snake.go_left, "Left")
        self.screen.onkey(self.snake.go_right, "Right")
        self.start_game()
        self.screen.mainloop()
