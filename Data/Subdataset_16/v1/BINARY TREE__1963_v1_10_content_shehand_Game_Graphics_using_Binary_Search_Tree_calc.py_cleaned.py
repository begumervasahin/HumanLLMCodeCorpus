class class1:
    def fonk1(self, indx):
        self.b1 = indx
        self.b2 = []
    def fonk2(self, x1, y1, x2, y2):
        if (x1 - x2) != 0:
            b3 = (y1 - y2) / (x1 - x2)
            b4 = y1 - (b3 * x1)
            if abs(b3) == 0:
                self.b2.insert(0, abs(b3))
            else:
                self.b2.insert(0, b3)
            self.b2.insert(1, b4)
        else:
            self.b2.insert(0, None)
            self.b2.insert(1, 0)
            self.b2.insert(2, x1)
    def fonk3(self):
        return self.b1
class class2:
    def fonk4(self, b6, b7):
        self.b5 = None
        self.b6 = b6
        self.b7 = b7
    def fonk5(self, b3):
        return self.b6 = = b3
    def fonk6(self, b4):
        return self.b7 = = b4
    def fonk7(self, tmpc):
        if self.b6 > 0:
            return 1 if self.b7 > tmpc else 0
        elif self.b6 < 0:
            return 0 if self.b7 > tmpc else 1
        else:
            return None
    def fonk8(self, b3, b4, b26, b27):
        b8 = float(b27[1])
        b9 = float(b27[3])
        b10 = max(b8, b9)
        b11 = min(b8, b9)
        if self.b6 is not None and b3 is not None:
            if self.b6 * b3 < 0:
                b12 = max(float(b26[1]), float(b26[3])) if self.b7 < b4 else min(float(b26[1]), float(b26[3]))
                return b10 > b12 and b11 < b12
            elif self.b6 != b3 and self.b6 * b3 > 0:
                b13 = (b4 - self.b7) / (self.b6 - b3)
                b14 = b3 * b13 + b4
                return b11 < b14 < b10
            else:
                return False
        elif self.b6 is None:
            b13 = float(b26[0])
            b15 = float(b27[0])
            b16 = float(b27[2])
            b17 = max(b15, b16)
            b18 = min(b15, b16)
            return b18 < b13 < b17
        elif b3 is None:
            b13 = float(b27[0])
            b19 = float(b26[0])
            b20 = float(b26[2])
            b21 = max(b19, b20)
            b22 = min(b19, b20)
            return b22 < b13 < b21
        else:
            return False
if b23 = = "__main__":
    b24 = class1(indx="example_index")
    b24.fonk2(1, 2, 3, 4)
    print(f"Index: {b24.fonk3()}")
    print(f"Slope and Intercept: {b24.b2}")
    b25 = class2(b6=1, b7=0)
    print(f"fonk5(1): {b25.fonk5(1)}")
    print(f"fonk6(0): {b25.fonk6(0)}")
    print(f"fonk7(-1): {b25.fonk7(-1)}")
    b26 = [0, 1, 2, 3]
    b27 = [1, 2, 3, 4]
    print(f"fonk8(1, 1, b26, b27): {b25.fonk8(1, 1, b26, b27)}")