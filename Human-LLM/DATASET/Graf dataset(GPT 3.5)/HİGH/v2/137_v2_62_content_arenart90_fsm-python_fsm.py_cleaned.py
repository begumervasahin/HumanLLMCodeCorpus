import time
from enum import Enum, auto
class class1(Enum):
    b1 = auto()
    b2 = auto()
    b3 = auto()
b4 = b6 = None
def fonk1():
    global b4, b6
    b4 = b6 = 1
    print(b4)
    print(b6)
    return class1.b2
def fonk2():
    global b4, b6
    b5 = b4 + b6
    b6 = b5
    time.sleep(0.1)
    if b4 + b6 < 620:
        return class1.b2
    else:
        return class1.b3
def fonk3():
    pass
def fonk4(b9):
    b7 = {
        class1.b3: off,
        class1.b1: initialize,
        class1.b2: fibonacci
    }
    b8 = b7.get(b9)
    return b8()
def fonk5(b9):
    while True:
        if b9 = = class1.b3:
            fonk4(b9)
            break
        else:
            b9 = fonk4(b9)
if b10 = = "__main__":
    fonk5(class1.b1)