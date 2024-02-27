import time
from tkinter import *
import os
import openai
from dotenv import load_dotenv

# Load OpenAI API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")  # Get the API key
client = openai.api_key = api_key  # Create the client object

# todo troubleshooting
print(type(client))  # This should print "<class 'str'>" if it's a string
print(client)  # This will print your API key (mask it before sharing)


# Assistant ID
ASSISTANT_ID = "asst_p5w56gSkfLs2cNExCbmAcxxH"

current_thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            # Update this with the query you want to use.
            "content": "give me a quote about time.",
        }
    ]
)

# -----------------------------------------
# 1. Constants
# -----------------------------------------
CHECKMARK = "✔"  # Symbol to represent completed work sessions
YELLOW = "#f7f5dd"  # Light yellow background color
GREEN = "#5c9a8f"  # Main color for work periods
RED = "#e7305b"  # Color for break periods
PINK = "#e2979c"  # Lighter break color
FONT_NAME = "Courier"  # Font for the timer display
NORMAL_BG = "white"  # Background color for the "Normal" theme
NORMAL_FG = "black"  # Text color for the "Normal" theme

# -----------------------------------------
# 2. Themes
# -----------------------------------------
themes = {
    "Dark": {"bg": "black", "fg": "green"},  # Dark mode colors
    "Colorful": {"bg": YELLOW, "fg": RED},  # Bright colors
    "Normal": {"bg": NORMAL_BG, "fg": NORMAL_FG},  # Classic light theme
}

# -----------------------------------------
# 4. Window Setup
# -----------------------------------------
window = Tk()
window.title("Pomodoro + GPT Assistant")
window.config(padx=100, pady=50, bg=YELLOW)

# 4a. Theme dropdown
current_theme = StringVar(window)
current_theme.set("Normal")  # Set the initial theme to "Dark"
theme_option_menu = OptionMenu(window, current_theme, *themes.keys())
theme_option_menu.grid(column=0, row=0)  # Position the dropdown menu

# -----------------------------------------
# 5. UI Setup
# -----------------------------------------

# 5a. Labels and entries for work/break durations
work_min_label = Label(window, text="Work Duration (min)", bg=YELLOW)
work_min_label.grid(column=0, row=4, pady=(10, 0))  # Position the label
work_min_entry = Entry(window, width=5)
work_min_entry.insert(END, "25")  # Set default value to 25 minutes
work_min_entry.grid(column=0, row=5)

short_break_min_label = Label(window, text="Short Break Duration (min)", bg=YELLOW)
short_break_min_label.grid(column=1, row=4, pady=(10, 0))
short_break_min_entry = Entry(window, width=5)
short_break_min_entry.insert(END, "5")  # Default short break 5 minutes
short_break_min_entry.grid(column=1, row=5)

long_break_min_label = Label(window, text="Long Break Duration (min)", bg=YELLOW)
long_break_min_label.grid(column=2, row=4, pady=(10, 0))
long_break_min_entry = Entry(window, width=5)
long_break_min_entry.insert(END, "15")  # Default long break 15 minutes
long_break_min_entry.grid(column=2, row=5)


# 5b. Timer elements
canvas = Canvas(width=200, height=224, bg=NORMAL_BG, highlightthickness=0)
# Timer display area
tomato_img = PhotoImage(file="tomato.png")  # Make sure the image path is correct
canvas.create_image(100, 112, image=tomato_img)  # Add the tomato image
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)  # Position the canvas

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=NORMAL_BG, fg=GREEN)
timer_label.grid(column=1, row=0)
checkmarks_label = Label(fg=GREEN, bg=NORMAL_BG)
checkmarks_label.grid(column=1, row=3)


# -----------------------------------------
# 6. Assistant Conversation Setup
# -----------------------------------------


def send_to_assistant():
    global current_thread

    assistant_query_entry = Entry(
        window, width=50
    )  # Declare and define 'assistant_query_entry'
    assistant_query_entry.grid(
        column=0, row=9, pady=(10, 0)
    )  # Position the entry field

    user_query = assistant_query_entry.get()
    assistant_query_entry.delete(0, END)

    if not current_thread:
        current_thread = client.beta.threads.create()

    # Add user message to thread
    message = client.beta.threads.messages.create(
        thread_id=current_thread.id, role="user", content=user_query
    )
    update_conversation_display(message)

    # Run the Assistant
    run = client.beta.threads.runs.create(
        thread_id=current_thread.id,
        assistant_id=ASSISTANT_ID,
    )


assistant_conversation_label = Label(
    window, text="", bg=YELLOW, wraplength=400
)  # Add missing declaration of 'assistant_conversation_label' variable
assistant_conversation_label.grid(column=0, row=12, pady=(10, 0))  # Position the label


assistant_conversation_label_text = Text(
    window, width=50, height=10
)  # Declare and define 'assistant_conversation_label_text'
assistant_conversation_label_text.grid(
    column=0, row=12, pady=(10, 0)
)  # Position the text widget


