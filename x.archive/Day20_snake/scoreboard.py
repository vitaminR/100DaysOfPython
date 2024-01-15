# scoreboard.py
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Scoreboard class for the Snake game. Manages the display of the player's score.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates and displays the current score on the screen.
        """
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """
        Increases the score by 1 and updates the scoreboard.
        """
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Displays the 'Game Over' message.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
