from tkinter import *

# Create the main window
window = Tk()
window.title("Kilometers to Miles Per Hour Converter")

# Configure the grid layout
for i in range(4):
    window.grid_columnconfigure(i, weight=1)

# Create a label and entry for the kilometers input
Label(window, text="Kilometers per hour:", bg="green").grid(
    row=0, column=1, sticky="we", padx=10, pady=10
)
kmph = DoubleVar()
Entry(window, textvariable=kmph).grid(row=1, column=1, sticky="we", padx=10, pady=10)

# Create a label for the miles per hour output
Label(window, text="Miles per hour:", bg="blue").grid(
    row=2, column=1, sticky="we", padx=10, pady=10
)
mph = StringVar()
Label(window, textvariable=mph, bg="yellow").grid(
    row=3, column=1, sticky="we", padx=10, pady=10
)


# Create a function to convert kilometers per hour to miles per hour
def convert():
    miles = kmph.get() * 0.621371
    mph.set(f"{miles:.2f}")


# Create a button to perform the conversion
Button(window, text="Convert", command=convert).grid(
    row=4, column=1, sticky="we", padx=10, pady=10
)

window.mainloop()
