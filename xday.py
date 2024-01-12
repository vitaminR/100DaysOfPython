from turtle import Turtle, Screen
import random

# screen
screen = Screen()
screen.setup(1000, 800)
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


# Function to draw a fractal spiral polygon
def draw_fractal_spiral_polygon(player, sides, size, depth):
    angle = 360 / sides
    if depth == 0:
        for _ in range(sides):
            player.forward(size)
            player.right(angle)
    else:
        for _ in range(sides):
            draw_fractal_spiral_polygon(player, sides, size / 2, depth - 1)
            player.forward(size)
            player.right(
                angle + 5
            )  # Add a slight rotation after each side to create a spiral effect


# Draw a series of interconnected fractal spiral polygons
for i in range(50):  # This loop creates 50 polygons
    sides = i % 7 + 3  # The number of sides varies from 3 to 9
    size = i * 5  # The size of the polygons increases more rapidly for each polygon
    player.penup()
    player.forward(i * 2)  # The player moves forward more for each polygon
    player.pendown()
    player.color(
        random.choice(color_list_with_names)[1]
    )  # Select a random color for each polygon
    draw_fractal_spiral_polygon(
        player, sides, size, 2
    )  # The depth of the fractal polygons is 2
    player.right(7)  # Rotate the player more after each polygon

# Draw a star of stars in a circle around the canvas
for i in range(36):  # This loop creates the outer star
    player.penup()
    player.goto(
        200 * math.cos(i * 10 * math.pi / 180), 200 * math.sin(i * 10 * math.pi / 180)
    )  # Move the player in a circle
    player.pendown()
    player.color(
        random.choice(color_list_with_names)[1]
    )  # Select a random color for each star
    for _ in range(5):  # This loop creates the inner star
        player.forward(100)
        player.right(144)  # Rotate the player to create a star shape
    player.penup()
    player.home()  # Move the player back to the center
    player.right(10)  # Rotate the player slightly after each star
    player.pendown()

# Set the function to be called when you click on the screen
turtle.Screen().exitonclick()


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
