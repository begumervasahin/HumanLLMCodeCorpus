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
        return self.a6 >= a1
    def fonk4(self, adjustment):
        self.a3 -= adjustment
def fonk5(init, *dims):
    if not dims:
        return init
    return [fonk5(init, *dims[1:]) for _ in range(dims[0])]
if b3 = = "__main__":
    b4 = class1()
    b4.b2 = [50, 100, 200, 300]
    b4.a6 = 150.0
    b4.fonk2()
    print(f"Rectangle X: {b4.a2}, Y: {b4.a3}, Width: {b4.a4}, Height: {b4.a5}")
    b5 = b4.fonk3()
    print(f"Is Contour Valid? {'Yes' if b5 else 'No'}")
    b4.fonk4(555)
    print(f"Adjusted Rectangle Y: {b4.a3}")
    b6 = fonk5(0, 2, 3, 4)
    print(f"3D List: {b6}")