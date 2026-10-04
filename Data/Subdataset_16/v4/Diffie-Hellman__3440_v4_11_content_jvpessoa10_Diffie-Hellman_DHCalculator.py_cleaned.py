from math import sqrt
from itertools import count, islice
import random
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 0
    def fonk2(self, n):
        return n > 1 and all(n % i != 0 for i in islice(count(2), int(sqrt(n) - 1)))
    def fonk3(self, b1 = 1000, max_value=10000):
        b2 = [i for i in range(b1, max_value) if self.fonk2(i)]
        return random.choice(b2)
    def fonk4(self, a1):
        self.a1 = a1
    def fonk5(self, b5, b4):
        return pow(b5, self.a1, b4)
    def fonk6(self, b7, b4):
        return pow(b7, self.a1, b4)
def fonk7():
    b3 = class1()
    b4 = b3.fonk3()
    b5 = random.randint(2, b4 - 1)
    print(f"Generated b4 P: {b4} and b5 G: {b5}")
    a1 = random.randint(1, b4 - 1)
    b3.fonk4(a1)
    print(f"Private key a: {a1}")
    b6 = b3.fonk5(b5, b4)
    print(f"Public value A: {b6}")
    b7 = random.randint(2, b4 - 1)
    print(f"Received public value B: {b7}")
    b8 = b3.fonk6(b7, b4)
    print(f"The shared secret key is: {b8}")
if b9 = = "__main__":
    fonk7()