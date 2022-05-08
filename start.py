import time
def startup():
    print("This is connect 4 in the terminal")
    want_explanation = input("Do you want a explanation on how to play: y/n")
    if want_explanation == "y":
        print("This is how to play")
        time.slepp(0.3)
        print("The game is going to ask you what ")
        