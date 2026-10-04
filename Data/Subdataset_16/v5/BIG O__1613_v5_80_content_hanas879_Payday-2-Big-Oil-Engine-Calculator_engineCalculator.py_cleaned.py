import os
from time import sleep
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2():
    fonk1()
    return input("How many nozzles?: ")
def fonk3():
    fonk1()
    print("Now it's time for the b3")
    print("")
    return input("Type 1 for <, or 2 for >: ")
def fonk4():
    fonk1()
    print("Engine")
    sleep(3)
def fonk5(b2):
    if b2 in ["1", "2"]:
        fonk4()
    elif b2 = = "3":
        b3 = fonk3()
        if b3 in ["1", "2"]:
            fonk4()
        else:
            print("I can't understand that")
            sleep(3)
    else:
        print("I can't understand that")
        sleep(3)
def fonk6():
    b4 = input("What is the b4? e.g: He, N or D: ").lower().replace(" ", "")
    fonk1()
    if b4 in ["he", "n", "d"]:
        b2 = fonk2()
        fonk5(b2)
    else:
        print("Something went wrong! Try again")
        sleep(3)
if b5 = = "__main__":
    fonk6()