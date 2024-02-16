from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
fg = GREEN

# Variable to control the grid line color
GRID_LINE_COLOR = (
    YELLOW  # Change to "lightgrey" for visible lines or YELLOW for "transparent"
)


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# Configure grid layout for equal column and row distribution
for i in range(3):  # 3 columns
    window.grid_columnconfigure(i, weight=1, uniform="fred")
for i in range(5):  # 5 rows
    window.grid_rowconfigure(i, weight=1, uniform="fred")

# Create cells with configurable borders to simulate grid lines or make them "transparent"
for i in range(3):  # for each column
    for j in range(5):  # for each row
        cell_frame = Frame(
            window,
            highlightbackground=GRID_LINE_COLOR,
            highlightcolor=GRID_LINE_COLOR,
            highlightthickness=1,
            bd=0,
        )
        cell_frame.grid(row=j, column=i, sticky="nsew", padx=0.5, pady=0.5)

# Canvas for tomato image and timer text
canvas = Canvas(window, width=100, height=100, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="tomato.png"
)  # Ensure tomato.png is in the correct directory
canvas.create_image(50, 50, image=tomato_img)
timer_text = canvas.create_text(
    50, 65, text="00:00", fill="black", font=(FONT_NAME, 15, "bold")
)
canvas.grid(row=2, column=1)  # Center placement in the grid

window.mainloop()
