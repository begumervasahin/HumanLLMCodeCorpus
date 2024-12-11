class class1:
    def fonk1(self, index):
        self.b1 = index
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
            self.b2.insert[0, None]
            self.b2.insert[1, 0]
            self.b2.insert[2, x1]
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
    def fonk7(self, tmp_intercept):
        if self.b6 > 0:
            return 1 if self.b7 > tmp_intercept else 0
        elif self.b6 < 0:
            return 0 if self.b7 > tmp_intercept else 1
        else:
            return None
    def fonk8(self, b3, b4, d_array, t_array):
        b8 = float(t_array[1])
        b9 = float(t_array[3])
        b10 = max(b8, b9)
        b11 = min(b8, b9)
        if self.b6 is not None and b3 is not None:
            if self.b6 * b3 < 0:
                if self.b7 < b4:
                    b12 = max(float(d_array[1]), float(d_array[3]))
                    return b10 > b12 and b11 < b12
                elif self.b7 > b4:
                    b12 = min(float(d_array[1]), float(d_array[3]))
                    return b10 > b12 and b11 < b12
                else:
                    return True
            elif self.b6 != b3 and self.b6 * b3 > 0:
                b13 = (b4 - self.b7) / (self.b6 - b3)
                b14 = b3 * b13 + b4
                return b11 < b14 < b10
            else:
                return False
        elif self.b6 is None:
            b15 = float(d_array[0])
            b16 = float(t_array[0])
            b17 = float(t_array[2])
            b18 = max(b16, b17)
            b19 = min(b16, b17)
            return b19 < b15 < b18
        elif b3 is None:
            b15 = float(t_array[0])
            b20 = float(d_array[0])
            b21 = float(d_array[2])
            b22 = max(b20, b21)
            b23 = min(b20, b21)
            return b23 < b15 < b22
        else:
            return False