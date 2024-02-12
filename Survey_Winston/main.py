# Door to door survey
# ===========================================
# 1. Importing the Tkinter Library
# ===========================================
from tkinter import (
    END,
    Button,
    Checkbutton,
    Entry,
    IntVar,
    Label,
    Listbox,
    Radiobutton,
    Scale,
    Spinbox,
    StringVar,
    Tk,
    Text,
)

# ===========================================
# 2. Creating the Main Window
# ===========================================
window = Tk()
# - 2.1 Initializes the Tkinter window.
window.title("Neighborhood Survey")
# - 2.2 Sets the title of the main window.
window.minsize(width=500, height=600)
# - 2.3 Defines the minimum size of the window to ensure all elements fit.

# ===========================================
# 3. Label Widget - Survey Instructions
# ===========================================
label_instruction = Label(
    window,
    text="Please answer the following questions:\nYou will receive $1 for participating.",
)
# - 3.1 Creates a label to display survey instructions.
label_instruction.pack()
# - 3.2 Adds the instruction label to the window.

# ===========================================
# 4. Entry Widget - Open-ended Question
# ===========================================
label_q1 = Label(
    window, text="1. Describe a daily task that you find time-consuming or frustrating:"
)
# - 4.1 Creates a label for the first question.
label_q1.pack()
# - 4.2 Adds the question label to the window.
entry_q1 = Entry(window, width=50)
# - 4.3 Creates an entry widget for answering the open-ended question.
entry_q1.pack()
# - 4.4 Adds the entry widget to the window.

# ===========================================
# 5. Spinbox Widget - Severity Rating
# ===========================================
label_q2 = Label(
    window, text="2. On a scale from 1 to 10, how inconvenient is this issue for you?"
)
# - 5.1 Creates a label for the severity rating question.
label_q2.pack()
# - 5.2 Adds the severity question label to the window.
spinbox_q2 = Spinbox(window, from_=1, to=10, width=5)
# - 5.3 Creates a spinbox for the severity rating.
spinbox_q2.pack()
# - 5.4 Adds the spinbox to the window.

# ===========================================
# 6. Scale Widget - Frequency
# ===========================================
label_q3 = Label(window, text="3. How often do you encounter this problem per day?")
# - 6.1 Creates a label for the frequency question.
label_q3.pack()
# - 6.2 Adds the frequency question label to the window.
scale_q3 = Scale(window, from_=0, to=100, orient="horizontal")
# - 6.3 Creates a scale widget for frequency rating.
scale_q3.pack()
# - 6.4 Adds the scale widget to the window.

# ===========================================
# 7. Checkbutton Widget - Areas Affected
# ===========================================
label_q4 = Label(
    window,
    text="4. Which areas of your daily life does this issue affect? (Select all that apply)",
)
# - 7.1 Creates a label for the areas affected question.
label_q4.pack()
# - 7.2 Adds the areas affected question label to the window.
checkbutton_var1 = IntVar()
Checkbutton(window, text="Home", variable=checkbutton_var1).pack()
# - 7.3 Creates and adds a checkbutton for the "Home" option.
checkbutton_var2 = IntVar()
Checkbutton(window, text="Work", variable=checkbutton_var2).pack()
# - 7.4 Creates and adds a checkbutton for the "Work" option.


# ===========================================
# 8. Radiobutton Widget - Solution Preference
# ===========================================
label_q5 = Label(
    window,
    text="5. Would you prefer a digital AI App or a local physical service to solve this problem?",
)
# - 8.1 Creates a label for the solution preference question.
label_q5.pack()
# - 8.2 Adds the solution preference question label to the window.
radio_var = StringVar(value="Digital")
Radiobutton(window, text="Digital", variable=radio_var, value="Digital").pack()
# - 8.3 Creates and adds a radiobutton for the "Digital" option.
Radiobutton(window, text="Physical", variable=radio_var, value="Physical").pack()
# - 8.4 Creates and adds a radiobutton for the "Physical" option.


# ===========================================
# 9. Functionality for Submit Button
# ===========================================
def submit_answers():
    # This function will handle the logic to process and store survey responses.
    # Example placeholder functionality:
    print("Collecting Answers...")
    answers = {
        "Open-Ended": entry_q1.get(),
        "Severity": spinbox_q2.get(),
        "Frequency": scale_q3.get(),
        "Areas Affected": {
            "Work": checkbutton_var1.get(),
            "Home": checkbutton_var2.get(),
        },
        "Solution Preference": radio_var.get(),
    }
    # Here you would add the logic to send answers to your storage solution or integrate with an API.
    print("Answers Submitted:", answers)


# ===========================================
# 10. Submit Button
# ===========================================
# Removed the first definition of submit_answers()

button_submit = Button(window, text="Submit Answers", command=submit_answers)
button_submit.pack()
# - 9.2 Adds the submit button to the window, making it visible for user interaction.


# ===========================================
# 11. Main Application Loop
# ===========================================
window.mainloop()
# - 11.1 Starts the Tkinter event loop, keeping the application responsive and awaiting user actions.
