from tkinter import *
from openai import *


# class to get new math problem from openai
class MathProblem:
    def __init__(self):
        self.problem = ""
        self.answer = ""
        self.get_new_problem()

    def get_new_problem(self):
        self.problem, self.answer = get_math_problem()
        print(self.problem, self.answer)

    def get_problem(self):
        return self.problem

    def get_answer(self):
        return self.answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")

# Create a canvas image
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)


# Create a button
known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img, highlightthickness=0, command=known_button_click)

known_button.grid(row=2, column=1)

unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=unknown_img, highlightthickness=0, command=unknown_button_click
)
unknown_button.grid(row=2, column=0)

# Create a label
word_label = Label(text="ML Math", font=("Ariel", 60, "bold"), bg=BACKGROUND_COLOR)
word_label.grid(row=1, column=0, columnspan=2)


# make the wrong button do something
def unknown_button_click():
    # make a popup window
    wrong_popup = Tk()
    wrong_popup.title("Added to unkown")
    wrong_popup.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    wrong_popup_label = Label(
        wrong_popup, text="Wrong", font=("Ariel", 60, "bold"), bg=BACKGROUND_COLOR
    )
    wrong_popup_label.grid(row=1, column=0, columnspan=2)


# make the right button do something
def known_button_click():
    # change the card
    # change the card
    canvas.itemconfig(canvas_text, text=new_word)


window.mainloop()
