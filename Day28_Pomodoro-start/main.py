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

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# 1. Configure grid layout for equal column and row distribution
for i in range(3):  # 3 columns
    window.grid_columnconfigure(i, weight=1)
for i in range(5):  # 5 rows
    window.grid_rowconfigure(i, weight=1)

# 2. Create faint grid lines for subtle visualization
for i in range(3):
    for j in range(5):
        Frame(window, bg="lightgrey", width=2).grid(row=j, column=i, sticky="ns")
        Frame(window, bg="lightgrey", height=2).grid(row=i, column=j, sticky="ew")

# 3. Label Widget for the title
label_instruction = Label(window, text="Timer")
label_instruction.grid(row=0, column=0, sticky="WE", pady=(10, 20))

# 4. Canvas for tomato image and timer text
canvas = Canvas(width=250, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image=tomato_img)
timer_text = canvas.create_text(
    125, 145, text="00:00", fill="seashell", font=(FONT_NAME, 25, "bold")
)
canvas.grid(row=1, column=1)  # Center placement

window.mainloop()
