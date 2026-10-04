class Calculations:
    def __init__(self, index: int):
        self.name = index
        self.mc = []
    def find_slope_and_intercept(self, x1: float, y1: float, x2: float, y2: float):
        if (x1 - x2) != 0:
            slope = (y1 - y2) / (x1 - x2)
            intercept = y1 - (slope * x1)
            self.mc.insert(0, slope if abs(slope) != 0 else abs(slope))
            self.mc.insert(1, intercept)
        else:
            self.mc.insert(0, None)
            self.mc.insert(1, 0)
            self.mc.insert(2, x1)
    def get_index(self) -> int:
        return self.name
class Positions:
    def __init__(self, default_slope: float, default_intercept: float):
        self.position = None
        self.default_slope = default_slope
        self.default_intercept = default_intercept
    def is_slope_equal(self, slope: float) -> bool:
        return self.default_slope == slope
    def is_intercept_equal(self, intercept: float) -> bool:
        return self.default_intercept == intercept
    def left_or_right(self, tmp_intercept: float) -> int:
        if self.default_slope > 0:
            return 1 if self.default_intercept > tmp_intercept else 0
        elif self.default_slope < 0:
            return 0 if self.default_intercept > tmp_intercept else 1
    def is_intersecting(self, slope: float, intercept: float, d_array: list, t_array: list) -> bool:
        tt1, tt2 = float(t_array[1]), float(t_array[3])
        ttm1, ttm2 = max(tt1, tt2), min(tt1, tt2)
        if self.default_slope is not None and slope is not None:
            if self.default_slope * slope < 0:
                dt = max(float(d_array[1]), float(d_array[3])) if self.default_intercept < intercept else min(float(d_array[1]), float(d_array[3]))
                return ttm1 > dt and ttm2 < dt
            elif self.default_slope != slope and self.default_slope * slope > 0:
                x = (intercept - self.default_intercept) / (self.default_slope - slope)
                y = slope * x + intercept
                return ttm2 < y < ttm1
            else:
                return False
        elif self.default_slope is None:
            x = float(d_array[0])
            tx1, tx2 = float(t_array[0]), float(t_array[2])
            txm1, txm2 = max(tx1, tx2), min(tx1, tx2)
            return txm2 < x < txm1
        elif slope is None:
            x = float(t_array[0])
            dx1, dx2 = float(d_array[0]), float(d_array[2])
            dxm1, dxm2 = max(dx1, dx2), min(dx1, dx2)
            return dxm2 < x < dxm1
        else:
            return False