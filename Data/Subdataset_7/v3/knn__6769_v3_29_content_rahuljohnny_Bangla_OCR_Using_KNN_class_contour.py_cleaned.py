import copy
a1 = 100
class class1():
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
        self.a6 = 0.0
    def fonk2(self):
        intX, intY, intWidth, b3 = self.b2
        self.a2 = intX
        self.a3 = intY
        self.a4 = intWidth
        self.a5 = b3
    def fonk3(self):
        return self.a6 >= a1
    def fonk4(self):
        self.a3 -= 555
def fonk5(init, *args):
    b4 = init
    for x in reversed(args):
        b4 = [copy.deepcopy(b4) for _ in range(x)]
    return b4
if b5 = = "__main__":
    b6 = class1()
    b6.b2 = [10, 20, 30, 40]
    b6.a6 = 200.0
    b6.fonk2()
    print("Initial a3:", b6.a3)
    b6.fonk4()
    print("Adjusted a3:", b6.a3)
    b7 = fonk5(0, 3, 4, 2)
    print("Nested list:", b7)