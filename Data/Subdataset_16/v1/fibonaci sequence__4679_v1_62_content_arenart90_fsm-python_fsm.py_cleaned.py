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
        self.a1 = self.a2 = 1
        print(self.a1)
        print(self.a2)
        return class1.b2
    def fonk3(self):
        b4 = self.a1 + self.a2
        print(b4)
        self.a1 = self.a2
        self.a2 = b4
        time.sleep(0.1)
        if self.a1 + self.a2 < 620:
            return class1.b2
        else:
            return class1.b3
    def fonk4(self):
        pass
    def fonk5(self, b7):
        b5 = {
            class1.b1: self.init_state,
            class1.b2: self.fib_state,
            class1.b3: self.off_state
        }
        b6 = b5.get(b7)
        return b6()
    def fonk6(self, initial_state):
        b7 = initial_state
        while b7 != class1.b3:
            b7 = self.fonk5(b7)
        self.fonk5(b7)
if b8 = = "__main__":
    b9 = class2()
    b9.fonk6(class1.b1)