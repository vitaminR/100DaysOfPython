from tkinter import *

# ===========================================
# 1. Importing the Tkinter Library
# ===========================================
from tkinter import *

# - 1.1 Imports all classes, functions, and variables from the Tkinter library, enabling GUI creation.

# ===========================================
# 2. Creating the Main Window
# ===========================================
window = Tk()
# - 2.1 Initializes the Tkinter window.
window.title("Widget Examples")
# - 2.2 Sets the title of the main window.
window.minsize(width=500, height=500)
# - 2.3 Defines the minimum size of the window to ensure all elements fit.

# ===========================================
# 3. Label Widget
# ===========================================
label = Label(window, text="This is old text")
# - 3.1 Creates a label with initial text.
label.config(text="This is new text")
# - 3.2 Updates the text of the label to "This is new text".
label.pack()
# - 3.3 Adds the label to the window using the pack geometry manager.


# ===========================================
# 4. Button Widget
# ===========================================
def action():
    print("Do something")
    # - 4.1 Defines a function that prints a message when the button is clicked.


button = Button(window, text="Click Me", command=action)
# - 4.2 Creates a button that, when clicked, calls the 'action' function.
button.pack()
# - 4.3 Adds the button to the window and makes it visible.

# ===========================================
# 5. Entry Widget
# ===========================================
entry = Entry(window, width=30)
# - 5.1 Creates an entry widget for text input. The 'window' parameter is the parent widget where this Entry widget will be placed.
# - 5.1.1 The 'width' parameter specifies the width of the Entry widget in characters.

entry.insert(END, "Some text to begin with.")
# - 5.2 Inserts a default string into the entry widget. The 'END' constant imported from tkinter represents the end of the text area.
# - 5.2.1 This means the text will be inserted at the end of the current text, which is useful when you want to append text to an Entry widget.

entry.pack()
# - 5.3 Adds the entry widget to the window. The pack() method is one of the three geometry managers in tkinter.
# - 5.3.1 It organizes widgets in blocks before placing them in the parent widget.

# ===========================================
# 6. Text Widget (Multi-line Text Entry)
# ===========================================
text = Text(window, height=4, width=30)
# - 6.1 Creates a text widget for multi-line text input. The 'window' parameter is the parent widget where this Text widget will be placed.
# - 6.1.1 The 'height' parameter specifies the height of the Text widget in lines (not pixels).
# - 6.1.2 The 'width' parameter specifies the width of the Text widget in characters.

text.insert(END, "Example of multi-line text entry.")
# - 6.2 Pre-populates the text widget with a sample text. The 'END' constant imported from tkinter represents the end of the text area.
# - 6.2.1 This means the text will be inserted at the end of the current text, which is useful when you want to append text to a Text widget.

text.pack()
# - 6.3 Displays the text widget in the window. The pack() method is one of the three geometry managers in tkinter.
# - 6.3.1 It organizes widgets in blocks before placing them in the parent widget.
# ===========================================


# ===========================================
# 7. Spinbox Widget
# ===========================================
def spinbox_used():
    print(spinbox.get())
    # - 7.1 Function to print the current value of the spinbox when adjusted.


spinbox = Spinbox(window, from_=0, to=10, width=5, command=spinbox_used)
# - 7.2 Creates a spinbox for numeric input.
spinbox.pack()
# - 7.3 Adds the spinbox to the window.


# ===========================================
# 8. Scale Widget
# ===========================================
def scale_used(value):
    print(value)
    # - 8.1 Function to print the value of the scale when it's changed.


scale = Scale(window, from_=0, to=100, command=scale_used)
# - 8.2 Creates a scale (slider) to select a value from a range.
scale.pack()
# - 8.3 Adds the scale to the window.

# ===========================================
# 9. Checkbutton Widget
# ===========================================
checked_state = StringVar(value="Unchecked")
# - 9.1 Initializes the variable to hold the state of the checkbutton.


def checkbutton_used():
    print(checked_state.get())
    # - 9.2 Function to print the current state of the checkbutton.


checkbutton = Checkbutton(
    window,
    text="Is On?",
    variable=checked_state,
    onvalue="Checked",
    offvalue="Unchecked",
    command=checkbutton_used,
)
# - 9.3 Creates a checkbutton with specified on/off values.
checkbutton.pack()
# - 9.4 Adds the checkbutton to the window.

# ===========================================
# 10. Radiobutton Widget
# ===========================================
radio_state = StringVar(value="Option 1 Selected")
# - 10.1 Initializes the variable to hold the selected value among radiobuttons. and sets defualt value.


def radio_used():
    print(radio_state.get())
    # - 10.2 Function to print the selected radiobutton's value.


radiobutton1 = Radiobutton(
    window,
    text="Option1",
    value="Option 1 Selected",
    variable=radio_state,
    command=radio_used,
)
radiobutton2 = Radiobutton(
    window,
    text="Option2",
    value="Option 2 Selected",
    variable=radio_state,
    command=radio_used,
)
# - 10.3 Creates two radiobuttons bound to the same variable but with different values.
radiobutton1.pack()
radiobutton2.pack()
# - 10.4 Adds the radiobuttons to the window.


# ===========================================
# 11. Listbox Widget
# ===========================================
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
    # - 11.1 Function to print the selection from the listbox.


listbox = Listbox(window, height=4)
# - 11.2 Creates a listbox to display a list of items.
for item in ["Apple", "Pear", "Orange", "Banana"]:
    listbox.insert(END, item)
    # - 11.3 Populates the listbox with items.
listbox.bind("<<ListboxSelect>>", listbox_used)
# - 11.4 Binds an event to the listbox to handle item selection.
listbox.pack()
# - 11.5 Adds the listbox to the window.

# ===========================================
# 13. Text Box for Displaying Selected or Typed Options
# ===========================================
text_box = Text(window)
# - 13.1 Creates a text box to display selected or typed options.
text_box.pack()
# - 13.2 Adds the text box to the window for display.


# ===========================================
# 14. Function to Display Selected or Typed Options
# ===========================================
def display_options():
    text_box.delete("1.0", END)
    # - 14.1 Clears the text box for new inputs.

    # Gathering inputs from various widgets:
    selected_options = [
        listbox.get(i) for i in listbox.curselection()
    ]  # Listbox selections
    typed_option = entry.get()  # Entry widget text
    multilinetext = text.get("1.0", END)  # Multiline text
    spinbox_value = spinbox.get()  # Spinbox value
    scale_value = scale.get()  # Scale value
    checkbox_value = checked_state.get()  # Checkbutton state
    radio_value = radio_state.get()  # Radiobutton selection

    # Compiling all selections and inputs:
    compiled_inputs = [
        typed_option,
        multilinetext,
        f"Spinbox: {spinbox_value}",
        f"Scale: {scale_value}",
        f"Checkbutton: {checkbox_value}",
        f"Radiobutton: {radio_value}",
    ] + selected_options

    # Displaying compiled inputs in the text box:
    for input in compiled_inputs:
        text_box.insert(END, input + "\n")


# ===========================================
# 15. Button to Display Options
# ===========================================
button = Button(window, text="Display Options", command=display_options)
button.pack()
# - 15.1 Creates and displays a button that triggers the display_options function.

# ===========================================
# 16. Run the Application
# ===========================================
window.mainloop()
# - 16.1 Starts the Tkinter event loop, keeping the application responsive.
