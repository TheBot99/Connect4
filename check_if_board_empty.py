from staticvariebles import Board
from staticvariebles import how_it_ends
def check_empty():
    open = []
    if (Board[0, 0]) == 0:
        open.append(0)
    if (Board[0, 1]) == 0:
        open.append(1)
    if (Board[0, 2]) == 0:
        open.append(2)
    if (Board[0, 3]) == 0:
        open.append(3)
    if (Board[0, 4]) == 0:
        open.append(4)
    if (Board[0, 5]) == 0:
        open.append(5)
    if (Board[0, 6]) == 0:
        open.append(6)
    
    if open == []:
        how_it_ends