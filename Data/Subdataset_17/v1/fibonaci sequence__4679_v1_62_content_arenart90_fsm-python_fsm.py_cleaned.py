import time
from enum import Enum, auto
class States(Enum):
    INIT = auto()
    FIB = auto()
    OFF = auto()
class FibonacciFSM:
    def __init__(self):
        self.a = 1
        self.b = 1
    def init_state(self):
        self.a = self.b = 1
        print(self.a)
        print(self.b)
        return States.FIB
    def fib_state(self):
        c = self.a + self.b
        print(c)
        self.a = self.b
        self.b = c
        time.sleep(0.1)
        if self.a + self.b < 620:
            return States.FIB
        else:
            return States.OFF
    def off_state(self):
        pass
    def fsm(self, state):
        state_methods = {
            States.INIT: self.init_state,
            States.FIB: self.fib_state,
            States.OFF: self.off_state
        }
        state_method = state_methods.get(state)
        return state_method()
    def run(self, initial_state):
        state = initial_state
        while state != States.OFF:
            state = self.fsm(state)
        self.fsm(state)
if __name__ == "__main__":
    fsm = FibonacciFSM()
    fsm.run(States.INIT)