# import all my modules
import random
from tkinter import messagebox

# import my data.txt
import os
import tkinter as tk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generate a password that is 8 characters long
def generate_password():
    entry_password.delete(0, tk.END)
    password = ""
    for _ in range(8):
        password += chr(random.randint(33, 126))
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


# save the password to a file
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if not website or not email or not password:
        tk.messagebox.showerror(
            title="Error", message="All fields must be filled out before saving."
        )
        return

    with open("data.txt", "a", encoding="utf-8") as data:
        data.write(f"{website} | {email} | {password}\n")
        entry_website.delete(0, tk.END)
        entry_password.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

# create a window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create a canvas
canvas = tk.Canvas(width=200, height=200)
canvas.grid(row=0, column=1)


# import logo
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

# Row 1
label_website = tk.Label(text="Website:")
label_website.grid(row=1, column=0)
entry_website = tk.Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2, sticky="EW")

# row 2
label_email = tk.Label(text="Email/Username:")
label_email.grid(row=2, column=0)
entry_email = tk.Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_email.insert(0, "nymilitarypolice@gmail.com")

# row 3
label_password = tk.Label(text="Password:")
label_password.grid(row=3, column=0)
entry_password = tk.Entry(width=21)
entry_password.grid(row=3, column=1, sticky="EW")

button_generate = tk.Button(text="Generate Password")
button_generate.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=36)
button_add.grid(row=4, column=1, columnspan=2)

# make the buttons work
button_generate.config(command=generate_password)
button_add.config(command=save)


# start the program

window.mainloop()
