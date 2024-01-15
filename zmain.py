# main.py
from turtle import Screen, TurtleGraphicsError
from zgame import Game


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

    game = Game()

    game.start()

    while game.is_game_on and not window_closed(screen):
        game.play_game()

    screen.exitonclick()


if __name__ == "__main__":
    main()
