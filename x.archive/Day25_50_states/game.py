import pandas as pd
import turtle


class Game:
    def __init__(self, csv_file):
        self.states = pd.read_csv(csv_file)

    def check_answer(self, answer):
        return (
            answer in self.states["state"].values.tolist()
            or answer.upper() in self.states["abbreviation"].values.tolist()
        )

    # get state coordinates
    def get_state_coordinates(self, answer):
        if answer.upper() in self.states["abbreviation"].values.tolist():
            state_data = self.states[self.states["abbreviation"] == answer.upper()]
        else:
            state_data = self.states[self.states["state"] == answer]
        return (int(state_data["x"]), int(state_data["y"]))

    def write_state_name(self, answer):
        if answer.upper() in self.states["abbreviation"].values.tolist():
            state_data = self.states[self.states["abbreviation"] == answer.upper()]
        else:
            state_data = self.states[self.states["state"] == answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data["state"].values[0])
