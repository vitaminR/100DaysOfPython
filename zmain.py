import tkinter as tk
from tkinter import simpledialog
import turtle


def setup_root_window():
    root = tk.Tk()
    root.withdraw()
    root.geometry("+0+0")
    return root


def setup_turtle_screen(image):
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    screen.addshape(image)
    return screen


def setup_turtle(image):
    my_turtle = turtle.Turtle()
    my_turtle.shape(image)
    return my_turtle


def get_user_input(root):
    answer_state = simpledialog.askstring(
        title="Guess the State", prompt="Enter a state's name:", parent=root
    )
    return answer_state


def main():
    root = setup_root_window()
    image = "blank_states_img.gif"
    screen = setup_turtle_screen(image)
    my_turtle = setup_turtle(image)
    answer_state = get_user_input(root)
    print(answer_state)
    screen.mainloop()

    while True:
        answer_state = get_user_input(root)
        if game.check_answer(answer_state):
            print(f"Correct! {answer_state} is a state.")
            game.write_state_name(answer_state)
        else:
            print(f"Sorry, {answer_state} is not a state.")


if __name__ == "__main__":
    main()
