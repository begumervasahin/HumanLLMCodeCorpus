from math import sqrt
from itertools import count, islice
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self,n):
        return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    def fonk3(self):
        import random
        a4 = 1000
        a5 = 10000
        b1 = [i for i in range(a4,a5) if self.fonk2(i)]
        return random.choice([i for i in b1 if a4<i<a5])
    def fonk4(self,a1):
        self.a1 = a1
    def fonk5(self,G,a3):
        return G**self.a1%a3
    def fonk6(self,a2,a3):
        return a2**self.a1%self.a3