def update_conversation_display(message):
    if message.role == "user":
        label_text = "You: "
    elif message.role == "assistant":
        label_text = "Assistant: "
    else:
        label_text = ""  # Handle other message roles as needed

    label_text += message.content + "\n"
    assistant_conversation_label_text.insert(END, label_text)


assistant_query_button = Button(window, text="Send", command=send_to_assistant)
assistant_query_button.grid(column=1, row=13)

# -----------------------------------------
# 7. Timer Logic
# -----------------------------------------

timer_active = False  # Timer status
timer_end = None  # Timestamp for when the timer should end


def start_timer():
    global work_sessions, timer_active, timer_end
    if not timer_active:  # Only start if not already running
        work_sessions = 0  # Declare and initialize the 'work_sessions' variable

        work_sessions += 1

        work_min = int(work_min_entry.get())
        short_break_min = int(short_break_min_entry.get())
        long_break_min = int(long_break_min_entry.get())

        # Determine break type
        if work_sessions % 8 == 0:
            duration = long_break_min * 60
            timer_label.config(text="Break", fg=RED)
        elif work_sessions % 2 == 0:
            duration = short_break_min * 60
            timer_label.config(text="Break", fg=PINK)
        else:
            duration = work_min * 60
            timer_label.config(text="Work", fg=GREEN)

        timer_end = time.time() + duration  # Calculate end time
        timer_active = True
        display_time_remaining()  # Start the countdown display


def stop_timer():
    global timer_active, timer_end
    timer_active = False
    timer_end = None  # Clear the end timestamp


def display_time_remaining():
    global timer, timer_active, timer_end
    if timer_active and timer_end:
        now = time.time()
        remaining = max(
            0, int(timer_end - now)
        )  # Ensure remaining time is not negative
        minutes, seconds = divmod(remaining, 60)
        canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
        timer = window.after(1000, display_time_remaining)
    else:
        canvas.itemconfig(timer_text, text="00:00")  # Reset if timer stopped


# -----------------------------------------
# 8. Countdown Mechanism
# -----------------------------------------

global timer  # Make 'timer' global


def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(
        timer_text, text=f"{minutes:02d}:{seconds:02d}"
    )  # Update the timer display

    if count > 0:
        timer = window.after(
            1000, count_down, count - 1
        )  # Schedule the next countdown update
    else:
        start_timer()  # Start the next cycle (work or break)
        marks = ""
        for _ in range(work_sessions // 2):
            marks += CHECKMARK
        checkmarks_label.config(text=marks)


count = 60  # Initialize the 'count' variable with a value
count_down(count)  # Call the count_down function with the 'count' variable
# -----------------------------------------
# 9. Timer Buttons and Reset
# -----------------------------------------

start_button = Button(text="Start", command=start_timer)  # Define the start button
start_button.grid(column=0, row=2)  # Add the start button to the grid


def reset_timer():
    # Add your code here to reset the timer
    pass


stop_button = Button(text="Stop", command=stop_timer)  # Add stop button
stop_button.grid(column=1, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

# -----------------------------------------
# 10. GPT-3.5-turbo Integration
# -----------------------------------------


def handle_gpt_query():
    # Add your code here to handle the GPT query
    pass


gpt_query_entry = Entry(window, width=50)  # Entry for the user's GPT-3 query
gpt_query_entry.grid(column=0, row=10, pady=(10, 0))
gpt_response_label = Label(
    window, text="", bg=YELLOW, wraplength=400
)  # Label to display the response
gpt_response_label.grid(column=0, row=11, pady=(10, 0))


# -----------------------------------------
# 11.  User Input and Theme Handling
# -----------------------------------------


def handle_enter_key(event=None):  # Function to call when Enter is pressed
    handle_gpt_query()


window.bind("<Return>", handle_enter_key)  # Bind Enter key to query GPT-3

# Define the button first:
gpt_query_button = Button(window, text="Ask GPT", command=handle_gpt_query)
gpt_query_button.grid(column=2, row=10)

# Adjust the layout (optional)
gpt_query_entry.grid(column=1, row=10, pady=(10, 0))  # Move to the right
gpt_response_label.grid(
    column=1, row=11, columnspan=2, pady=(10, 0)
)  # Expand the response label


# -----------------------------------------
# 12. THEME FUNCTION
# -----------------------------------------
def apply_theme():
    theme = themes[current_theme.get()]  # Get the selected theme
    window.config(bg=theme["bg"])  # Update the main window background
    timer_label.config(fg=theme["fg"], bg=theme["bg"])
    checkmarks_label.config(fg=theme["fg"], bg=theme["bg"])
    work_min_label.config(bg=theme["bg"], fg=theme["fg"])
    short_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    long_break_min_label.config(bg=theme["bg"], fg=theme["fg"])
    gpt_response_label.config(bg=theme["bg"], fg=theme["fg"])
    canvas.config(bg=theme["bg"])  # Update the canvas background


# Initial theme application
apply_theme()

# Apply theme changes when the dropdown selection changes
current_theme.trace("w", lambda *args: apply_theme())

# -----------------------------------------
# 13. START THE TKINTER MAIN LOOP
# -----------------------------------------
window.mainloop()
