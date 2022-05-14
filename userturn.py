#imports
from curses.ascii import isdigit
from staticvariebles import command
from staticvariebles import Board
import os
import time
#function
def userturnfunction():
    os.system(command)
    x = 5
    print(Board)
    UserNumb = input("What is the Column That you want to drop a coin into: ")
    if isdigit(UserNumb) == True:
      UserNumb = int(UserNumb)
      UserNumb = UserNumb - 1
      if (Board[0, UserNumb]) == 0:
        if UserNumb < 7 and UserNumb > -1:
          os.system(command)
          placing = True
          while placing  == True:
            if (Board[x, UserNumb]) == 0:
              (Board[x, UserNumb]) = 1
              print(Board)
              placing = False
            else:
                x = x-1
        else:
          print("That is not a column on the Connect 4 board")
          time.sleep(3)
          userturnfunction()
      else:
        print("That column if full")
        time.sleep(2)
        userturnfunction()
    else:
      print("That is not a number")
      time.sleep(3)
      userturnfunction()

