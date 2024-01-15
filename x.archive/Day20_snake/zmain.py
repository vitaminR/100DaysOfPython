# main.py
from turtle import Screen, TurtleGraphicsError
from game import Game
from wall import create_wall  # Ensure this module exists


def window_closed(screen):
    try:
        screen.getcanvas()
        return False
    except TurtleGraphicsError:
        return True


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    turtle_window_width, turtle_window_height = (
        screen.window_width(),
        screen.window_height(),
    )
    wall_width, wall_height = create_wall(
        turtle_window_width, turtle_window_height
    )  # Adjust as needed
    game = Game(screen=screen, wall_width=wall_width, wall_height=wall_height)
    game.start()

    while game.is_game_on and not window_closed(screen):
        game.play_game()

    screen.exitonclick()


if __name__ == "__main__":
    main()
