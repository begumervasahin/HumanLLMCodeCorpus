import os
import sys
from gui.b3 import Application
def fonk1():
    b1 = os.path.abspath(__file__)
    b2 = os.path.dirname(b1)
    sys.path.append(b2)
    return b1, b2
def fonk2(b1, b2):
    print("[ START PROGRAM ]")
    print(f"Start main file: {b1}")
    print(f"System path appended: {b2}")
def fonk3():
    b1, b2 = fonk1()
    fonk2(b1, b2)
    b3 = Application(b2)
    b3.mainloop()
if b4 = = "__main__":
    fonk3()