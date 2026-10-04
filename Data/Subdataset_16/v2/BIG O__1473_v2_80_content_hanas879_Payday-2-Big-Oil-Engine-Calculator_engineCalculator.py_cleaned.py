import os
import time
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2(prompt):
    b2 = input(prompt).strip().lower().replace(" ", "")
    fonk1()
    return b2
def fonk3():
    b3 = fonk2("What is the b3? e.g: He, N or D: ")
    if b3 in ["he", "n", "d"]:
        b4 = fonk2("How many nozzles?: ")
        if b4 in ["1", "2"]:
            print("Engine")
            time.sleep(3)
        elif b4 = = "3":
            if b3 = = "he":
                print("Engine")
                time.sleep(3)
            else:
                b5 = fonk2("Type 1 for <, or 2 for >")
                if b5 in ["1", "2"]:
                    print("Engine")
                    time.sleep(3)
                else:
                    print("Invalid input for b5.")
                    time.sleep(3)
        else:
            print("Invalid number of nozzles.")
            time.sleep(3)
    else:
        print("Invalid b3 input! Try again.")
        time.sleep(3)
if b6 = = "__main__":
    fonk3()
