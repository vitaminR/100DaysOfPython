import time
from tkinter import *
import os
import openai

CHECKMARK = "✔"

YELLOW = "#f7f5dd"
GREEN = "#5c9a8f"
RED = "#e7305b"
PINK = "#e2979c"
FONT_NAME = "Courier"
NORMAL_BG = "white"
NORMAL_FG = "black"

themes = {
    "Dark": {"bg": "black", "fg": "green"},
    "Colorful": {"bg": YELLOW, "fg": RED},
    "Normal": {"bg": NORMAL_BG, "fg": NORMAL_FG},
}

openai.api_key = os.getenv("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")

# -----------------------------------------
# 1a. Timer Variables
# -----------------------------------------
timer = None
work_sessions = 0

# ===========================================
# 2. UI SETUP
# ===========================================
window = Tk()
window.title("Pomodoro + GPT Assistant")
window.config(padx=100, pady=50, bg=YELLOW)

# Define your labels and entries here
work_min_label = Label(window, text="Work Duration (min)", bg=YELLOW)
work_min_label.grid(column=0, row=4, pady=(10, 0))

work_min_entry = Entry(window, width=5)
work_min_entry.insert(END, "25")  # Default value
work_min_entry.grid(column=0, row=5)

short_break_min_label = Label(window, text="Short Break Duration (min)", bg=YELLOW)
short_break_min_label.grid(column=1, row=4, pady=(10, 0))

short_break_min_entry = Entry(window, width=5)
short_break_min_entry.insert(END, "5")  # Default value
short_break_min_entry.grid(column=1, row=5)

long_break_min_label = Label(window, text="Long Break Duration (min)", bg=YELLOW)
long_break_min_label.grid(column=2, row=4, pady=(10, 0))

long_break_min_entry = Entry(window, width=5)
long_break_min_entry.insert(END, "15")  # Default value
long_break_min_entry.grid(column=2, row=5)

themes = {
    "Dark": {"bg": "black", "fg": "green"},
    "Colorful": {"bg": "white", "fg": "magenta"},
}

current_theme = StringVar(window)
current_theme.set("Dark")  # default value

theme_option_menu = OptionMenu(window, current_theme, *themes.keys())
theme_option_menu.grid(column=0, row=0)

canvas = Canvas(width=200, height=224, bg=NORMAL_BG, highlightthickness=0)
tomato_img = PhotoImage(
    file="tomato.png"
)  # Make sure the path to your image is correct
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=NORMAL_BG, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmarks_label = Label(fg=GREEN, bg=NORMAL_BG)
checkmarks_label.grid(column=1, row=3)


# ===========================================
# GPT-3.5-turbo Integration
# ===========================================
gpt_query_entry = Entry(window, width=50)
gpt_query_entry.grid(column=0, row=10, pady=(10, 0))

gpt_response_label = Label(window, text="", bg=YELLOW, wraplength=400)
gpt_response_label.grid(column=0, row=11, pady=(10, 0))


def ask_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another suitable GPT-3 model
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    except openai.error.APIError as e:  # Handle specific OpenAI errors
        return f"Error: {e}"


def handle_gpt_query():
    user_prompt = gpt_query_entry.get()
    gpt_response = ask_gpt(user_prompt)
    gpt_response_label.config(text=gpt_response)


gpt_query_button = Button(window, text="Ask GPT", command=handle_gpt_query)
gpt_query_button.grid(column=1, row=10)


# ===========================================
# 3. TIMER MECHANISM
# ===========================================
def start_timer():
    global work_sessions
    work_sessions += 1

    work_min = int(work_min_entry.get())
    short_break_min = int(short_break_min_entry.get())
    long_break_min = int(long_break_min_entry.get())
    if work_sessions % 8 == 0:
        count_down(long_break_min * 60)
        timer_label.config(text="Break", fg=RED)
    elif work_sessions % 2 == 0:
        count_down(short_break_min * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_min * 60)
        timer_label.config(text="Work", fg=GREEN)


