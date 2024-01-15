import random


class Game:
    def __init__(self):
        self.is_game_on = False
        print("game is init")
        self.rounds_played = 0

    def start(self):
        self.is_game_on = True
        print("game has started")

    def play_game(self):
        if self.is_game_on:
            print("game is on")
            print(random)
            self.rounds_played += 1

            # Stop the game after 10 rounds
            if self.rounds_played >= 10:
                self.is_game_on = False
                print("game has stopped")
        else:
            print("game is not on")

    def stop_game(self):
        self.is_game_on = False
        print("game has stopped")
