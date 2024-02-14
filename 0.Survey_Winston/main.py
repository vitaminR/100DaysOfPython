# ===========================================
# 1. Importing the Tkinter Library
# ===========================================
from tkinter import (
    LEFT,
    RIGHT,
    Tk,
    Label,
    Entry,
    Button,
    Checkbutton,
    IntVar,
    Radiobutton,
    Scale,
    Spinbox,
    StringVar,
)

# - 1.1 Imports all necessary widgets and variables from tkinter for building the GUI.

# ===========================================
# 2. Creating the Main Window
# ===========================================
window = Tk()
# - 2.1 Initializes the Tkinter window.
window.title("Neighborhood Survey")
# - 2.2 Sets the title of the main window.
window.minsize(width=1000, height=800)
# - 2.3 Defines the minimum size of the window to ensure all elements fit.
window.config(padx=20, pady=20)

# ===========================================
# 3. Configuring Grid Layout for Spacing
# ===========================================
window.grid_columnconfigure(0, weight=2)
# - 3.1 Configures the first column for left-side spacing.
window.grid_columnconfigure(1, weight=1)
# - 3.2 Configures the second column for central content, making it wider.
window.grid_columnconfigure(2, weight=1)
# - 3.3 Configures the third column for right-side spacing.
window.grid_columnconfigure(3, weight=2)
# - 3.4 Configures the third column for right-side spacing.

# ===========================================
# 4. Label Widget - Survey Instructions
# ===========================================
label_instruction = Label(
    window,
    text="Please answer the following questions:\nYou will receive $1 for participating.",
)
# - 4.1 Creates a label to display survey instructions.
label_instruction.grid(row=0, column=1, columnspan=2, sticky="WE", pady=(10, 20))
# - 4.2 Adds the instruction label to the window, placing it in the central column for alignment.

# ===========================================
# 5. Entry Widget - Open-ended Question
# ===========================================
label_q1 = Label(
    window, text="1. Describe a daily task that you find time-consuming or frustrating:"
)
# - 5.1 Creates a label for the first question.
label_q1.grid(row=1, column=1, columnspan=2, sticky="WE", pady=(10, 0))
# - 5.2 Adds the first question label to the window with top padding.
entry_q1 = Entry(window, width=50)
# - 5.3 Creates an entry widget for answering the open-ended question.
entry_q1.grid(row=2, column=1, columnspan=2, sticky="WE", pady=(0, 10))
# - 5.4 Adds the entry widget to the window with bottom padding.

# Following this pattern, ensure all subsequent widgets are aligned within the central column, using `column=1` for their placement.

# ===========================================
# 6. Spinbox Widget - Severity Rating
# ===========================================
label_q2 = Label(
    window, text="2. On a scale from 1 to 10, how inconvenient is this issue for you?"
)
# - 6.1 Creates a label for the severity rating question.
label_q2.grid(row=3, column=1, columnspan=2, sticky="W", pady=(10, 0))
# - 6.2 Adds the severity question label to the window with top padding.
spinbox_q2 = Spinbox(window, from_=1, to=10, width=5)
# - 6.3 Creates a spinbox for the severity rating.
spinbox_q2.grid(row=4, column=1, columnspan=2, sticky="WE", pady=(0, 10))
# - 6.4 Adds the spinbox to the window with bottom padding.

# ===========================================
# 7. Scale Widget - Frequency
# ===========================================
label_q3 = Label(window, text="3. How often do you encounter this problem per day?")
# - 7.1 Creates a label for the frequency question.
label_q3.grid(row=5, column=1, columnspan=2, sticky="W", pady=(10, 0))
# - 7.2 Adds the frequency question label to the window with top padding.
scale_q3 = Scale(window, from_=0, to=100, orient="horizontal")
# - 7.3 Creates a scale widget for frequency rating.
scale_q3.grid(row=6, column=1, columnspan=2, sticky="WE", pady=(0, 10))
# - 7.4 Adds the scale widget to the window with bottom padding.


# ===========================================
# 8. Checkbutton Widget - Areas Affected
# ===========================================
label_q4 = Label(
    window,
    text="4. Which areas of your daily life does this issue affect? (Select all that apply)",
)
# - 8.1 Creates a label for the areas affected question.
label_q4.grid(
    row=7,
    column=1,
    columnspan=2,
    sticky="W",
    pady=(10, 0),
)
# - 8.2 Adds the areas affected question label to the window with top padding.

