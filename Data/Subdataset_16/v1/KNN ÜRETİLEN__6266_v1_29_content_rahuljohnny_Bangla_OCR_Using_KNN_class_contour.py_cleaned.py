import copy
a1 = 100
class class1:
    def fonk1(self):
        self.b1 = None
        self.b2 = None
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.a5 = 0
        self.a6 = 0.0
    def fonk2(self):
        [intX, intY, intWidth, intHeight] = self.b2
        self.a2 = intX
        self.a3 = intY
        self.a4 = intWidth
        self.a5 = intHeight
    def fonk3(self):
        if self.a6 < a1:
            return False
        return True
    def fonk4(self, adjustment):
        self.a3 -= adjustment
def fonk5(init, *args):
    b3 = init
    for x in reversed(args):
        b3 = [copy.deepcopy(b3) for _ in range(x)]
    return b3
if b4 = = "__main__":
    b5 = class1()
    b5.b2 = [50, 100, 200, 300]
    b5.a6 = 150.0
    b5.fonk2()
    print(f"Rectangle X: {b5.a2}, Y: {b5.a3}, Width: {b5.a4}, Height: {b5.a5}")
    b6 = b5.fonk3()
    print(f"Is Contour Valid? {'Yes' if b6 else 'No'}")
    b5.fonk4(555)
    print(f"Adjusted Rectangle Y: {b5.a3}")
    b7 = fonk5(0, 2, 3, 4)
    print(f"3D List: {b7}")