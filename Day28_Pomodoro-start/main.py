import time
from tkinter import *

# ===========================================
# 1. CONSTANTS
# ===========================================

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#c0c0c0"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 45
CHECKMARK = "✔"  # Add this lineb'

# -----------------------------------------
# 1a. Timer Variables
# -----------------------------------------


timer = None
work_sessions = 0


def start_timer():
    global timer
    global work_sessions

    # If timer is running, cancel it before starting a new one
    if timer:
        window.after_cancel(timer)  # Aligned with comment on timer variable
        timer = None

    work_sessions += 1  # Increment the session count

    # Determine the type of session and its duration
    if work_sessions % 8 == 0:  # Every 8th session is a long break
        count_down(LONG_BREAK_MIN * 60)
    elif work_sessions % 2 == 0:  # Even sessions (excluding the 8th) are short breaks
        count_down(SHORT_BREAK_MIN * 60)
    else:  # Odd sessions are work periods
        count_down(WORK_MIN * 60)


def count_down(count):
    count_min = count // 60  # Comment 6: Calculate minutes
    count_sec = count % 60  # Comment 7: Calculate seconds
    canvas.itemconfig(
        timer_text, text=f"{count_min:02d}:{count_sec:02d}"
    )  # Comment 8: Update UI with remaining time
    if count > 0:
        global timer
        timer = window.after(
            1000, count_down, count - 1
        )  # Comment 9: Schedule the next countdown call
    else:
        start_timer()  # Comment 10: Auto-start the next session


# -----------------------------------------
# 1b. Leg Checkmark Panel Variables
# -----------------------------------------

leg_checkmark_panel = None
leg_checkmark_labels = []

# ===========================================
# 2. UI SETUP
# ===========================================

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# -----------------------------------------
# 2a. Configure Grid Layout
# -----------------------------------------

# Configure the grid layout for equal column and row distribution
for i in range(3):  # 3 columns
    window.grid_columnconfigure(
        i, weight=1, minsize=50
    )  # Ensure columns have a minimum size
for i in range(8):  # 8 rows
    window.grid_rowconfigure(i, weight=1, minsize=20)  # Ensure rows have a minimum size

# -----------------------------------------
# 2b. Create Leg Checkmark Panel
# -----------------------------------------

leg_checkmark_panel = Frame(window, bg=GREEN)
leg_checkmark_panel.grid(row=7, column=0, columnspan=3)

# Create the leg checkmark labels with their text, background color, foreground color, and font
for i in range(4):
    checkmark_label = Label(
        leg_checkmark_panel,
        text=CHECKMARK,
        bg=GREEN,
        fg="white",
        font=(FONT_NAME, 15, "bold"),
    )
    leg_checkmark_labels.append(checkmark_label)
    checkmark_label.grid(row=0, column=i)

# Initially hide the leg checkmark labels
for label in leg_checkmark_labels:
    label.grid_remove()

# -----------------------------------------
# 2c. Create Canvas
# -----------------------------------------

# Create a canvas for displaying the tomato image and timer text
canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load the tomato image file
tomato_img = PhotoImage(file="tomato.png")  # Ensure the image file exists

# Create an image object on the canvas at the center
canvas.create_image(100, 112, image=tomato_img)

# Create a text object on the canvas for displaying the timer
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="black", font=(FONT_NAME, 15, "bold")
)

# Place the canvas in the grid at row 2, column 1
canvas.grid(row=2, column=1)  # Center placement in the grid

# -----------------------------------------
# 2d. Create Timer Label
# -----------------------------------------

timer_label = Label(
    window, text="Timer", bg=GREEN, fg="white", font=(FONT_NAME, 24, "bold")
)
timer_label.grid(row=0, column=1, columnspan=2)


# ===========================================
# 3. FUNCTIONS
# ===========================================

# -----------------------------------------
# 3a. Reset Timer
# -----------------------------------------


def reset_timer():
    global timer
    if timer:
        window.after_cancel(timer)  # Comment 11: Cancel the ongoing timer
        timer = None
    canvas.itemconfig(timer_text, text="00:00")  # Comment 12: Reset timer text to 00:00
    global work_sessions
    work_sessions = 0  # Comment 13: Reset work session counter
    # Additional UI reset actions as necessary


# -----------------------------------------
# 3b. Start Timer
# -----------------------------------------


def start_timer():
    global timer  # Add this line
    global work_sessions

    # Reset the timer if it's already running
    if timer:
        reset_timer()

    # Increment the work sessions counter
    work_sessions += 1

    # Calculate the total number of minutes for the current session
    if work_sessions % 8 == 0:  # Long break
        minutes = LONG_BREAK_MIN
    elif work_sessions % 2 == 0:  # Short break
        minutes = SHORT_BREAK_MIN
    else:  # Work session
        minutes = WORK_MIN

    # Convert minutes to seconds
    seconds = minutes * 60

    # Create a countdown timer
    timer = window.after(seconds * 1000, countdown)


# -----------------------------------------
# 3c. Countdown
# -----------------------------------------


def countdown():
    global work_sessions

    # Get the current time in seconds
    current_seconds = time.time()

    # Calculate the remaining seconds
    remaining_seconds = timer - current_seconds

    # Convert the remaining seconds to minutes and seconds
    remaining_minutes = remaining_seconds // 60
    remaining_seconds = remaining_seconds % 60

    # Update the timer text
    canvas.itemconfig(
        timer_text, text=f"{remaining_minutes:02d}:{remaining_seconds:02d}"
    )

    # Check if the timer has reached 00:00
    if remaining_seconds == 0 and remaining_minutes == 0:
        # Stop the timer
        timer.cancel()

        # Show the leg checkmark label for the completed work session
        leg_checkmark_labels[work_sessions - 1].grid()

        # If all 4 work sessions are complete, reset the timer
        if work_sessions == 4:
            reset_timer()
        else:
            # Start the next timer
            start_timer()
    else:
        # Create a new countdown timer
        timer = window.after(1000, countdown)


# ===========================================
# 4. BUTTONS
# ===========================================

# -----------------------------------------
# 4a. Start Button
# -----------------------------------------

start_button = Button(
    window,
    text="Start",
    command=start_timer,
    bg=GREY,
    activebackground=GREY,
    bd=2,
    relief="groove",
)
start_button.grid(row=6, column=0)

# -----------------------------------------
# 4b. Reset Button
# -----------------------------------------

reset_button = Button(
    window,
    text="Reset",
    command=reset_timer,
    bg=GREY,
    activebackground=GREY,
    bd=2,
    relief="groove",
)
reset_button.grid(row=6, column=2)


# ===========================================
# 5. MAIN LOOP
# ===========================================

window.mainloop()
