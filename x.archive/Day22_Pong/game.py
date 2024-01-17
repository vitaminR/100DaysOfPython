# game.py
"""game module for pong game"""

import random
from gear import Paddle


class Game:
    def __init__(self, left_paddle, right_paddle, ball):
        self.is_game_on = False
        self.rounds_played = 0
        self.paddle_l = left_paddle
        self.paddle_r = right_paddle
        print("Game initialized")  # Print statement for initialization
        self.ball = ball

    def start(self):
        self.is_game_on = True
        print("Game has started")  # Print statement for game start

    def scoring_event_detected(self):
        # For now, this method just returns False. You should replace this with your own logic.
        return False

    def play_game(self):
        if self.is_game_on:
            self.ball.move()
            print("Playing round:", self.rounds_played)
            self.rounds_played += 1
            # Additional game logic goes here

            if self.rounds_played >= 10:
                self.is_game_on = False
                print("Game has stopped after 10 rounds")  # Game stop condition
                # Check for a scoring event to advance the round
        if self.scoring_event_detected():
            self.rounds_played += 1
            if self.rounds_played >= 10:
                self.is_game_on = False

    def stop_game(self):
        self.is_game_on = False
        print("Game has been stopped manually")  # Manual stop
