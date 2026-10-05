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
    print("Initialized with values: ", b4, b6)
    return class1.b2
def fonk2():
    global b4, b6
    b5 = b4 + b6
    print("Next Fibonacci number: ", b5)
    b4, b6 = b6, b5
    time.sleep(0.1)
    return class1.b2 if b4 + b6 < 620 else class1.b3
def fonk3():
    print("Off state reached.")
def fonk4(state):
    b7 = {
        class1.b3: off,
        class1.b1: initialize,
        class1.b2: fibonacci
    }
    return b7[state]()
def fonk5(initial_state):
    b8 = initial_state
    while b8 != class1.b3:
        b8 = fonk4(b8)
if b9 = = "__main__":
    fonk5(class1.b1)