import time
from enum import Enum, auto
class States(Enum):
    INITIALIZE = auto()
    FIBONACCI = auto()
    OFF = auto()
a = b = None
def initialize():
    global a, b
    a = b = 1
    print(a)
    print(b)
    return States.FIBONACCI
def fibonacci():
    global a, b
    c = a + b
    b = c
    time.sleep(0.1)
    if a + b < 620:
        return States.FIBONACCI
    else:
        return States.OFF
def off():
    pass
def fsm(state):
    switcher = {
        States.OFF: off,
        States.INITIALIZE: initialize,
        States.FIBONACCI: fibonacci
    }
    func = switcher.get(state)
    return func()
def fsm_loop(state):
    while True:
        if state == States.OFF:
            fsm(state)
            break
        else:
            state = fsm(state)
if __name__ == "__main__":
    fsm_loop(States.INITIALIZE)