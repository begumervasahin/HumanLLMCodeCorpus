import os
import sys
b1 = os.path.abspath(__file__)
b2 = os.path.dirname(b1)
sys.path.append(b2)
def fonk1():
    print("[ START PROGRAM ]")
    print(f"Start main file: {b1}")
    print(f"System append path: {b2}")
    from gui.b3 import Application
    b3 = Application(b2)
    b3.mainloop()
if b4 = = "__main__":
    fonk1()