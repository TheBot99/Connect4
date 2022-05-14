from staticvariebles import command
import os
from staticvariebles import Board
from secrets import choice
from staticvariebles import Useable_Numbers

def BotTurn():
    x = 5
    os.system(command)
    #computation
    #just for now until I learn A.I.
    bot_number = choice(Useable_Numbers)
    if (Board[0, bot_number]) == 0:
        placing = True
        while placing == True:
            if (Board[x, bot_number]) == 0:
                (Board[x, bot_number]) = 2
                placing = False
            else:
                x = x-1

    else:
        BotTurn()
    #just printing and moving on
    print("This is the bot turn")
    print(Board)
    input("Press Enter to move on ")