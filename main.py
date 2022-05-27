#all the import needed
from curses.ascii import isdigit

from secrets import choice
import random
from botturn import BotTurn
#functions to check if it is a win
from check_if_in_4 import checkall
#to check how it wins
from staticvariebles import how_it_ends
#check if board is empty
#fuction for the user turn
from userturn import userturnfunction

#function for the start up code
from start import intro
from start import animation

#function to see what the ending is
from start import Ending

#function for devmode


#function to see if user wants to go into devmode

#The code for intro and startup and animation
animation()
intro()


#The game loop
Game_is_not_finished = False
while Game_is_not_finished == False:
    UserTurn = True
    if UserTurn == True:
        userturnfunction()
        Ending(how_it_ends)
        UserTurn = False
    if UserTurn == False:
        BotTurn()
        Ending(how_it_ends)
