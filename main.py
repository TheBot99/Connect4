#all the import needed
from curses.ascii import isdigit

from secrets import choice
import time
import random
from botturn import BotTurn
#functions to check if it is a win
from check_if_in_4 import check_horizontal
from check_if_in_4 import check_vertical
from check_if_in_4 import check_diagonal

#fuction for the user turn
from userturn import userturnfunction

#function for the start up code
from start import intro
from start import animation

#The code for intro and startup and animation
animation()
intro()

#The game loop
Game_is_not_finished = False
while Game_is_not_finished == False:
    UserTurn = True
    if UserTurn == True:
        userturnfunction()
        UserTurn = False
    if UserTurn == False:
        BotTurn()
