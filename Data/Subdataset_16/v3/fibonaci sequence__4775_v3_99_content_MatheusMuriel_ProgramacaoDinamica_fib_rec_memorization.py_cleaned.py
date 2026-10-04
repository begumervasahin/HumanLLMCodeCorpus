import sys
from Memoria import Cerebro
class class1:
    def fonk1(self, b1 = 10000000, cleaning_rate=0.7):
        self.b2 = Cerebro(b1, cleaning_rate)
    def fonk2(self, b3):
        if b3 = = 0:
            return 0
        if b3 = = 1:
            return 1
        str_n1, b4 = str(b3 - 1), str(b3 - 2)
        b5 = self.b2.get_lembranca(str_n1)
        b6 = self.b2.get_lembranca(b4)
        if b5 = = -1:
            b5 = self.fonk2(b3 - 1)
            self.b2.nova_memoria(str_n1, b5)
        if b6 = = -1:
            b6 = self.fonk2(b3 - 2)
            self.b2.nova_memoria(b4, b6)
        return b5 + b6
    def fonk3(self):
        return lambda b3: self.fonk2(b3)
    def fonk4(self):
        return "Recursive + Memoization"
def fonk5():
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <number>")
        return
    try:
        b3 = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer.")
        return
    b7 = class1()
    b8 = b7.fonk2(b3)
    print(f"Fibonacci number for {b3} is: {b8}")
if b9 = = "__main__":
    fonk5()