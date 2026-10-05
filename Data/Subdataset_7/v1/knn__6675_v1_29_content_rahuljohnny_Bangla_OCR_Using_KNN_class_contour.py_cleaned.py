import copy
a1 = 100
class class1():
    b1 = None
    b2 = None
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0.0
    def fonk1(self):
        [intX, intY, intWidth, intHeight] = self.b2
        self.a2 = intX
        self.a3 = intY
        self.a4 = intWidth
        self.a5 = intHeight
    def fonk2(self):
        if self.a6 < a1:
            return False
        return True
    def fonk3(self):
        self.a3 -= 555
def fonk4(init, *args):
    b3 = init
    for x in reversed(args):
        b3 = [copy.deepcopy(b3) for _ in range(x)]
    return b3
if b4 = = "__main__":
    b5 = class1()
    b5.b2 = [10, 20, 30, 40]
    b5.a6 = 200.0
    b5.fonk1()
    print("Initial a3:", b5.a3)
    b5.fonk3()
    print("Adjusted a3:", b5.a3)
    b6 = fonk4(0, 3, 4, 2)
    print("Nested list:", b6)