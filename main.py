import json
import random
import tkinter as tk
from tkinter import END, messagebox, simpledialog
from PIL import Image, ImageTk, ImageDraw


# ---------------------------- 1. Copy to clipboard popup ------------------------------- ## ---------------------------- 1. Copy to clipboard popup ------------------------------- #
# ---------------------------- 1. Copy to clipboard popup ------------------------------- #
class CopyableDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, password=None):
        self.password = password
        super().__init__(parent, title=title)

    def body(self, parent):
        label = tk.Label(self, text="Password:")
        label.pack()
        self.text = tk.Text(self, width=40, height=1)
        self.text.pack(fill="both", expand=True)
        self.text.insert("1.0", self.password)
        self.text.configure(state="disabled")
        return self.text

    def set_geometry(self, x, y):
        self.geometry(f"+{x}+{y}")


# ---------------------------- 2. Search for password ------------------------------- #
def search_password():
    website = entry_website.get()
    password = ""

    if len(website) == 0:
        messagebox.showerror(
            title="Error", message="Input a website for me to fetch the password."
        )
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(
            title="No Password Found",
            message="No password were saved yet.",
        )
        return

    for key, value in data.items():
        if key == website:
            password = value["password"]
            break

    if password:
        CopyableDialog(window, title="Password Found", password=password)
    else:
        messagebox.showerror(
            title="No Password Found",
            message="No password found for the given website.",
        )

    entry_website.delete(0, END)


# ---------------------------- 3. PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, tk.END)
    password = "".join(chr(random.randint(33, 126)) for _ in range(8))
    entry_password.insert(0, password)


# ---------------------------- 4. SAVE PASSWORD ------------------------------- #
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
        return

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

    entry_website.delete(0, END)
    entry_password.delete(0, END)


# ---------------------------- 5. UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.grid_rowconfigure(6, minsize=50)
window.config(padx=50, pady=50)
tk.Label(window).grid(row=6)

canvas = tk.Canvas(width=200, height=200)
canvas.grid(row=0, column=1, pady=20)

img = Image.open("logo.png")
img = img.resize((222, 222), Image.LANCZOS)

mask = Image.new("L", img.size, 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle([0, 0, img.width, img.height], radius=30, fill=255)

result = Image.new("RGB", img.size)
result.paste(img, mask=mask)

logo = ImageTk.PhotoImage(result)
canvas.create_image(100, 100, image=logo)

label = tk.Label(
    window, text="AI Password Generator", fg="blue", font=("Helvetica", 24)
)
label.grid(row=1, column=1)

entry_website = tk.Entry(width=35)
entry_website.grid(row=2, column=1, sticky="EW")
tk.Label(text="Website:").grid(row=2, column=0)

entry_email = tk.Entry(width=35)
entry_email.grid(row=3, column=1, columnspan=2, sticky="EW")
entry_email.insert(0, "nymilitarypolice@gmail.com")
tk.Label(text="Email/Username:").grid(row=3, column=0)

entry_password = tk.Entry(width=21)
entry_password.grid(row=4, column=1, sticky="EW")
tk.Label(text="Password:").grid(row=4, column=0)

tk.Button(text="Search", command=search_password).grid(
    row=2, column=2, columnspan=2, sticky="EW"
)
tk.Button(text="Generate Password", command=generate_password).grid(row=3, column=2)
tk.Button(text="Add", width=36, command=save).grid(
    row=5,
    column=1,
    columnspan=2,
    rowspan=2,
    sticky="EW",
)

tk.Label(window).grid(row=6)

window.mainloop()
