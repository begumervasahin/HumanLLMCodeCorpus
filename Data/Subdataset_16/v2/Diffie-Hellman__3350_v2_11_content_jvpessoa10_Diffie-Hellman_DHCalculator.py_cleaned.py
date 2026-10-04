from math import sqrt
from itertools import count, islice
import random
class class1:
    def fonk1(self):
        self.a1 = 0
    def fonk2(self, n):
        return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))
    def fonk3(self):
        a2 = 1000
        a3 = 10000
        b1 = [i for i in range(a2, a3) if self.fonk2(i)]
        return random.choice(b1)
    def fonk4(self, a1):
        self.a1 = a1
    def fonk5(self, b4, b3):
        return pow(b4, self.a1, b3)
    def fonk6(self, b6, b3):
        return pow(b6, self.a1, b3)
def fonk7():
    b2 = class1()
    b3 = b2.fonk3()
    b4 = random.randint(2, b3 - 1)
    print(f"Generated b3 P: {b3} and b4 G: {b4}")
    a1 = random.randint(1, b3 - 1)
    b2.fonk4(a1)
    print(f"Private key a: {a1}")
    b5 = b2.fonk5(b4, b3)
    print(f"Public value A: {b5}")
    b6 = random.randint(2, b3 - 1)
    print(f"Received public value B: {b6}")
    b7 = b2.fonk6(b6, b3)
    print(f"The shared secret key is: {b7}")
if b8 = = "__main__":
    fonk7()