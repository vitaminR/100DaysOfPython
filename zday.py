'''#100DaysOfPython Day16'''
# pylint: disable=global-variable-not-assigned
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from prettytable import PrettyTable
from data.art import *
from data.game_data import *


#import turtle
from turtle import Screen, Turtle
from random import randint, choice

# make a basic turtle movement
tim = Turtle()
tim.shape("turtle")
tim.color("DarkSeaGreen4")
tim.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

table = PrettyTable()
    
print(table)


