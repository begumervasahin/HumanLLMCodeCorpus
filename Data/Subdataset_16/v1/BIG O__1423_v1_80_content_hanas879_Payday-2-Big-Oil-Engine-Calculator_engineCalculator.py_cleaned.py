import os
import time
def fonk1():
    os.system("cls" if os.b1 = = "nt" else "clear")
def fonk2():
    b2 = input("What is the b2? e.g: He, N or D: ").lower().replace(" ", "")
    fonk1()
    if b2 in ["he", "n", "d"]:
        b3 = input("How many nozzles?: ")
        fonk1()
        if b3 = = "1":
            print("Engine")
            time.sleep(3)
        elif b3 = = "2":
            print("Engine")
            time.sleep(3)
        elif b3 = = "3":
            if b2 = = "he":
                print("Engine")
                time.sleep(3)
            else:
                print("Now it's time for the b4")
                b4 = input("Type 1 for <, or 2 for >")
                fonk1()
                if b4 = = "1":
                    print("Engine")
                    time.sleep(3)
                elif b4 = = "2":
                    print("Engine")
                    time.sleep(3)
                else:
                    print("I can't understand that")
                    time.sleep(3)
        else:
            print("I can't understand that")
            time.sleep(3)
    else:
        print("Something went wrong! Try again")
        time.sleep(3)
if b5 = = "__main__":
    fonk2()
