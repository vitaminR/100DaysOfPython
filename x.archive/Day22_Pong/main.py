# main.py
"""main module for pong game"""

from turtle import Screen, TurtleGraphicsError
from game import Game
from gear import Paddle, Ball
import time

# Initialize the screen
screen = Screen()
screen.setup(width=1400, height=900)
screen.bgcolor("black")
screen.title("Pong")


# Function to check if window is closed
def window_closed(screen):
    try:
        screen.getcanvas()
        return False
    except TurtleGraphicsError:
        return True


# Main function to run the game
def main():
    # Create paddles and ball
    left_paddle = Paddle(screen, "left", "w", "s")
    right_paddle = Paddle(screen, "right", "Up", "Down")
    ball = Ball()

    # Set initial positions for paddles
    left_paddle.loc()
    right_paddle.loc()

    screen.listen()

    # Create a game instance
    game = Game(left_paddle, right_paddle, ball)

    # Start the game
    game.start()
    print("Game started")  # Print statement to indicate game start

    while game.is_game_on and not window_closed(screen):
        left_paddle.paddle_move()

        right_paddle.paddle_move()

        game.play_game()
        screen.update()
        time.sleep(0.1)  # Small delay for better event processing

    # End the game
    screen.exitonclick()


if __name__ == "__main__":
    main()
