# ===========================================
# 1. Importing the Tkinter Library
# ===========================================
from tkinter import *

# - 1.1 This imports all necessary classes, functions, and variables from the Tkinter library for GUI creation.

# ===========================================
# 2. Creating the Main Window
# ===========================================
window = Tk()
# - 2.1 Initializes the main application window with Tk().
window.title("Widget Examples")
# - 2.2 Sets the window title.
window.minsize(width=500, height=500)
# - 2.3 Defines the minimum size of the window.

# ===========================================
# 3. Label Widget
# ===========================================
label = Label(text="This is old text")
# - 3.1 Creates a label widget with initial text.
label.config(text="This is new text")
# - 3.2 Updates the label's text to "This is new text".
label.pack()
# - 3.3 Places the label in the window using the pack geometry manager.


# ===========================================
# 4. Button Widget
# ===========================================
def action():
    print("Do something")
    # - 4.1 Function to be executed when the button is clicked, printing "Do something".


button = Button(text="Click Me", command=action)
# - 4.2 Creates a button that calls the 'action' function when clicked.
button.pack()
# - 4.3 Adds the button to the window and displays it.

# ===========================================
# 5. Entry Widget
# ===========================================
entry = Entry(width=30)
# - 5.1 Creates an entry widget for text input.
entry.insert(END, string="Some text to begin with.")
# - 5.2 Pre-populates the entry with "Some text to begin with."
entry.pack()
# - 5.3 Adds the entry widget to the window and displays it.

# ===========================================
# 6. Text Widget (Multi-line Text Entry)
# ===========================================
text = Text(height=5, width=30)
# - 6.1 Creates a text widget for multi-line text input.
text.insert(END, "Example of multi-line text entry.")
# - 6.2 Inserts "Example of multi-line text entry." as initial text.
text.pack()
# - 6.3 Adds the text widget to the window and displays it.


# ===========================================
# 7. Spinbox Widget
# ===========================================
def spinbox_used():
    print(spinbox.get())
    # - 7.1 Function to print the current value of the spinbox.


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# - 7.2 Creates a spinbox for selecting numbers within a range.
spinbox.pack()
# - 7.3 Adds the spinbox to the window and displays it.


# ===========================================
# 8. Scale Widget
# ===========================================
def scale_used(value):
    print(value)
    # - 8.1 Function to print the current value of the scale.


scale = Scale(from_=0, to=100, command=scale_used)
# - 8.2 Creates a scale (slider) for selecting a range of values.
scale.pack()
# - 8.3 Adds the scale to the window and displays it.


# ===========================================
# 9. Checkbutton Widget
# ===========================================
def checkbutton_used():
    print(checked_state.get())
    # - 9.1 Function to print the state of the checkbutton (0 for off, 1 for on).


checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
# - 9.2 Variable to hold the state of the checkbutton.
# - 9.3 Creates a checkbutton that toggles the state between on and off.
checkbutton.pack()
# - 9.4 Adds the checkbutton to the window and displays it.


# ===========================================
# 10. Radiobutton Widget
# ===========================================
def radio_used():
    print(radio_state.get())
    # - 10.1 Function to print which radiobutton is selected.


radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option1", value=1, variable=radio_state, command=radio_used
)
# - 10.2 Variable to hold which radiobutton value is checked.
# - 10.3 Creates the first radiobutton option.
radiobutton2 = Radiobutton(
    text="Option2", value=2, variable=radio_state, command=radio_used
)
# -
# - 10.4 Creates the second radiobutton option.
radiobutton1.pack()
# - 10.5 Adds the first radiobutton to the window and displays it.
radiobutton2.pack()
# - 10.6 Adds the second radiobutton to the window and displays it.


# ===========================================
# 11. Listbox Widget
# ===========================================
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
    # - 11.1 Function to print the currently selected item from the listbox.


listbox = Listbox(height=4)
# - 11.2 Creates a listbox to display a list of items.
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(END, item)
    # - 11.3 Inserts each item into the listbox.
listbox.bind("<<ListboxSelect>>", listbox_used)
# - 11.4 Binds the selection event to the 'listbox_used' function to print the selection when it changes.
listbox.pack()
# - 11.5 Adds the listbox to the window and displays it.

# ===========================================
# 13. Text Box for Displaying Selected or Typed Options
# ===========================================
text_box = Text(window)
# - 13.1 Creates a text box for output display.
text_box.pack()
# - 13.2 Adds the text box to the window and displays it.


# ===========================================
# 14. Function to Display Selected or Typed Options
# ===========================================


def display_options():
    # 14.1 Clear the text box
    text_box.delete("1.0", END)

    # 14.2 Get selected options from listbox
    selected_options = [listbox.get(i) for i in listbox.curselection()]

    # 14.3 Get typed option from entry field
    typed_option = entry.get()

    # 14.4 Get value from spinbox
    spinbox_value = spinbox.get()

    # 14.5 Get value from scale
    scale_value = scale.get()

    # 14.6 Get text from multi-line text input
    text_input_content = text.get("1.0", END)

    # 14.7 Get the value of the checkbox and radio button
    checkbox_value = checkbox_var.get()
    radio_value = radio_var.get()

    # 14.8 Add typed option to selected options if it is not empty
    if typed_option:
        selected_options.append(typed_option)

    # 14.9 Add spinbox value, scale value, multi-line text content, checkbox value, and radio button value to selected options
    selected_options.extend(
        [spinbox_value, scale_value, text_input_content, checkbox_value, radio_value]
    )

    # 14.10 Display options in text box
    for option in selected_options:
        text_box.insert(END, str(option) + "\n")


# ===========================================
# 15. Button to Display Options
# ===========================================
button = Button(window, text="Display Options", command=display_options)
# - 15.1 Creates a button labeled "Display Options" that, when clicked, calls the 'display_options' function.
button.pack()
# - 15.2 Adds the button to the window and displays it.

# ===========================================
# 16. Run the Application
# ===========================================
window.mainloop()
# - 16.1 Initiates the Tkinter event loop to keep the GUI application running and responsive to user interactions.
