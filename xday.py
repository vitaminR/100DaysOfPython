from turtle import Turtle, Screen
import random
import math

# screen
screen = Screen()
screen.setup(1100, 1100)
screen.bgcolor("black")

# Move the window to the left side of the screen
root = screen.getcanvas().winfo_toplevel()
root.geometry("+0+0")

# Bryan Brinkman's color palette
color_list_with_names = [
    ("Pinkish", "#f2668b", (242, 102, 139)),
    ("Light Blue", "#23c7d9", (35, 199, 217)),
    ("Mint Green", "#48d9a4", (72, 217, 164)),
    ("Sunflower Yellow", "#f2bf27", (242, 191, 39)),
    ("Off White", "#f2f1df", (242, 241, 223)),
]

# Slightly varied color palette
varied_colors = [
    ("Light Pinkish", "#f2889b"),
    ("Lighter Blue", "#33d7e9"),
    ("Light Mint Green", "#58e9b4"),
    ("Light Sunflower Yellow", "#f2cf37"),
    ("Light Off White", "#f2f1ef"),
]


# player
player = Turtle()
player.shape("turtle")
player.pensize(3)
player.speed(0)
screen.tracer(1, 0)
player.color("white")


player = Turtle()
player.speed(0)  # Set the speed to the maximum
player.color("white")

# Draw a spiral of stars
for i in range(206):  # This loop creates 206 stars
    player.penup()
    player.goto(
        (i * 2) * math.cos(i * 5 * math.pi / 180),
        (i * 2) * math.sin(i * 5 * math.pi / 180),
    )  # Move the player in a spiral
    player.pendown()
    player.color(
        random.choice(color_list_with_names)[1]
    )  # Select a random color for each star
    for _ in range(5):  # This loop creates the inner star
        player.forward(i / 2 + 15)  # The size of the stars increases for each star
        player.right(144)  # Rotate the player to create a star shape
    player.right(222.492235)  # Rotate the player by the golden angle after each star


# Set the function to be called when you click on the screen
Screen().exitonclick()

# # Draw a star of stars
# for _ in range(36):  # This loop creates the outer star
#     player.penup()
#     player.forward(100)  # Move the turtle to a new position
#     player.pendown()
#     player.color(
#         random.choice(color_list_with_names)[1]
#     )  # Select a random color for each star
#     for _ in range(5):  # This loop creates the inner star
#         player.forward(100)
#         player.right(144)  # Rotate the turtle to create a star shape
#     player.penup()
#     player.backward(100)  # Move the turtle back to the center
#     player.right(10)  # Rotate the turtle slightly after each star
#     player.pendown()

# # Set the function to be called when you click on the screen
# screen.exitonclick()


# # Draw a circle of circles
# for _ in range(36):  # This loop creates the outer circle
#     player.penup()
#     player.forward(200)  # Move the turtle to a new position
#     player.pendown()
#     for _ in range(10):  # This loop creates the inner circle of circles
#         player.color(random.choice(color_list_with_names)[1])
#         player.circle(50)  # Reduced the radius to make the pattern fit on the screen
#         player.right(36)  # Rotate the turtle slightly after each circle
#     player.penup()
#     player.backward(200)  # Move the turtle back to the center
#     player.right(10)  # Rotate the turtle slightly after each circle of circles
#     player.pendown()

# Set the function to be called when you click on the screen
# screen.exitonclick()
