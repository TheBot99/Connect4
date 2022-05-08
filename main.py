#all the import needed
from curses.ascii import isdigit

from secrets import choice
import time
import random
#functions to check if it is a win
from check_if_in_4 import check_horizontal
from check_if_in_4 import check_vertical
from check_if_in_4 import check_diagonal

#fuction for the user turn
from userturn import userturnfunction

#function for the start up code
from start import startup

#The code for intro and startup
startup()

#The game loop
Game_is_not_finished = False
while Game_is_not_finished == False:
    UserTurn = True
    if UserTurn == True:
        userturnfunction()
        UserTurn = False