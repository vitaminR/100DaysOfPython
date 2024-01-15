# main.py
"""main module for pong game"""
from turtle import Screen, TurtleGraphicsError
from game import Game
from gear import Paddle, Ball

screen = Screen()


def window_closed(screen):
    try:
        screen.getcanvas()
        return False
    except TurtleGraphicsError:
        return True


def main():
    screen = Screen()
    screen.setup(width=1400, height=900)
    screen.bgcolor("black")
    screen.title("Pong")

    # Create the left paddle
    left_paddle = Paddle(screen, "left", "w", "s")

    # Create the right paddle
    right_paddle = Paddle(screen, "right", "Up", "Down")

    ball = Ball()

    # Set initial positions
    left_paddle.loc()
    right_paddle.loc()

    # Create a new game
    game = Game(left_paddle, right_paddle)

    game.start()

    while game.is_game_on and not window_closed(screen):
        left_paddle.paddle_move()
        right_paddle.paddle_move()
        game.play_game()

    screen.exitonclick()


if __name__ == "__main__":
    main()