checkbutton_var1 = IntVar()
# - 8.3 Initializes the variable for the "Home" option checkbutton.
Checkbutton(window, text="Home", variable=checkbutton_var1).grid(
    row=8,
    column=1,
    columnspan=2,
    sticky="W",
    pady=(0, 5),
)
# - 8.4 Places the "Home" option checkbutton with slight bottom padding.

checkbutton_var2 = IntVar()
# - 8.5 Initializes the variable for the "Work" option checkbutton.
Checkbutton(window, text="Work", variable=checkbutton_var2).grid(
    row=9,
    column=1,
    columnspan=2,
    sticky="W",
    pady=(5, 10),
)

# - 8.6 Adjusts the placement of the "Work" option checkbutton with top and bottom padding for separation.

# ===========================================
# 9. Radiobutton Widget - Solution Preference
# ===========================================
label_q5 = Label(
    window,
    text="5. Would you prefer a digital AI App only to solve this problem, or would you like a local physical service as well?",
)
# - 9.1 Creates a label for the solution preference question.
label_q5.grid(row=10, column=1, columnspan=2, sticky="W", pady=(10, 0))
# - 9.2 Adds the solution preference question label to the window with top padding.

radio_var = StringVar(value="Digital")  # Ensuring variable initialization is noted.
Radiobutton(window, text="Digital", variable=radio_var, value="Digital").grid(
    row=11, column=1, columnspan=2, sticky="W", pady=(0, 5)
)
# - 9.3 Places the "Digital" option radiobutton with slight bottom padding.

Radiobutton(window, text="Physical", variable=radio_var, value="Physical").grid(
    row=12, column=1, columnspan=2, sticky="W", pady=(5, 10)
)
# - 9.4 Places the "Physical" option radiobutton with top and bottom padding for clear separation.


# Continue placing each question and corresponding widgets in the central column (column=1),
# incrementing the row for each new element to maintain proper order and spacing.


# ===========================================
# 10. Collect answers and submit button
# ===========================================
def submit_answers():
    # Collect answers
    answers = {
        "Open-Ended Question": entry_q1.get(),
        "Severity Rating": spinbox_q2.get(),
        "Frequency Rating": scale_q3.get(),
        "Home": checkbutton_var1.get(),
        "Work": checkbutton_var2.get(),
        "Solution Preference": radio_var.get(),
        # Add code to collect answers for questions 6-9 here
    }

    # Update labels with question names and answers
    label_questions.config(
        text="\n".join(k for k in answers.keys()),
        font=("Helvetica", 12, "bold"),  # Make text bold
        justify=LEFT,  # Left-align text
        anchor="w",  # Position text at the left edge of the label
        foreground="green",  # Make text green
    )
    label_answers.config(
        text="\n".join(str(v) for v in answers.values()),
        font=("Helvetica", 12, "bold"),  # Make text bold
        justify=LEFT,  # Right-align text
        anchor="e",  # Position text at the right edge of the label
    )
    label_message.config(
        text="From Isabella: Thank you very much, I'm going to use this to make you a personalized AI app. I'll talk to you soon.",
        font=("Helvetica", 16, "italic"),
        foreground="#FF69B4",  # Hot pink
        background="black",
        wraplength=525,  # Wrap text after 500 pixels
    )


Button(window, text="Submit Answers", command=submit_answers).grid(
    row=13, column=0, columnspan=4
)

# Create labels for question names and answers
label_questions = Label(window)
label_questions.grid(row=14, column=1, columnspan=1, pady=(5, 10))
label_answers = Label(window, text="")
label_answers.grid(row=14, column=2, columnspan=1, sticky="w")


# Add custom message label
label_message = Label(
    window,
    text="",
)
label_message.grid(row=17, column=0, columnspan=4, pady=(5, 10))

# # Troubleshooting: Create labels for each column in row 10
# for i in range(4):
#     color = ""
#     if i == 0:
#         color = "red"
#     elif i == 1:
#         color = "green"
#     elif i == 2:
#         color = "blue"
#     elif i == 3:
#         color = "yellow"
#     Label(window, text=f"Row 19 Column {i}", bg=color).grid(
#         row=19, column=i, sticky="we"
#     )

# ===========================================
# 11. Main Application Loop
# ===========================================
window.mainloop()
# - 11.1 Starts the Tkinter event loop, keeping the application responsive and awaiting user actions.
