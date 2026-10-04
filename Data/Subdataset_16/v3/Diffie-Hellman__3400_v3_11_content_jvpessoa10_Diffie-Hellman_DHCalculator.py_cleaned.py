from math import sqrt
from itertools import count, islice
import random
class class1:
    def fonk1(self):
        self.b1 = None
    @staticmethod
    def fonk2(n):
        return n > 1 and all(n % i != 0 for i in islice(count(2), int(sqrt(n) - 1)))
    def fonk3(self, b2 = 1000, max_n=10000):
        b3 = [i for i in range(b2, max_n) if self.fonk2(i)]
        return random.choice(b3)
    def fonk4(self, b1):
        self.b1 = b1
    def fonk5(self, b6, b5):
        if self.b1 is None:
            raise ValueError("Private key is not set.")
        return pow(b6, self.b1, b5)
    def fonk6(self, b8, b5):
        if self.b1 is None:
            raise ValueError("Private key is not set.")
        return pow(b8, self.b1, b5)
def fonk7():
    b4 = class1()
    b5 = b4.fonk3()
    b6 = random.randint(2, b5 - 1)
    print(f"Generated b5 P: {b5} and b6 G: {b6}")
    b1 = random.randint(1, b5 - 1)
    b4.fonk4(b1)
    print(f"Private key a: {b1}")
    b7 = b4.fonk5(b6, b5)
    print(f"Public value A: {b7}")
    b8 = random.randint(2, b5 - 1)
    print(f"Received public value B: {b8}")
    b9 = b4.fonk6(b8, b5)
    print(f"The shared secret key is: {b9}")
if b10 = = "__main__":
    fonk7()