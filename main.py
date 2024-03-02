import random
import tkinter as tk
from tkinter import END, messagebox
import json
from PIL import Image, ImageTk, ImageDraw


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, tk.END)
    password = "".join(chr(random.randint(33, 126)) for _ in range(8))
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error", message="All fields must be filled out before saving."
        )
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.grid_rowconfigure(6, minsize=50)
window.config(padx=50, pady=50)
tk.Label(window).grid(row=6)

canvas = tk.Canvas(width=200, height=200)
canvas.grid(row=0, column=1, pady=20)

img = Image.open("logo.png")
img = img.resize((222, 222), Image.LANCZOS)

# Create a new image with the same size and alpha channel (for transparency)
mask = Image.new("L", img.size, 0)
# Create a draw object
draw = ImageDraw.Draw(mask)
# Draw a white rounded rectangle with the same size as the image onto the mask
draw.rounded_rectangle([0, 0, img.width, img.height], radius=30, fill=255)

# Create a new image with the same size as the original image
result = Image.new("RGB", img.size)
# Paste the original image onto the result image, using the mask
result.paste(img, mask=mask)

# Convert the result image to a PhotoImage
logo = ImageTk.PhotoImage(result)
canvas.create_image(100, 100, image=logo)

label = tk.Label(
    window, text="AI Password Generator", fg="blue", font=("Helvetica", 24)
)
label.grid(row=1, column=1)

entry_website = tk.Entry(width=35)
entry_website.grid(row=2, column=1, columnspan=2, sticky="EW")
tk.Label(text="Website:").grid(row=2, column=0)

entry_email = tk.Entry(width=35)
entry_email.grid(row=3, column=1, columnspan=2, sticky="EW")
entry_email.insert(0, "nymilitarypolice@gmail.com")
tk.Label(text="Email/Username:").grid(row=3, column=0)

entry_password = tk.Entry(width=21)
entry_password.grid(row=4, column=1, sticky="EW")
tk.Label(text="Password:").grid(row=4, column=0)

tk.Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
tk.Button(text="Add", width=36, command=save).grid(
    row=5, column=1, columnspan=2, rowspan=2
)

# Add an empty label in the 6th row to force the window to accommodate the extra row
tk.Label(window).grid(row=6)

window.mainloop()
