from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("1600x1000")
def add1():
   Input = 1
   print(Input)
def add2():
    Input = 2
    print(Input)  
def add3():
   Input = 3
   print(Input)
def add4():
   Input = 4
   print(Input)
def add5():
   Input = 5
   print(Input)
def add6():
   Input = 6
   print(Input)
def add7():
   Input = 7
   print(Input)

B1 = Button(top, text = "Add to column 1", command = add1)
B2 = Button(top, text = "Add to column 2", command = add2)
B3 = Button(top, text = "Add to column 3", command = add3)
B4 = Button(top, text = "Add to column 4", command = add4)
B5 = Button(top, text = "Add to column 5", command = add5)
B6 = Button(top, text = "Add to column 6", command = add6)
B7 = Button(top, text = "Add to column 7", command = add7)

B1.place(x = 0,y = 50)
B2.place(x = 200,y = 50)
B3.place(x = 400,y = 50)
B4.place(x = 600,y = 50)
B5.place(x = 800,y = 50)
B6.place(x = 1000,y = 50)
B7.place(x = 1200,y = 50)

top.mainloop()