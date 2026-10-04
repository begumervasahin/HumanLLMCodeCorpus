class class1:
    def fonk1(self, index: int):
        self.b1 = index
        self.b2 = []
    def fonk2(self, x1: float, y1: float, x2: float, y2: float):
        if (x1 - x2) != 0:
            b3 = (y1 - y2) / (x1 - x2)
            b4 = y1 - (b3 * x1)
            self.b2.insert(0, b3 if abs(b3) != 0 else abs(b3))
            self.b2.insert(1, b4)
        else:
            self.b2.insert(0, None)
            self.b2.insert(1, 0)
            self.b2.insert(2, x1)
    def fonk3(self) -> int:
        return self.b1
class class2:
    def fonk4(self, b6: float, b7: float):
        self.b5 = None
        self.b6 = b6
        self.b7 = b7
    def fonk5(self, b3: float) -> bool:
        return self.b6 = = b3
    def fonk6(self, b4: float) -> bool:
        return self.b7 = = b4
    def fonk7(self, tmp_intercept: float) -> int:
        if self.b6 > 0:
            return 1 if self.b7 > tmp_intercept else 0
        elif self.b6 < 0:
            return 0 if self.b7 > tmp_intercept else 1
    def fonk8(self, b3: float, b4: float, d_array: list, t_array: list) -> bool:
        tt1, b8 = float(t_array[1]), float(t_array[3])
        ttm1, b9 = max(tt1, b8), min(tt1, b8)
        if self.b6 is not None and b3 is not None:
            if self.b6 * b3 < 0:
                b10 = max(float(d_array[1]), float(d_array[3])) if self.b7 < b4 else min(float(d_array[1]), float(d_array[3]))
                return ttm1 > b10 and b9 < b10
            elif self.b6 != b3 and self.b6 * b3 > 0:
                b11 = (b4 - self.b7) / (self.b6 - b3)
                b12 = b3 * b11 + b4
                return b9 < b12 < ttm1
            else:
                return False
        elif self.b6 is None:
            b11 = float(d_array[0])
            tx1, b13 = float(t_array[0]), float(t_array[2])
            txm1, b14 = max(tx1, b13), min(tx1, b13)
            return b14 < b11 < txm1
        elif b3 is None:
            b11 = float(t_array[0])
            dx1, b15 = float(d_array[0]), float(d_array[2])
            dxm1, b16 = max(dx1, b15), min(dx1, b15)
            return b16 < b11 < dxm1
        else:
            return False