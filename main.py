from tkinter import *
import openai
from dotenv import load_dotenv
import os

# -----------------------------------------
# 1. Environment Setup and API Configuration
# -----------------------------------------

# 1.1 Load API credentials from environment variables
#     - Ensures sensitive API keys are not directly embedded in the code
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
assistant_id = os.getenv("ASSISTANT_ID")

# 1.2 Initialize the OpenAI client
#     - Establishes the connection to the OpenAI API
client = openai.Client()
# -----------------------------------------
# 2. OpenAI Assistant Interaction
# -----------------------------------------

# 2.1 Create a specialized math tutor assistant
#     - Provides clear instructions to focus the assistant on math tasks
#     - Uses the 'code_interpreter' tool to enable code generation by the assistant
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions. "
    "Focus on providing flashcard-friendly questions and answers. Start questions with 'q:' and answers with 'a:'",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo-preview",
)

# 2.2 Initialize a new thread for flashcard generation
#     - Creates a dedicated conversation space for generating math flashcards
thread = client.beta.threads.create()

# 2.3 Begin conversation by requesting a math question
#     - Prompts the assistant to  provide a suitable question and answer
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="We are making ML Math Flashcards. We need a math question to put on the front of a flashcard, "
    "and the answer on the back. Please lead your questions with 'q:' and answers with 'a:'",
)

# 2.4 Prompt the assistant to select a question from your 'ML_Math' document
#      - Guides the assistant to use existing material for flashcards
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please look at the ML_Math document and pick out a math question to put on the front of a flashcard.",
)
# 2.5 Wait for the run to complete
#     - Pauses execution until the OpenAI assistant has finished its task
run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

# 2.6 Retrieve the assistant's response
#     - Collects the generated math question and answer from the OpenAI thread
messages = client.beta.threads.messages.list(thread_id=thread.id)


# -----------------------------------------
# 3. Math Problem Class
# -----------------------------------------


def extract_problem_and_answer(messages):
    """Assumes a simple 'q:' and 'a:' format in the OpenAI response."""
    for message in messages.data:
        if message.role == "assistant":
            text = message.content[0].text.value

            # Simple splitting (adjust if the response format changes)
            question, answer = text.split("q:")[1].split("a:")
            return question.strip(), answer.strip()

    # If no 'q:' and 'a:' are found:
    return "Question not found", "Answer not found"


class MathProblem:
    """Represents a math problem and its solution, obtained from OpenAI."""

    def __init__(self):
        self.problem = ""
        self.answer = ""
        self.get_new_problem()

    def get_new_problem(self):
        """Fetches a new math problem and answer from the OpenAI thread."""
        # TODO: Extract the question and answer from the OpenAI response in 'messages'
        #       You'll likely need to parse the text content of the assistant's messages
        self.problem, self.answer = extract_problem_and_answer(messages)

    def get_problem(self):
        """Returns the current math problem."""
        return self.problem

    def get_answer(self):
        """Returns the answer to the current math problem."""
        return self.answer

    def check_answer(self, user_answer):
        """Checks if the user's answer is correct."""
        return user_answer == self.answer


# -----------------------------------------
# 4. Tkinter GUI Setup
# -----------------------------------------
# 4.1 GUI Constants and Setup
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("ML Math Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# 4.2  Flashcard Display (Canvas)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")  # Ensure the path is correct
canvas.create_image(400, 263, image=card_front_img)
canvas_text = canvas.create_text(
    400, 263, text="", font=("Ariel", 40, "italic"), fill="black"
)
canvas.grid(row=0, column=0, columnspan=2)

# 4.3 Initialize the Math Problem
math_problem = MathProblem()  # Initialize MathProblem to get the first question

# -----------------------------------------
# 5.  Updating the Flashcard
# -----------------------------------------


# 5.1 Function to update the displayed flashcard
def update_card():
    """Retrieves a new problem from the MathProblem object and updates the Tkinter canvas."""
    new_problem = math_problem.get_problem()
    canvas.itemconfig(canvas_text, text=new_problem)


# ... (Rest of your Tkinter GUI code) ...


# -----------------------------------------
# 6. Button Handlers
# -----------------------------------------
def unknown_button_click():
    """Handles the 'Unknown' button press."""
    print("Incorrect")  # Could be expanded to provide feedback or explanations
    math_problem.get_new_problem()
    update_card()


def known_button_click():
    """Handles the 'Known' button press."""
    print("Correct")  # Could be expanded to include rewards or progress tracking
    math_problem.get_new_problem()
    update_card()


# 6.2 Button Setup
known_img = PhotoImage(file="images/right.png")  # Ensure the path is correct
known_button = Button(image=known_img, highlightthickness=0, command=known_button_click)
known_button.grid(row=1, column=1)

unknown_img = PhotoImage(file="images/wrong.png")  # Ensure the path is correct
unknown_button = Button(
    image=unknown_img, highlightthickness=0, command=unknown_button_click
)
unknown_button.grid(row=1, column=0)
# -----------------------------------------
# 7. Starting the Flashcard App
# -----------------------------------------

# 7.1 Initial card display
update_card()

# 7.2 Tkinter Main Loop - Keeps the GUI running
window.mainloop()
