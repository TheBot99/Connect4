from staticvariebles import Board
from staticvariebles import how_it_ends
import time
def checkall():
    def check_diagonal():
      User_Counter = 0
      Bot_Counter = 0
      fully_checked = False
      x_axis = 0
      y_axis = 5
      while fully_checked == False:
        if (Board[y_axis, x_axis]) == 1:
          User_Counter = User_Counter + 1
          Bot_Counter = 0
        if (Board[y_axis, x_axis]) == 2:
          Bot_Counter = Bot_Counter + 2
          User_Counter = 0
        if (Board[y_axis, x_axis]) == 0:
          User_Counter = 0
          Bot_Counter = 0
        if User_Counter == 4:
          how_it_ends.append("user")
        if Bot_Counter == 8:
          how_it_ends.append("bot")
        
    def check_vertical():
      User_Counter = 0
      Bot_Counter = 0
      fully_checked = False
      x_axis = 0
      y_axis = 5
      while fully_checked == False:
        if (Board[y_axis, x_axis]) == 1:
          User_Counter = User_Counter + 1
          Bot_Counter = 0
        if (Board[y_axis, x_axis]) == 2:
          Bot_Counter = Bot_Counter + 2
          User_Counter = 0
        if (Board[y_axis, x_axis]) == 0:
          User_Counter = 0
          Bot_Counter = 0
        if User_Counter == 4:
          how_it_ends.append("user")
        if Bot_Counter == 8:
          how_it_ends.append("bot")
        if y_axis >= 1:
          y_axis = y_axis -1
        else:
          User_Counter = 0
          Bot_Counter = 0
          if x_axis <= 5:
            y_axis = 5
            x_axis = x_axis + 1
          else:
            fully_checked = True         
    def check_horizontal():
      User_Counter = 0
      Bot_Counter = 0
      fully_checked = False
      x_axis = 0
      y_axis = 5
      while fully_checked == False:
        if (Board[y_axis, x_axis]) == 1:
          User_Counter = User_Counter + 1
          Bot_Counter = 0
        if (Board[y_axis, x_axis]) == 2:
          Bot_Counter = Bot_Counter + 2
          User_Counter = 0
        if (Board[y_axis, x_axis]) == 0:
          User_Counter = 0
          Bot_Counter = 0
        if User_Counter == 4:
          how_it_ends.append("user")
        if Bot_Counter == 8:
          how_it_ends.append("bot")
        if x_axis <= 5:
          x_axis = x_axis + 1
        else:
          User_Counter = 0
          Bot_Counter = 0
          if y_axis >= 1:
            x_axis = 0
            y_axis = y_axis - 1
          else:
            fully_checked = True
    check_diagonal()
    check_horizontal()
    check_vertical()