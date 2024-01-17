from turtle import Turtle, Screen


class Player(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(x, y)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def reset(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.tracer(0)

    player = Player(0, -280)

    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")

    while True:
        screen.update()


if __name__ == "__main__":
    main()
