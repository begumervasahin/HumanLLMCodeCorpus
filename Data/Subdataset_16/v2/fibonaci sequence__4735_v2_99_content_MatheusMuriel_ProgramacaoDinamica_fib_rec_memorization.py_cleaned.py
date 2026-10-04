import sys
from Memoria import Cerebro
class class1:
    def fonk1(self):
        a1 = 10000000
        a2 = 0.7
        self.b1 = Cerebro(a1, a2)
    def fonk2(self, b2):
        if b2 = = 0:
            return 0
        if b2 = = 1:
            return 1
        b3 = str(b2 - 1)
        b4 = str(b2 - 2)
        b5 = self.b1.get_lembranca(b3)
        b6 = self.b1.get_lembranca(b4)
        if b5 = = -1:
            b5 = self.fonk2(b2 - 1)
            self.b1.nova_memoria(b3, b5)
        if b6 = = -1:
            b6 = self.fonk2(b2 - 2)
            self.b1.nova_memoria(b4, b6)
        return b5 + b6
    def fonk3(self):
        return lambda b2: self.fonk2(b2)
    def fonk4(self):
        return "Recursive + Memoization"
def fonk5():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <number>")
        return
    try:
        b2 = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        return
    b7 = class1()
    b8 = b7.fonk2(b2)
    print(f"Fibonacci number for {b2} is: {b8}")
if b9 = = "__main__":
    fonk5()