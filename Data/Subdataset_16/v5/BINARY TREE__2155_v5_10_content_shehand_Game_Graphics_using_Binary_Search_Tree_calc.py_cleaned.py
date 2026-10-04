class class1:
    def fonk1(self, b1: int):
        self.b1 = b1
        self.b2 = []
    def fonk2(self, x1: float, y1: float, x2: float, y2: float):
        if (x1 - x2) != 0:
            b3 = (y1 - y2) / (x1 - x2)
            b4 = y1 - (b3 * x1)
            self.b2 = [b3, b4]
        else:
            self.b2 = [None, 0, x1]
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
        return -1
    def fonk8(self, b3: float, b4: float, d_array: list, t_array: list) -> bool:
        t_min, b8 = min(float(t_array[1]), float(t_array[3])), max(float(t_array[1]), float(t_array[3]))
        if self.b6 is not None and b3 is not None:
            if self.b6 * b3 < 0:
                b9 = max(float(d_array[1]), float(d_array[3])) if self.b7 < b4 else min(float(d_array[1]), float(d_array[3]))
                return t_min < b9 < b8
            elif self.b6 != b3 and self.b6 * b3 > 0:
                b10 = (b4 - self.b7) / (self.b6 - b3)
                b11 = b3 * b10 + b4
                return t_min < b11 < b8
            else:
                return False
        elif self.b6 is None:
            b10 = float(d_array[0])
            t_min_x, b12 = min(float(t_array[0]), float(t_array[2])), max(float(t_array[0]), float(t_array[2]))
            return t_min_x < b10 < b12
        elif b3 is None:
            b10 = float(t_array[0])
            d_min_x, b13 = min(float(d_array[0]), float(d_array[2])), max(float(d_array[0]), float(d_array[2]))
            return d_min_x < b10 < b13
        else:
            return False