import os
from time import sleep
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2():
    fonk1()
    return input("How many nozzles?: ")
def fonk3():
    fonk1()
    print("Now it's time for the b4")
    print("")
    return input("Type 1 for <, or 2 for >")
def fonk4():
    fonk1()
    print("Engine")
    sleep(3)
def fonk5():
    b2 = input("What is the b2? e.g: He, N or D: ").lower().replace(" ", "")
    fonk1()
    if b2 = = "he":
        b3 = fonk2()
        if b3 = = "2" or b3 == "3":
            fonk4()
        else:
            print("I can't understand that")
            sleep(3)
    elif b2 = = "n":
        b3 = fonk2()
        if b3 in ["1", "2"]:
            fonk4()
        elif b3 = = "3":
            b4 = fonk3()
            if b4 in ["1", "2"]:
                fonk4()
            else:
                print("I can't understand that")
                sleep(3)
        else:
            print("I can't understand that")
            sleep(3)
    elif b2 = = "d":
        b3 = fonk2()
        if b3 in ["1", "2"]:
            fonk4()
        elif b3 = = "3":
            b4 = fonk3()
            if b4 in ["1", "2"]:
                fonk4()
            else:
                print("I can't understand that")
                sleep(3)
        else:
            print("I can't understand that")
            sleep(3)
    else:
        print("Something went wrong! Try again")
        sleep(3)
if b5 = = "__main__":
    fonk5()