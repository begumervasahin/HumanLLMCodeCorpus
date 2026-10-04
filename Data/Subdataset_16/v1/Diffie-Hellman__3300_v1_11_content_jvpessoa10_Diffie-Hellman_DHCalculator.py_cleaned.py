from math import sqrt
from itertools import count, islice
import random
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self, n):
        return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))
    def fonk3(self):
        a4 = 1000
        a5 = 10000
        b1 = [i for i in range(a4, a5) if self.fonk2(i)]
        return random.choice([i for i in b1 if a4 < i < a5])
    def fonk4(self, a1):
        self.a1 = a1
    def fonk5(self, b3, a3):
        return b3 ** self.a1 % a3
    def fonk6(self, a2, a3):
        return a2 ** self.a1 % a3
def fonk7():
    b2 = class1()
    a3 = b2.fonk3()
    b3 = random.randint(2, a3 - 1)
    print(f"Generated prime a3: {a3} and base b3: {b3}")
    b4 = random.randint(1, a3 - 1)
    b2.fonk4(b4)
    print(f"Private key a1: {b4}")
    b5 = b2.fonk5(b3, a3)
    print(f"Public value b5: {b5}")
    b6 = random.randint(2, a3 - 1)
    print(f"Received public value a2: {b6}")
    b7 = b2.fonk6(b6, a3)
    print(f"The shared secret key is: {b7}")
if b8 = = "__main__":
    fonk7()