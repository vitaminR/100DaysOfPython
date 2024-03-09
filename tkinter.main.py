import asyncio
import os
from tkinter import *
from tkinter import ttk
from openai_chat import OpenAIChat
from dotenv import load_dotenv
import threading
import openai


# 1. Setup environment and initialize OpenAIChat
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
ASSISTANT_ID = os.getenv("ASSISTANT_ID")
openai_chat = OpenAIChat(assistant_id=ASSISTANT_ID)

# 2. Define GUI layout
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("ML Flashcards with OpenAI")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(
    file="images/card_front.png"
)  # Ensure the image path is correct
canvas.create_image(400, 263, image=card_front_img)
card_text = canvas.create_text(
    400, 263, text="", font=("Arial", 40, "italic"), fill="black"
)
canvas.grid(row=0, column=0, columnspan=2)

progress_bar = ttk.Progressbar(
    window, orient=HORIZONTAL, length=300, mode="indeterminate"
)
progress_bar.grid(row=2, column=0, columnspan=2, pady=10)


# 3. Asyncio event loop setup for Tkinter
def start_asyncio_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_forever()


threading.Thread(target=start_asyncio_loop, daemon=True).start()


# 4. Async function to fetch and display flashcard content
async def fetch_flashcard_content():
    progress_bar.start()
    try:
        canvas.itemconfig(card_text, text="Fetching a fun fact for you...")
        await asyncio.sleep(2)  # Simulate fetching time

        # Here, integrate the actual fetching logic with OpenAI's API
        # For demonstration, we'll just change the text
        canvas.itemconfig(
            card_text,
            text="Did you know? The Eiffel Tower can be 15 cm taller during the summer.",
        )
        await asyncio.sleep(5)  # Display the fun fact for a bit

        # Now fetch the actual flashcard content
        canvas.itemconfig(card_text, text="Fetching new flashcard content...")
        await asyncio.sleep(2)  # Simulate fetching time
        # Replace this with actual content fetching and updating the canvas text
    finally:
        progress_bar.stop()


# 5. Tkinter callbacks
def on_update_card():
    asyncio.run_coroutine_threadsafe(
        fetch_flashcard_content(), asyncio.get_event_loop()
    )


# 6. GUI Button Setup
known_button = Button(window, text="Show Answer", command=on_update_card)
known_button.grid(row=1, column=1)

unknown_button = Button(window, text="Next", command=on_update_card)
unknown_button.grid(row=1, column=0)

# 7. Initiate the GUI
if __name__ == "__main__":
    on_update_card()  # Initial content fetch
    window.mainloop()
