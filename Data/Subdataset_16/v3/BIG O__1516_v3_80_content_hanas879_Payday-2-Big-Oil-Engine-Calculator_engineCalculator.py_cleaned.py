import os
import time
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2(prompt):
    b2 = input(prompt).strip().lower().replace(" ", "")
    fonk1()
    return b2
def fonk3(b4):
    b3 = fonk2("How many nozzles?: ")
    if b3 in ["1", "2"]:
        print("Engine")
        time.sleep(3)
    elif b3 = = "3":
        if b4 = = "he":
            print("Engine")
            time.sleep(3)
        else:
            fonk4()
    else:
        print("Invalid number of nozzles.")
        time.sleep(3)
def fonk4():
    b5 = fonk2("Type 1 for <, or 2 for >: ")
    if b5 in ["1", "2"]:
        print("Engine")
        time.sleep(3)
    else:
        print("Invalid input for b5.")
        time.sleep(3)
def fonk5():
    b4 = fonk2("What is the b4? e.g: He, N or D: ")
    if b4 in ["he", "n", "d"]:
        fonk3(b4)
    else:
        print("Invalid b4 input! Try again.")
        time.sleep(3)
if b6 = = "__main__":
    fonk5()
