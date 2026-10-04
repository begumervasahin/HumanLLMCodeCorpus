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
        self.a, self.b = 1, 1
        print(self.a)
        print(self.b)
        return States.FIB
    def fib_state(self):
        c = self.a + self.b
        print(c)
        self.a, self.b = self.b, c
        time.sleep(0.1)
        return States.FIB if self.a + self.b < 620 else States.OFF
    def off_state(self):
        print("FSM is now OFF.")
    def run_state(self, state):
        state_methods = {
            States.INIT: self.init_state,
            States.FIB: self.fib_state,
            States.OFF: self.off_state
        }
        return state_methods[state]()
    def run(self, initial_state):
        state = initial_state
        while state != States.OFF:
            state = self.run_state(state)
        self.off_state()
def main():
    fsm = FibonacciFSM()
    fsm.run(States.INIT)
if __name__ == "__main__":
    main()