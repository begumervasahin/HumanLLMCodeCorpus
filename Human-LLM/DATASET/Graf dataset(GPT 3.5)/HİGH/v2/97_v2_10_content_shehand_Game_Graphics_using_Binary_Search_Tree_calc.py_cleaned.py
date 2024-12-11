class class1:
    def fonk1(self, indx):
        self.b1 = indx
        self.b2 = []
    def fonk2(self, x1, y1, x2, y2):
        if x1 != x2:
            b3 = (y1 - y2) / (x1 - x2)
            b4 = y1 - b3 * x1
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
    def fonk5(self, slope):
        return self.b6 = = slope
    def fonk6(self, intercept):
        return self.b7 = = intercept
    def fonk7(self, tmp_intercept):
        if self.b6 > 0:
            return 1 if self.b7 > tmp_intercept else 0
        elif self.b6 < 0:
            return 0 if self.b7 > tmp_intercept else 1
    def fonk8(self, slope, intercept, d_array, t_array):
        t1, b8 = float(t_array[1]), float(t_array[3])
        tm1, b9 = max(t1, b8), min(t1, b8)
        if self.b6 is not None and slope is not None:
            if self.b6 * slope < 0:
                if self.b7 < intercept:
                    b10 = max(float(d_array[1]), float(d_array[3]))
                    return b9 < b10 < tm1
                elif self.b7 > intercept:
                    b10 = min(float(d_array[1]), float(d_array[3]))
                    return b9 < b10 < tm1
                else:
                    return True
            elif self.b6 != slope and self.b6 * slope > 0:
                b11 = (intercept - self.b7) / (self.b6 - slope)
                b12 = slope * b11 + intercept
                return b9 < b12 < tm1
            else:
                return False
        elif self.b6 is None:
            b11 = float(d_array[0])
            tx1, b13 = float(t_array[0]), float(t_array[2])
            txm1, b14 = max(tx1, b13), min(tx1, b13)
            return b14 < b11 < txm1
        elif slope is None:
            b11 = float(t_array[0])
            dx1, b15 = float(d_array[0]), float(d_array[2])
            dxm1, b16 = max(dx1, b15), min(dx1, b15)
            return b16 < b11 < dxm1
        else:
            return False