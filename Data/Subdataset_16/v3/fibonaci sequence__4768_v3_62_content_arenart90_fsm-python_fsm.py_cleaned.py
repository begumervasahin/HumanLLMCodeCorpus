import time
from enum import Enum, auto
class class1(Enum):
    b1 = auto()
    b2 = auto()
    b3 = auto()
class class2:
    def fonk1(self):
        self.a1 = 1
        self.a2 = 1
    def fonk2(self):
        self.a1 = 1
        self.a2 = 1
        print(self.a1)
        print(self.a2)
        return class1.b2
    def fonk3(self):
        b4 = self.a1 + self.a2
        print(b4)
        self.a1, self.a2 = self.a2, b4
        time.sleep(0.1)
        return class1.b2 if self.a1 + self.a2 < 620 else class1.b3
    def fonk4(self):
        print("FSM is now b3.")
    def fonk5(self, b6):
        b5 = {
            class1.b1: self.init_state,
            class1.b2: self.fib_state,
            class1.b3: self.off_state
        }
        return b5[b6]()
    def fonk6(self, initial_state):
        b6 = initial_state
        while b6 != class1.b3:
            b6 = self.fonk5(b6)
        self.fonk5(b6)
def fonk7():
    b7 = class2()
    b7.fonk6(class1.b1)
if b8 = = "__main__":
    fonk7()