# ===========================================
# 4. COUNTDOWN MECHANISM
# ===========================================
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(work_sessions // 2):
            marks += CHECKMARK
        checkmarks_label.config(text=marks)


# ===========================================
# 5. RESET TIMER
# ===========================================
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    global work_sessions
    work_sessions = 0


# ===========================================
# 6. BUTTONS
# ===========================================
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# Bind the Enter key to the handle_gpt_query function
window.bind("<Return>", lambda event=None: handle_gpt_query())

# Move the GPT entry, button, and response label to the right by updating their column index in the grid method
gpt_query_entry.grid(column=1, row=10, pady=(10, 0))  # Moved to column 1 from 0
gpt_query_button.grid(column=2, row=10)  # Moved to column 2 from 1
gpt_response_label.grid(
    column=1, row=11, columnspan=2, pady=(10, 0)
)  # Expanded to span 2 columns


def apply_theme():
    theme = themes[current_theme.get()]
    window.config(bg=theme["bg"])
    timer_label.config(fg=theme["fg"], bg=theme["bg"])
    checkmarks_label.config(fg=theme["fg"], bg=theme["bg"])
    work_min_label.config(bg=theme["bg"], fg=theme["fg"])
    short_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    long_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    gpt_response_label.config(bg=theme["bg"], fg=theme["fg"])
    canvas.config(bg=theme["bg"])  # Change the background color of the canvas
    # Add other UI elements that you want to change the color of


# Call apply_theme whenever the selected theme changes
current_theme.trace("w", lambda *args: apply_theme())

window.mainloop()

# -----------------------------------------
# 1a. Timer Variables
# -----------------------------------------
timer = None
work_sessions = 0

# ===========================================
# 2. UI SETUP
# ===========================================
window = Tk()
window.title("Pomodoro + GPT Assistant")
window.config(padx=100, pady=50, bg=YELLOW)

# Define your labels and entries here
work_min_label = Label(window, text="Work Duration (min)", bg=YELLOW)
work_min_label.grid(column=0, row=4, pady=(10, 0))

work_min_entry = Entry(window, width=5)
work_min_entry.insert(END, "25")  # Default value
work_min_entry.grid(column=0, row=5)

short_break_min_label = Label(window, text="Short Break Duration (min)", bg=YELLOW)
short_break_min_label.grid(column=1, row=4, pady=(10, 0))

short_break_min_entry = Entry(window, width=5)
short_break_min_entry.insert(END, "5")  # Default value
short_break_min_entry.grid(column=1, row=5)

long_break_min_label = Label(window, text="Long Break Duration (min)", bg=YELLOW)
long_break_min_label.grid(column=2, row=4, pady=(10, 0))

long_break_min_entry = Entry(window, width=5)
long_break_min_entry.insert(END, "15")  # Default value
long_break_min_entry.grid(column=2, row=5)

themes = {
    "Dark": {"bg": "black", "fg": "green"},
    "Colorful": {"bg": "white", "fg": "magenta"},
}

current_theme = StringVar(window)
current_theme.set("Dark")  # default value

theme_option_menu = OptionMenu(window, current_theme, *themes.keys())
theme_option_menu.grid(column=0, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(
    file="tomato.png"
)  # Make sure the path to your image is correct
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

checkmarks_label = Label(fg=GREEN, bg=YELLOW)
checkmarks_label.grid(column=1, row=3)

# ===========================================
# GPT-3.5-turbo Integration
# ===========================================
gpt_query_entry = Entry(window, width=50)
gpt_query_entry.grid(column=0, row=10, pady=(10, 0))

gpt_response_label = Label(window, text="", bg=YELLOW, wraplength=400)
gpt_response_label.grid(column=0, row=11, pady=(10, 0))


def ask_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or another suitable GPT-3 model
            prompt=prompt,
            temperature=0.7,
            max_tokens=150,
        )
        return response.choices[0].text.strip()
    except openai.error.APIError as e:  # Handle specific OpenAI errors
        return f"Error: {e}"


def handle_gpt_query():
    user_prompt = gpt_query_entry.get()
    gpt_response = ask_gpt(user_prompt)
    gpt_response_label.config(text=gpt_response)


gpt_query_button = Button(window, text="Ask GPT", command=handle_gpt_query)
gpt_query_button.grid(column=1, row=10)


# ===========================================
# 3. TIMER MECHANISM
# ===========================================
def start_timer():
    global work_sessions
    work_sessions += 1

    work_min = int(work_min_entry.get())
    if work_sessions % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    elif work_sessions % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_min * 60)
        timer_label.config(text="Work", fg=GREEN)


# ===========================================
# 4. COUNTDOWN MECHANISM
# ===========================================
def count_down(count):
    global timer
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(work_sessions // 2):
            marks += CHECKMARK
        checkmarks_label.config(text=marks)


# ===========================================
# 5. RESET TIMER
# ===========================================
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmarks_label.config(text="")
    global work_sessions
    work_sessions = 0


# ===========================================
# 6. BUTTONS
# ===========================================
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


##other###
# Bind the Enter key to the handle_gpt_query function
window.bind("<Return>", lambda event=None: handle_gpt_query())

# Move the GPT entry, button, and response label to the right by updating their column index in the grid method
gpt_query_entry.grid(column=1, row=10, pady=(10, 0))  # Moved to column 1 from 0
gpt_query_button.grid(column=2, row=10)  # Moved to column 2 from 1
gpt_response_label.grid(
    column=1, row=11, columnspan=2, pady=(10, 0)
)  # Expanded to span 2 columns


def apply_theme():
    theme = themes[current_theme.get()]
    window.config(bg=theme["bg"])
    timer_label.config(fg=theme["fg"])
    checkmarks_label.config(fg=theme["fg"])
    work_min_label.config(bg=theme["bg"], fg=theme["fg"])
    short_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    long_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    gpt_response_label.config(bg=theme["bg"], fg=theme["fg"])
    # Add other UI elements that you want to change the color of


# Call apply_theme whenever the selected theme changes
current_theme.trace("w", lambda *args: apply_theme())

window.mainloop()
