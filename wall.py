# wall.py

import turtle


def create_wall(turtle_window_width, turtle_window_height):
    # Create a new turtle to draw the walls
    wall_turtle = turtle.Turtle()
    wall_turtle.hideturtle()
    wall_turtle.penup()
    wall_turtle.color("white")

    # Turn off the turtle's animation
    turtle.Screen().tracer(0)

    # Adjust the size of the wall to be slightly smaller than the screen
    wall_width = turtle_window_width - 20
    wall_height = turtle_window_height - 20

    # Draw the top wall
    wall_turtle.goto(-wall_width / 2, wall_height / 2)
    wall_turtle.pendown()
    wall_turtle.forward(wall_width)
    wall_turtle.penup()

    # Draw the right wall
    wall_turtle.goto(wall_width / 2, wall_height / 2)
    wall_turtle.right(90)
    wall_turtle.pendown()
    wall_turtle.forward(wall_height)
    wall_turtle.penup()

    # Draw the bottom wall
    wall_turtle.goto(wall_width / 2, -wall_height / 2)
    wall_turtle.right(90)
    wall_turtle.pendown()
    wall_turtle.forward(wall_width)
    wall_turtle.penup()

    # Draw the left wall
    wall_turtle.goto(-wall_width / 2, -wall_height / 2)
    wall_turtle.right(90)
    wall_turtle.pendown()
    wall_turtle.forward(wall_height)
    wall_turtle.penup()

    # Turn the turtle's animation back on
    turtle.Screen().tracer(1)
    turtle.Screen().update()

    return wall_width, wall_height
