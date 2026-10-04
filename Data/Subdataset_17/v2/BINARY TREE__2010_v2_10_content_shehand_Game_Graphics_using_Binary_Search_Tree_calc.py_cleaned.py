class Calculations:
    def __init__(self, index: str):
        self.index = index
        self.mc = []
    def find_slope_and_intercept(self, x1: float, y1: float, x2: float, y2: float):
        if (x1 - x2) != 0:
            m = (y1 - y2) / (x1 - x2)
            c = y1 - (m * x1)
            self.mc = [abs(m) if m == 0 else m, c]
        else:
            self.mc = [None, 0, x1]
    def get_index(self) -> str:
        return self.index
class Positions:
    def __init__(self, default_m: float, default_c: float):
        self.position = None
        self.default_m = default_m
        self.default_c = default_c
    def is_m_equal(self, m: float) -> bool:
        return self.default_m == m
    def is_c_equal(self, c: float) -> bool:
        return self.default_c == c
    def left_or_right(self, tmpc: float) -> Union[int, None]:
        if self.default_m > 0:
            return 1 if self.default_c > tmpc else 0
        elif self.default_m < 0:
            return 0 if self.default_c > tmpc else 1
        else:
            return None
    def is_intersect(self, m: float, c: float, d_array: list[float], t_array: list[float]) -> bool:
        tt1, tt2 = float(t_array[1]), float(t_array[3])
        ttm1, ttm2 = max(tt1, tt2), min(tt1, tt2)
        if self.default_m is not None and m is not None:
            if self.default_m * m < 0:
                dt = max(float(d_array[1]), float(d_array[3])) if self.default_c < c else min(float(d_array[1]), float(d_array[3]))
                return ttm1 > dt and ttm2 < dt
            elif self.default_m != m and self.default_m * m > 0:
                x = (c - self.default_c) / (self.default_m - m)
                y = m * x + c
                return ttm2 < y < ttm1
            else:
                return False
        elif self.default_m is None:
            x = float(d_array[0])
            tx1, tx2 = float(t_array[0]), float(t_array[2])
            return min(tx1, tx2) < x < max(tx1, tx2)
        elif m is None:
            x = float(t_array[0])
            dx1, dx2 = float(d_array[0]), float(d_array[2])
            return min(dx1, dx2) < x < max(dx1, dx2)
        else:
            return False
if __name__ == "__main__":
    calc = Calculations(index="example_index")
    calc.find_slope_and_intercept(1, 2, 3, 4)
    print(f"Index: {calc.get_index()}")
    print(f"Slope and Intercept: {calc.mc}")
    pos = Positions(default_m=1, default_c=0)
    print(f"is_m_equal(1): {pos.is_m_equal(1)}")
    print(f"is_c_equal(0): {pos.is_c_equal(0)}")
    print(f"left_or_right(-1): {pos.left_or_right(-1)}")
    d_array = [0, 1, 2, 3]
    t_array = [1, 2, 3, 4]
    print(f"is_intersect(1, 1, d_array, t_array): {pos.is_intersect(1, 1, d_array, t_array)}")