from time import sleep
import os
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2():
    fonk1()
    return input("What is the b2? (Enter 'He', 'N', or 'D'): ").lower().replace(" ", "")
def fonk3():
    fonk1()
    return input("How many nozzles? (Enter 1, 2, or 3): ")
def fonk4():
    fonk1()
    print("Engine")
    sleep(3)
def fonk5():
    fonk1()
    print("I can't understand that")
    sleep(3)
def fonk6():
    """
    Function to print "Try again" message.
    """
    fonk1()
    print("Something went wrong! Try again")
    sleep(3)
def fonk7():
    b2 = fonk2()
    if b2 in ["he", "n", "d"]:
        b3 = fonk3()
        if b3 in ["1", "2", "3"]:
            fonk4()
        else:
            fonk5()
    else:
        fonk6()
if b4 = = "__main__":
    fonk7()