from turtle import Screen
from turtle import Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


def draw_wall():
    wall = Turtle()
    wall.hideturtle()
    wall.penup()
    wall.color("white")
    wall.pensize(5)
    wall.goto(-330, -330)  # Starting point at bottom left

    # Draw the square wall
    for _ in range(4):
        wall.pendown()
        wall.forward(660)  # Length of wall
        wall.left(90)  # Turn left to draw the next side


# Call the function to draw the wall
draw_wall()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (
        snake.head.xcor() > 325
        or snake.head.xcor() < -325
        or snake.head.ycor() > 325
        or snake.head.ycor() < -325
    ):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
