import re
import math
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 1
        self.a3 = 0
        self.a4 = 0
    def fonk2(self):
        print("Error occurred")
    def fonk3(self, a5):
        b1 = re.compile(r"^[^6]{1,3}", re.I | re.S)
        if b1.match(str(self.a1)):
            return
        if a5 > 12:
            return
        self.fonk2()
    def fonk4(self, a5):
        print("0\n1")
        while self.a3 < a5:
            self.a1, self.a2 = self.a2, self.a1 + self.a2
            self.fonk3(a5)
            print(self.a1)
            self.a3 += 1
if b2 = = "__main__":
    a5 = 15
    b3 = class1()
    b3.fonk4(a5)