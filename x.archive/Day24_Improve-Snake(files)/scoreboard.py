from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_score())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def read_score(self):
        try:
            with open("data.txt", "r", encoding="utf-8") as file:
                content = file.read()
                return content if content.isdigit() else "0"
        except PermissionError:
            print("Permission denied: Unable to write to data.txt")

    def write_score(self, new_high_score):
        try:
            with open("data.txt", "w", encoding="utf-8") as file:
                content = file.write(new_high_score)
                return content
        except PermissionError:
            print("Permission denied: Unable to write to data.txt")

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self):
        if self.score > self.high_score:
            self.write_score(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
