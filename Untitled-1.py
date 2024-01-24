import pandas as pd
import turtle


class Game:
    def __init__(self, csv_file):
        self.states = pd.read_csv(csv_file)

    def check_answer(self, answer):
        return answer in self.states["state"].values.tolist()

    # get state coordinates
    def get_state_coordinates(self, state):
        state_data = self.states[self.states["state"] == state]
        return (int(state_data["x"]), int(state_data["y"]))

    # write state name on map
    def write_state_name(self, state):
        state_data = self.states[self.states["state"] == state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state)
