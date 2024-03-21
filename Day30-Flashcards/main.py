### 1. Importing the necessary libraries ###
import pandas as pd  # 1.1 For handling data.
import random  # 1.2 For shuffling data.
import os  # 1.3 For file path operations.
from tkinter import *  # 1.4 For GUI creation.
from PIL import Image, ImageTk  # 1.5 For image handling.
import simpleaudio as sa  # 1.6 For playing sound.

### 2. Setting constants ###
BACKGROUND_COLOR = "#B1DDC6"  # 2.1 Background color for the app.


### 3. Preparing word data ###
### 3. Preparing word data ###
# 3.1 Define a function to load word data from CSV files
def load_word_data():
    words_to_learn_path = "data/words_to_learn.csv"  # The custom list of words to learn
    default_data_path = "data/french_words.csv"  # The default dataset

    # 3.2 Check if 'words_to_learn.csv' exists and is not empty
    if os.path.exists(words_to_learn_path) and os.path.getsize(words_to_learn_path) > 0:
        try:
            # 3.2.1 Attempt to load the custom word list
            return pd.read_csv(words_to_learn_path)
        except pd.errors.EmptyDataError:
            # 3.2.2 Fallback to the default dataset if the file is unreadable
            return pd.read_csv(default_data_path)
    else:
        # 3.3 Load the default dataset if the custom word list does not exist
        return pd.read_csv(default_data_path)


# Use the load_word_data function to load the word data
word_data = load_word_data()
word_data.dropna(inplace=True)  # 3.4 Ensure there are no missing values

# 3.5 Convert the data to a list of dictionaries and shuffle it
data_dict = word_data.to_dict(orient="records")
random.shuffle(data_dict)  # 3.6 Shuffle to randomize flashcards

### 4. Initializing global variables ###
current_card = {}  # 4.1 The current flashcard displayed.
current_index = 0  # 4.2 Index to track the current card position.


### 5. Function definitions ###
def play_sound(sound_file):
    # 5.1 Function to play sound
    wave_obj = sa.WaveObject.from_wave_file(sound_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until sound has finished playing


def next_card():
    # 5.2 Display the next card
    global current_card, current_index, flip_timer
    if not data_dict:
        # 5.2.1 If no more cards, show congratulations.
        show_congratulations()
        return
    if flip_timer:
        root.after_cancel(flip_timer)
    current_card = data_dict[current_index]
    current_index = (current_index + 1) % len(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = root.after(3000, flip_card)


def flip_card():
    # 5.3 Flip the card to show the answer
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def known_word():
    # 5.4 Mark the current word as known and remove from the list
    global current_index
    if current_card in data_dict:
        data_dict.remove(current_card)
        pd.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)
        play_sound("sounds/correct.wav")  # Play sound for correct answer
    if not data_dict:
        show_congratulations()
        return
    if current_index >= len(data_dict):
        current_index = 0
    next_card()


def show_congratulations():
    # 5.5 Show congratulations message
    canvas.itemconfig(card_title, text="Congratulations!", fill="black")
    canvas.itemconfig(card_word, text="You've learned all the words!", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)


### 6. GUI setup ###
root = Tk()
root.title("FlasKards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = ImageTk.PhotoImage(Image.open("images/card_front.png"))
card_back_img = ImageTk.PhotoImage(Image.open("images/card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

chk_img = PhotoImage(file="images/right.png")
known_btn = Button(root, image=chk_img, highlightthickness=0, command=known_word)
known_btn.grid(row=1, column=1)

x_img = PhotoImage(file="images/wrong.png")
unk_btn = Button(root, image=x_img, highlightthickness=0, command=next_card)
unk_btn.grid(row=1, column=0)

### 7. Start the application ###
# 7.1 Automatically show the first card when the application starts.
next_card()

### 8. Main event loop ###
# 8.1 Keep the application window open and responsive.
root.mainloop()
