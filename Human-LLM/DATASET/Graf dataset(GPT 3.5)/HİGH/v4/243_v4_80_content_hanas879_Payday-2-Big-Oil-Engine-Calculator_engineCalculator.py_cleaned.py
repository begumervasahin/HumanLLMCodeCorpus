from time import sleep
import os
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2():
    fonk1()
    b2 = input("What is the b2? e.g: He, N or D: ").lower().replace(" ", "")
    fonk1()
    if b2 = = "he" or b2 == "n" or b2 == "d":
        b3 = input("How many nozzles?: ")
        fonk1()
        if b3 in ["1", "2", "3"]:
            fonk1()
            print("Engine")
            sleep(3)
        else:
            fonk1()
            print("I can't understand that")
            sleep(3)
    else:
        fonk1()
        print("Something went wrong! Try again")
        sleep(3)
if b4 = = "__main__":
    fonk2()