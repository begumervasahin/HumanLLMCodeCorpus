import os
import sys
def fonk1():
    return os.path.abspath(__file__)
def fonk2(b2):
    return os.path.dirname(b2)
def fonk3(b3):
    sys.path.append(b3)
def fonk4(b3):
    from gui.b1 import Application
    b1 = Application(b3)
    b1.mainloop()
def fonk5():
    b2 = fonk1()
    b3 = fonk2(b2)
    fonk3(b3)
    print("[ START PROGRAM ]")
    print(f"Start main file: {b2}")
    print(f"System append path: {b3}")
    fonk4(b3)
if b4 = = "__main__":
    fonk5()