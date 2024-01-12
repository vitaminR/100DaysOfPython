from turtle import Turtle, Screen
import random


# Function to generate a random neon color within a range
def generate_neon_color_custom():
    # Define custom RGB ranges for neon colors
    custom_ranges = {
        "pink": {"red": (200, 255), "green": (20, 60), "blue": (100, 255)},
        "blue": {"red": (0, 50), "green": (100, 200), "blue": (180, 255)},
        "yellow": {"red": (190, 255), "green": (180, 255), "blue": (0, 70)},
        "green": {"red": (0, 80), "green": (190, 255), "blue": (0, 130)},
        "orange": {"red": (255, 255), "green": (100, 140), "blue": (0, 50)},
        "light_blue": {"red": (0, 100), "green": (180, 255), "blue": (200, 255)},
    }

    # Randomly choose a color range to generate a color from
    color_choice = random.choice(list(custom_ranges.keys()))
    ranges = custom_ranges[color_choice]

    # Generate a random color within the selected range
    red = random.randint(*ranges["red"])
    green = random.randint(*ranges["green"])
    blue = random.randint(*ranges["blue"])

    # Return the color in hexadecimal format
    return f"#{red:02X}{green:02X}{blue:02X}"


# Function to generate a lighter version of the neon color for the glow effect
def generate_lighter_neon_color(base_color):
    # Parse the base color and increase each color component to make it lighter
    red = min(int(base_color[1:3], 16) + 60, 255)
    green = min(int(base_color[3:5], 16) + 60, 255)
    blue = min(int(base_color[5:], 16) + 60, 255)
    return f"#{red:02X}{green:02X}{blue:02X}"


# Function to draw a smoother glowing line
def draw_smooth_glowing_line(player, length, base_color):
    # Set the glow effect
    glow_color = generate_lighter_neon_color(
        base_color
    )  # Define and assign a value to 'glow_color'
    player.width(10)  # Increase the pen width for the glow effect
    player.color(glow_color)

    # Draw the glowing line with segments
    for _ in range(int(length / 2)):  # More segments for a smoother line
        player.forward(2)  # Short segments
        player.right(random.uniform(-1.0, 1.0))  # Slight random angle change

    # Go back to the start of the line and draw the main line on top of the glow
    player.penup()
    player.backward(length)
    player.pendown()
    player.width(3)  # Reset the pen width for the main shape
    player.color(base_color)
    for _ in range(int(length / 2)):
        player.forward(2)
        player.right(random.uniform(-1.0, 1.0))


# Setup the screen
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
# Tracer set to 0 for no animation
screen.tracer(0)

# Move the window to the left side of the screen
root = screen.getcanvas().winfo_toplevel()
root.geometry("+0+0")

# Player setup
player = Turtle()
# Set the drawing speed to a slower pace
player.speed(3)

# Margin from the edge of the screen
margin = 20

# Draw random smoother glowing lines
for _ in range(50):  # Draw 50 random lines
    player.penup()
    # Move to a random starting point within a small overflow from the edge
    start_x = random.randint(
        -screen.window_width() // 2 + margin, screen.window_width() // 2 - margin
    )
    start_y = random.randint(
        -screen.window_height() // 2 + margin, screen.window_height() // 2 - margin
    )
    player.goto(start_x, start_y)
    player.pendown()

    # Set a random direction
    player.setheading(random.randint(0, 360))

    # Set a random length a bit shorter, between 30 and 100
    line_length = random.randint(30, 100)

    # Generate a random neon color for the line
    base_color = generate_neon_color_custom()

    # Draw the smoother glowing line
    draw_smooth_glowing_line(player, line_length, base_color)

    # Update the screen after each line is drawn
    screen.update()

screen.exitonclick()
