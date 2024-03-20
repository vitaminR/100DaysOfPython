# 1. Importing the necessary libraries: where our coding journey begins.
import pandas as pd  # For managing our word data like a data wizard.
import random  # To shuffle words, making learning unpredictable and fun.
import os  # For file operations, because even heroes need to check their inventory.
from tkinter import *  # The GUI toolkit, because every hero needs a flashy interface.
from tkinter import (
    ttk,
)  # Additional tkinter goodies, for when you need that extra flair.
from PIL import (
    Image,
    ImageTk,
)  # For dealing with images, making learning visually appealing.

# 2. Constants are the rock upon which we build our code fortress.
BACKGROUND_COLOR = "#B1DDC6"  # A soothing background color, like a calm sea.

# 3. Preparing our word data: the arsenal of knowledge.
# 3a. Deciding which word list to engage with today.
if os.path.exists("data/words_to_learn.csv"):
    word_data = pd.read_csv("data/words_to_learn.csv")  # The path of the knowledgeable.
else:
    word_data = pd.read_csv("data/french_words.csv")  # The path of the beginner.
word_data.dropna(
    inplace=True
)  # Banishing any voids in our data, like a hero banishes fear.

# 3b. Converting the data into a list of dictionaries: our flashcard deck.
data_dict = word_data.to_dict(orient="records")
random.shuffle(
    data_dict
)  # Shuffling the deck, because unpredictability is the spice of life.

# 4. Global variables: the characters in our story.
current_card = {}  # The current flashcard: a mystery to unravel.
current_index = 0  # Our position in the journey of learning.


# 5. Function declarations: our spells to cast at will.
# 5a. Revealing the next card: a step forward in our quest.
def next_card():
    global current_card, flip_timer, current_index  # Invoking our global variables.
    root.after_cancel(
        flip_timer
    )  # Stopping the countdown, because anticipation is key.
    current_card = data_dict[current_index]  # The revelation of the current word.
    current_index = (current_index + 1) % len(
        data_dict
    )  # Moving forward, but in a loop.
    # Updating the canvas with the new word, like painting a masterpiece.
    canvas.itemconfig(card_title, text="French:", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = root.after(5000, flip_card)  # The suspenseful wait before the reveal.


# 5b. The flip card function: revealing the hidden truth.
def flip_card():
    global current_card  # The global card, holding secrets to be unveiled.
    # Changing the canvas to show the English translation, like the turn of a page.
    canvas.itemconfig(card_title, text="English:", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# 5c. Recognizing a known word: the hero's choice to move on.
def known_word():
    global current_card, data_dict  # Our protagonists in this story of learning.
    data_dict.remove(
        current_card
    )  # The act of letting go, for we have mastered this word.
    next_card()  # Onward to the next challenge, with no time to rest.
    pd.DataFrame(data_dict).to_csv(
        "data/words_to_learn.csv", index=False
    )  # Recording our journey for posterity.


# 6. The main stage: where our tale unfolds.
# 6a. Setting up the root window: the foundation of our GUI castle.
root = Tk()
root.title("FlasKards")  # A title that promises adventure and learning.
root.config(
    padx=50, pady=50, bg=BACKGROUND_COLOR
)  # Styling our GUI, because aesthetics matter.

flip_timer = root.after(
    5000, flip_card
)  # The countdown begins, like the ticking of a clock in a suspenseful moment.

# 6b. Crafting the canvas: the painter's easel.
canvas = Canvas(width=800, height=526)
card_front_img = ImageTk.PhotoImage(
    file="images/card_front.png"
)  # The face of our flashcard.
card_back_img = ImageTk.PhotoImage(
    file="images/card_back.png"
)  # The hidden side, bearing answers.
# Placing the elements on our canvas, like setting the stage for a play.
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 100, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 200, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)

# 6c. The interactive elements: our buttons of destiny.
x_img = PhotoImage(file="images/wrong.png")  # The symbol of rejection.
unk_btn = Button(
    image=x_img, highlightthickness=0, command=next_card
)  # The button of continued curiosity.
unk_btn.grid(row=2, column=0)

chk_img = PhotoImage(file="images/right.png")  # The symbol of mastery.
known_btn = Button(
    image=chk_img, highlightthickness=0, command=known_word
)  # The button of achievement.
known_btn.grid(row=2, column=1)

# 7. The beginning of our adventure: invoking the first card.
next_card()

# 8. And so the story continues, indefinitely...
root.mainloop()
