from staticvariebles import command
from staticvariebles import how_it_ends
from check_if_board_empty import check_empty
from check_if_in_4 import checkall
import os
from staticvariebles import Board
from secrets import choice
Useable_Numbers = []

def BotTurn():
    check_empty()
    checkall()
    Useable_Numbers = []
    x = 5
    os.system(command)
    #find usable numbers
    if (Board[0, 0]) == 0:
        Useable_Numbers.append(0)
    if (Board[0, 1]) == 0:
        Useable_Numbers.append(1)
    if (Board[0, 2]) == 0:
        Useable_Numbers.append(2)
    if (Board[0, 3]) == 0:
        Useable_Numbers.append(3)
    if (Board[0, 4]) == 0:
        Useable_Numbers.append(4)
    if (Board[0, 5]) == 0:
        Useable_Numbers.append(5)
    if (Board[0, 6]) == 0:
        Useable_Numbers.append(6)

    #computation
    #just for now until I learn A.I.
    bot_number = choice(Useable_Numbers)
    placing = True
    while placing == True:
        if (Board[x, bot_number]) == 0:
            (Board[x, bot_number]) = 2
            placing = False
        else:
            x = x-1

   
    #just printing and moving on
    print("This is the bot turn")
    print(Board)
    check_empty()
    checkall()
    input("Press Enter to move on ")