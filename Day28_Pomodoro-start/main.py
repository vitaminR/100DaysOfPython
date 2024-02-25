import time
from tkinter import *
import os
import openai


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

# Define your labels and entries here
work_min_label = Label(window, text="Work Duration (min)", bg=YELLOW)
work_min_label.grid(column=0, row=4, pady=(10, 0))

work_min_entry = Entry(window, width=5)
work_min_entry.insert(END, "25")  # Default value
work_min_entry.grid(column=0, row=5)


themes = {
    "Dark": {"bg": "black", "fg": "green"},
    "Colorful": {"bg": "white", "fg": "magenta"},
}

current_theme = StringVar(window)
current_theme.set("Dark")  # default value

theme_option_menu = OptionMenu(window, current_theme, *themes.keys())
theme_option_menu.grid(column=0, row=0)


remaining_time = (
    0  # Add this line at the top of your script to declare the global variable
)


def apply_theme(*args):
    global canvas, timer_text, remaining_time
    theme = themes[current_theme.get()]
    window.config(bg=theme["bg"])
    canvas.grid_forget()  # Remove the old canvas from the grid
    canvas = Canvas(width=200, height=224, bg=theme["bg"], highlightthickness=0)
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(
        100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
    )
    canvas.grid(column=1, row=1)
    work_min_label.config(bg=theme["bg"], fg=theme["fg"])
    short_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    long_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    timer_label.config(bg=theme["bg"], fg=theme["fg"])
    checkmarks_label.config(bg=theme["bg"], fg=theme["fg"])
    # Apply the theme to other widgets...
    if (
        remaining_time > 0
    ):  # If there was a timer running, restart it with the remaining time
        count_down(remaining_time)


current_theme.trace("w", apply_theme)


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


# Short Break Duration
short_break_min_label = Label(window, text="Short Break Duration (min)", bg=YELLOW)
short_break_min_label.grid(column=1, row=4, pady=(10, 0))

short_break_min_entry = Entry(window, width=5)
short_break_min_entry.insert(END, "5")  # Default value
short_break_min_entry.grid(column=1, row=5)

# Long Break Duration
long_break_min_label = Label(window, text="Long Break Duration (min)", bg=YELLOW)
long_break_min_label.grid(column=2, row=4, pady=(10, 0))

long_break_min_entry = Entry(window, width=5)
long_break_min_entry.insert(END, "15")  # Default value
long_break_min_entry.grid(column=2, row=5)


# ===========================================
# 3. FUNCTIONS
# ===========================================

# -----------------------------------------
# 3a. Count Down
# -----------------------------------------


def count_down(count):
    global remaining_time
    remaining_time = count  # Store the remaining time
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

    # Get work and break durations from Entry fields
    WORK_MIN = int(work_min_entry.get())
    SHORT_BREAK_MIN = int(short_break_min_entry.get())
    LONG_BREAK_MIN = int(long_break_min_entry.get())

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


# -----------------------------------------
# 3d. AI
# -----------------------------------------


openai.api_key = "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"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Translate the following English text to French: '{}'",
    max_tokens=60,
)

print(response.choices[0].text.strip())


def handle_chatbot_command(command):
    if "mode=dark" in command:
        current_theme.set("dark")
        apply_theme()
    elif "mode=light" in command:
        current_theme.set("light")
        apply_theme()
    elif "minute=" in command:
        minutes = int(command.split("=")[1])
        start_timer()


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


command_entry = Entry(window, width=50)
command_entry.grid(column=0, row=6, columnspan=3)


def submit_command():
    command = command_entry.get()
    handle_chatbot_command(command)


submit_button = Button(
    text="Submit Command", command=submit_command, highlightthickness=0
)
submit_button.grid(column=0, row=7, columnspan=3)


# Update your handle_chatbot_command function
def handle_chatbot_command(command):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=command,
        max_tokens=60,
    )
    response_text = response.choices[0].text.strip()

    if "mode=dark" in response_text:
        current_theme.set("Dark")
        apply_theme()
    elif "mode=light" in response_text:
        current_theme.set("Colorful")
        apply_theme()
    elif "minute=" in response_text:
        minutes = int(response_text.split("=")[1])
        start_timer(minutes)


# ===========================================
# 6. MAIN LOOP
# ===========================================

window.mainloop()
