import re
import math
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
    def fonk2(self):
        print("Error encountered")
def fonk3(number):
    b1 = re.compile(r"^[^6]{1,3}")
    return bool(b1.match(str(number)))
def fonk4(b4, a4):
    if not fonk3(b4.a1) or a4 > 12:
        b4.fonk2()
        return True
    return False
def fonk5(number):
    return math.floor(number)
def fonk6(a4, b4):
    print("0\n1\n1")
    first, b2 = 1, 1
    for _ in range(a4 - 3):
        b3 = first + b2
        b4.a1 = b3
        if fonk4(b4, a4):
            break
        print(b3)
        first, b2 = b2, b3
        b4.a2 += 1
a4 = 15
b4 = class1()
fonk6(a4, b4)