from curses.ascii import isdigit
import os
command  = 'clear'
os.system(command)
import numpy as np
import time
command  = 'clear'
sleep_time = 2

Board = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

Decision_In_Making = False
while Decision_In_Making == False:
    Decision = "Undefined"
    print(Board)
    User_Input = input(
        "What is the column number that you want to drop into: ")
    if User_Input == "stop":
        Decision_In_Making = True
    else:
        is_that_an_integer  = User_Input.isdigit()
        if is_that_an_integer == True:
            User_Input = int(User_Input)
            if User_Input > 7:
                print("Thats column does not exist")
                time.sleep(sleep_time)
            else:
                counter_upper = 5
                User_Input = User_Input - 1
                not_placed = True
                while not_placed == True:
                    if (Board[counter_upper, User_Input]) == 0:
                        (Board[counter_upper, User_Input]) = 1
                        not_placed = False
                    else:
                        if counter_upper > 0:
                            counter_upper = counter_upper - 1
                        else:
                            print("That Column is full")
                            time.sleep(sleep_time)
                            not_placed = False
        else:
            print("That is not a number")
            time.sleep(sleep_time)
            
        os.system(command)
if Decision != "Win" or "Loose":
    print("You ended the game early")