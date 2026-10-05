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
    print("Initialized variables: ", a, b)
    return States.FIBONACCI
def fibonacci():
    global a, b
    next_fib = a + b
    b = next_fib
    time.sleep(0.1)
    print("Next Fibonacci number: ", next_fib)
    if next_fib < 620:
        return States.FIBONACCI
    else:
        return States.OFF
def off():
    print("Off state reached.")
def fsm(state):
    switcher = {
        States.OFF: off,
        States.INITIALIZE: initialize,
        States.FIBONACCI: fibonacci
    }
    func = switcher.get(state)
    return func()
def fsm_loop(initial_state):
    current_state = initial_state
    while current_state != States.OFF:
        current_state = fsm(current_state)
if __name__ == "__main__":
    fsm_loop(States.INITIALIZE)