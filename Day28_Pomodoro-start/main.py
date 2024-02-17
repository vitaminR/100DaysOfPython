# ===========================================
# 1. IMPORTS
# ===========================================

from tkinter import *

# ===========================================
# 2. CONSTANTS
# ===========================================

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#c0c0c0"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
fg = GREEN
CHECKMARK = "✔"

# -----------------------------------------
# 2a. Grid Line Color Constant
# -----------------------------------------

# Change to YELLOW or "lightgrey" to toggle grid line visibility
GRID_LINE_COLOR = GREY


# ===========================================
# 3. UI SETUP
# ===========================================

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# -----------------------------------------
# 3a. Configure Grid Layout
# -----------------------------------------

# Configure grid layout for equal column and row distribution
for i in range(3):  # 3 columns
    window.grid_columnconfigure(
        i, weight=1, minsize=50
    )  # Ensure columns have a minimum size
for i in range(5):  # 5 rows
    window.grid_rowconfigure(i, weight=1, minsize=20)  # Ensure rows have a minimum size

# -----------------------------------------
# 3b. Create Grid Lines
# -----------------------------------------

# Optionally create grid lines based on the color setting
for i in range(3):  # Column iteration
    for j in range(5):  # Row iteration
        if (
            GRID_LINE_COLOR != YELLOW
        ):  # Only add grid lines if color is not set to background color
            cell_frame = Frame(
                window, highlightcolor=GRID_LINE_COLOR, highlightthickness=1, bd=0
            )
            cell_frame.grid(row=j, column=i, sticky="nsew", padx=1, pady=1)
        else:  # Create an empty frame to maintain grid structure without visible lines
            Frame(window, bg=YELLOW).grid(
                row=j, column=i, sticky="nsew", padx=1, pady=1
            )

# -----------------------------------------
# 3c. Create Canvas
# -----------------------------------------

# Canvas for tomato image and timer text
canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # Ensure the file exists
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="black", font=(FONT_NAME, 15, "bold")
)
canvas.grid(row=2, column=1)  # Center placement in the grid

# -----------------------------------------
# 3d. Button Click Handlers
# -----------------------------------------


def on_start_click():
    print("Start button clicked!")


def on_reset_click():
    print("Reset button clicked!")


# -----------------------------------------
# 3e. Create Start Button
# -----------------------------------------

# Create the start button
start_button = Button(
    window,
    text="Start",
    command=on_start_click,
    bg=GREY,
    activebackground=GREY,
    bd=2,
    relief="groove",
)
start_button.grid(row=3, column=0)

# -----------------------------------------
# 3f. Create Reset Button
# -----------------------------------------

# Create the reset button
reset_button = Button(
    window,
    text="Reset",
    command=on_reset_click,
    bg=GREY,
    activebackground=GREY,
    bd=2,
    relief="groove",
)
reset_button.grid(row=3, column=2)

# ===========================================
# 4. MAIN LOOP
# ===========================================

window.mainloop()
