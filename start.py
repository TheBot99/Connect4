import time
from staticvariebles import command
import os

def animation():
  os.system(command)
  print("Welcome to:")
  time.sleep(0.5)
  os.system(command)
  
  print("................................................................................................")
  time.sleep(0.05)
  print("................................................................................................")
  time.sleep(0.05)
  print("................................................................................................")
  time.sleep(0.05)
  print("................................................................................................")
  time.sleep(0.05)

  print("")
  time.sleep(0.05)
  print("")
  time.sleep(0.05)
  
  print(" ........    ........   ......       ...  ......       ...  ...........   ........   ...........")
  time.sleep(0.05)
  print("..........  ..........  ... ...      ...  ... ...      ...  ...........  ..........  ...........")
  time.sleep(0.05)
  print("...         ...    ...  ...  ...     ...  ...  ...     ...  ....         ...             ....   ")
  time.sleep(0.05)
  print("...         ...    ...  ...   ...    ...  ...   ...    ...  ...........  ...             ....   ")
  time.sleep(0.05)
  print("...         ...    ...  ...    ...   ...  ...    ...   ...  ...........  ...             ....   ")
  time.sleep(0.05)
  print("...         ...    ...  ...     ...  ...  ...     ...  ...  ....         ...             ....   ")
  time.sleep(0.05)
  print("..........  ..........  ...      ... ...  ...      ... ...  ...........  ..........      ....   ")
  time.sleep(0.05)
  print(" ........    ........   ...       ......  ...       ......  ...........   ........       ....   ")
  time.sleep(0.05)

  print("")
  time.sleep(0.05)

  print("                                               ......")
  time.sleep(0.05)
  print("                                              ... ...")
  time.sleep(0.05)
  print("                                             ...  ...")
  time.sleep(0.05)
  print("                                            ...   ...")
  time.sleep(0.05)
  print("                                           ...    ...")
  time.sleep(0.05)
  print("                                          ...     ...")
  time.sleep(0.05)
  print("                                          ...........")
  time.sleep(0.05)
  print("                                          ...........")
  time.sleep(0.05)
  print("                                                  ...")
  time.sleep(0.05)
  print("                                                  ...")
  time.sleep(0.05)
  
  print("")
  time.sleep(0.05)
  print("")
  time.sleep(0.05)

  print("................................................................................................")
  time.sleep(0.05)
  print("................................................................................................")
  time.sleep(0.05)
  print("................................................................................................")
  time.sleep(0.05)
  print("................................................................................................")
  time.sleep(0.05)
  
  time.sleep(1)
  
def intro():
    os.system(command)
    want_explanation = input("Do you want an explanation on how to play: y/n: ")
    while want_explanation == "y":
        os.system(command)
        print("This is how to play")
        time.sleep(1.5)
        print("The game is going to ask you what column you want to drop your token into")
        time.sleep(2)
        print("The token won't be a color it will be a number, the players token will be the number 1 and the CPUs token will be the numeber 2")
        time.sleep(3)
        understood =  input("Do you understand how to play now? y/n: ")
        if understood != "y" or "n":
          os.system(command)
          print("That is not an option you have to choose y or n")
          time.sleep(3)
        if understood == "y":
            os.system(command)
            print("Welcome to connect 4")
            want_explanation = False
            time.sleep(2)
        if understood == "n":
            pass

            time.sleep(2)
    if want_explanation == "n":
        os.system(command)
        print("Welcome to Connect 4")
        time.sleep(2)

        
def Ending(how_end):
  if how_end == ["no win"]:
    os.system(command)
    print("Nobody won")
    exit(1)