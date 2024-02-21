import time
from tkinter import *
import os


# ===========================================
# 1. CONSTANTS
# ===========================================

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#c0c0c0"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
CHECKMARK = "✔"

# -----------------------------------------
# 1a. Timer Variables
# -----------------------------------------

timer = None
work_sessions = 0

# ===========================================
# 2. UI SETUP
# ===========================================

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmarks_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
checkmarks_label.grid(column=1, row=3)
# ===========================================
# 3. FUNCTIONS
# ===========================================

# -----------------------------------------
# 3a. Count Down
# -----------------------------------------


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Play sound when timer reaches zero
        os.system("aplay beep.wav")
        start_timer()


# -----------------------------------------
# 3b. Start Timer
# -----------------------------------------


def start_timer():
    global timer
    global work_sessions

    if timer:
        window.after_cancel(timer)
        timer = None

    work_sessions += 1

    if work_sessions % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif work_sessions % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
        checkmarks_label.config(text=CHECKMARK * (work_sessions // 2))


# -----------------------------------------
# 3c. Reset Timer
# -----------------------------------------


def reset_timer():
    global work_sessions, timer
    if timer:
        window.after_cancel(timer)
    timer = None
    canvas.itemconfig(timer_text, text="00:00")
    work_sessions = 0
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")


# ===========================================
# 4. EVENT HANDLERS
# ===========================================

# -----------------------------------------
# 4a. Start Button Click
# -----------------------------------------


def start_button_click():
    start_timer()


# -----------------------------------------
# 4b. Reset Button Click
# -----------------------------------------


def reset_button_click():
    reset_timer()


# ===========================================
# 5. UI EVENT BINDINGS
# ===========================================

start_button = Button(text="Start", command=start_button_click, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_button_click, highlightthickness=0)
reset_button.grid(column=2, row=2)

# ===========================================
# 6. MAIN LOOP
# ===========================================

window.mainloop()
