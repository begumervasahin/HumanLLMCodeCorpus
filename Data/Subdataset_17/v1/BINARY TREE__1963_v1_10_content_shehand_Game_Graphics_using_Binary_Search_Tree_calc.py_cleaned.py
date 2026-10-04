class Calculations:
    def __init__(self, indx):
        self.name = indx
        self.mc = []
    def findMnC(self, x1, y1, x2, y2):
        if (x1 - x2) != 0:
            m = (y1 - y2) / (x1 - x2)
            c = y1 - (m * x1)
            if abs(m) == 0:
                self.mc.insert(0, abs(m))
            else:
                self.mc.insert(0, m)
            self.mc.insert(1, c)
        else:
            self.mc.insert(0, None)
            self.mc.insert(1, 0)
            self.mc.insert(2, x1)
    def returnIndex(self):
        return self.name
class Positions:
    def __init__(self, default_m, default_c):
        self.position = None
        self.default_m = default_m
        self.default_c = default_c
    def mEqual(self, m):
        return self.default_m == m
    def cEqual(self, c):
        return self.default_c == c
    def leftOright(self, tmpc):
        if self.default_m > 0:
            return 1 if self.default_c > tmpc else 0
        elif self.default_m < 0:
            return 0 if self.default_c > tmpc else 1
        else:
            return None
    def isIntersec(self, m, c, dArray, tArray):
        tt1 = float(tArray[1])
        tt2 = float(tArray[3])
        ttm1 = max(tt1, tt2)
        ttm2 = min(tt1, tt2)
        if self.default_m is not None and m is not None:
            if self.default_m * m < 0:
                dt = max(float(dArray[1]), float(dArray[3])) if self.default_c < c else min(float(dArray[1]), float(dArray[3]))
                return ttm1 > dt and ttm2 < dt
            elif self.default_m != m and self.default_m * m > 0:
                x = (c - self.default_c) / (self.default_m - m)
                y = m * x + c
                return ttm2 < y < ttm1
            else:
                return False
        elif self.default_m is None:
            x = float(dArray[0])
            tx1 = float(tArray[0])
            tx2 = float(tArray[2])
            txm1 = max(tx1, tx2)
            txm2 = min(tx1, tx2)
            return txm2 < x < txm1
        elif m is None:
            x = float(tArray[0])
            dx1 = float(dArray[0])
            dx2 = float(dArray[2])
            dxm1 = max(dx1, dx2)
            dxm2 = min(dx1, dx2)
            return dxm2 < x < dxm1
        else:
            return False
if __name__ == "__main__":
    calc = Calculations(indx="example_index")
    calc.findMnC(1, 2, 3, 4)
    print(f"Index: {calc.returnIndex()}")
    print(f"Slope and Intercept: {calc.mc}")
    pos = Positions(default_m=1, default_c=0)
    print(f"mEqual(1): {pos.mEqual(1)}")
    print(f"cEqual(0): {pos.cEqual(0)}")
    print(f"leftOright(-1): {pos.leftOright(-1)}")
    dArray = [0, 1, 2, 3]
    tArray = [1, 2, 3, 4]
    print(f"isIntersec(1, 1, dArray, tArray): {pos.isIntersec(1, 1, dArray, tArray)}")