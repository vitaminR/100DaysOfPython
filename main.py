# Day 27 GUI

from tkinter import Tk, Button, Label

# Create a window
window = Tk()
window.title("Day27")
window.minsize(width=500, height=300)

# lable with cool font
label = Label(
    text="Sumerizer",
    font=("quicksand", 24, "bold"),
    fg="blue",
    bg="yellow",
    padx=20,
    pady=20,
)

# Position the label at the top center of the window
label.pack(anchor="n")

# display total of all numbers on center of the screen:
my_label = Label(text="Total", font=("quicksand", 24, "bold"))
my_label.pack(expand=True, side="left")


def add_unlimited(*args):
    total = 0
    for n in args:
        total += n
    # Update the text of my_label to display the total
    my_label.config(text=f"Total: {total}")


# print total on screen:
my_button = Button(text="Add", command=lambda: add_unlimited(1, 3, 4, 6, 9))
# display button
my_button.pack(expand=True, side="left")


def calculate(n, **kwargs):

    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    n /= kwargs["divide"]
    n -= kwargs["subtract"]

    print(n)


calculate(2, add=3, multiply=5, divide=8, subtract=1)
