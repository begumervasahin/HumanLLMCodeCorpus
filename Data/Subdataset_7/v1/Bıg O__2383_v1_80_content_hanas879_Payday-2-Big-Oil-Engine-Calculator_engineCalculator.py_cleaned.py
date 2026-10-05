from time import sleep
import os
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2(b2):
    if b2 = = "2":
        print("Engine with 2 nozzles")
    elif b2 = = "3":
        print("Engine with 3 nozzles")
    else:
        print("I can't understand that")
def fonk3(b2, b3):
    if b2 = = "3":
        print("Now it's time for the b3:")
        if b3 = = "1":
            print("Pressure is less than")
        elif b3 = = "2":
            print("Pressure is greater than")
        else:
            print("I can't understand that")
    else:
        print("I can't understand that")
def fonk4():
    fonk1()
    b4 = input("What is the b4? e.g: He, N or D: ").lower().replace(" ", "")
    fonk1()
    if b4 = = "he":
        b2 = input("How many nozzles?: ")
        fonk1()
        fonk2(b2)
    elif b4 = = "n":
        b2 = input("How many nozzles?: ")
        fonk1()
        if b2 = = "1" or b2 == "2":
            fonk2(b2)
        elif b2 = = "3":
            b3 = input("Type 1 for <, or 2 for >: ")
            fonk1()
            fonk3(b2, b3)
        else:
            print("I can't understand that")
    elif b4 = = "d":
        b2 = input("How many nozzles?: ")
        fonk1()
        if b2 = = "1" or b2 == "2":
            fonk2(b2)
        elif b2 = = "3":
            b3 = input("Type 1 for <, or 2 for >: ")
            fonk1()
            fonk3(b2, b3)
        else:
            print("I can't understand that")
    else:
        print("Something went wrong! Try again")
    sleep(3)
if b5 = = "__main__":
    fonk4()