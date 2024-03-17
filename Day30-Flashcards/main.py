from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


word_data = pd.read_csv("data/french_words.csv")
# dropping null value columns to avoid errors
word_data.dropna(inplace=True)

# converting to dict
data_dict = word_data.to_dict(orient="records")

# display
# print(data_dict)
current_card = {}


def next_card():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    print(current_card["French"])
    canvas.itemconfig(card_title, text="French:", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = root.after(5000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English:", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# 1. window setup
root = Tk()
root.title("Faskards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = root.after(5000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = ImageTk.PhotoImage(file="images/card_front.png")
card_back_img = ImageTk.PhotoImage(file="images/card_back.png")


card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 100, text="Welcome to FlasKards!", font=("Ariel", 40, "italic")
)
card_word = canvas.create_text(
    400, 200, text="You will have a few seconds to guess", font=("Ariel", 60, "bold")
)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=2)

x_img = PhotoImage(file="images/wrong.png")
unk_btn = Button(image=x_img, highlightthickness=0, command=next_card)
unk_btn.grid(row=2, column=0)

chk_img = PhotoImage(file="images/right.png")
known_btn = Button(image=chk_img, highlightthickness=0, command=next_card)
known_btn.grid(row=2, column=1)

# Quit the app


next_card()
root.mainloop()
