from curses.ascii import isdigit
import os
from secrets import choice
command  = 'clear'
os.system(command)
import numpy as np
import time
import random
sleep_time = 2
Useable_Numbers = (1, 2, 3, 4, 5, 6, 7)

Board = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

Decision_In_Making = False
while Decision_In_Making == False:
    Decision = "Undefined"
    User_Has_Turn = True
    while User_Has_Turn == True:
        print(Board)
        #Asking for user input and checking if it is to stop
        User_Input = input(
            "What is the column number that you want to drop into: ")
        if User_Input == "stop":
            Decision_In_Making = True
        else:
            #Checking if User input is an integer so it don't crash when converted into integer
            is_that_an_integer  = User_Input.isdigit()
            if is_that_an_integer == True:
                User_Input = int(User_Input)
                #Checking if the column exists so it don't crash
                if User_Input > 7:
                    print("Thats column does not exist")
                    time.sleep(sleep_time)
                    os.system(command)
                else:
                    #If the column does exist then try and place it in first spot then go up and up
                    counter_upper = 5
                    User_Input = User_Input - 1
                    not_placed = True
                    while not_placed == True:
                        if (Board[counter_upper, User_Input]) == 0:
                            (Board[counter_upper, User_Input]) = 1
                            not_placed = False
                            #To set it so the bot has the next turn
                            User_Has_Turn = False
                            os.system(command)
                        else:
                            #This is the code to make the coin go up and up
                            if counter_upper > 0:
                                counter_upper = counter_upper - 1
                            else:
                                #If it can't go any higher then tell the player that column is full
                                print("That Column is full")
                                time.sleep(sleep_time)
                                os.system(command)
                                not_placed = False
            else:
                print("That is not a number")
                time.sleep(sleep_time)
                os.system(command)
    while User_Has_Turn == False:
        Bot_Board_Counterupper = 5
        print("Bot turn")
        Bot_Turn = True
        while Bot_Turn == True:
          Bot_Board_Counterupper = 5
          rand_Bot_Numb = choice(Useable_Numbers)
          rand_Bot_Numb = rand_Bot_Numb - 1
          if (Board[Bot_Board_Counterupper, rand_Bot_Numb]) == 0:
              (Board[Bot_Board_Counterupper, rand_Bot_Numb]) = 2    
              print(Board)
              time.sleep(sleep_time)
              os.system(command)
              Bot_Turn = False
              User_Has_Turn = True
          else:
              if Bot_Board_Counterupper > 0:
                  Bot_Board_Counterupper = Bot_Board_Counterupper - 1   
              else: Bot_Turn = False

if Decision == "Win" or "Loose":
    os.system(command)
    print("You" + Decision )
else:
    os.system(command)
    print("You ended the game to early")