class Calculations:
    def __init__(self, index):
        self.name = index
        self.mc = []
    def find_slope_and_intercept(self, x1, y1, x2, y2):
        if (x1 - x2) != 0:
            slope = (y1 - y2) / (x1 - x2)
            intercept = y1 - (slope * x1)
            if abs(slope) == 0:
                self.mc.insert(0, abs(slope))
            else:
                self.mc.insert(0, slope)
            self.mc.insert(1, intercept)
        else:
            self.mc.insert[0, None]
            self.mc.insert[1, 0]
            self.mc.insert[2, x1]
    def return_index(self):
        return self.name
class Positions:
    def __init__(self, default_slope, default_intercept):
        self.position = None
        self.default_slope = default_slope
        self.default_intercept = default_intercept
    def slope_equal(self, slope):
        return self.default_slope == slope
    def intercept_equal(self, intercept):
        return self.default_intercept == intercept
    def left_or_right(self, tmp_intercept):
        if self.default_slope > 0:
            if self.default_intercept > tmp_intercept:
                return 1
            else:
                return 0
        elif self.default_slope < 0:
            if self.default_intercept > tmp_intercept:
                return 0
            else:
                return 1
        else:
            return None
    def is_intersection(self, slope, intercept, d_array, t_array):
        t1 = float(t_array[1])
        t2 = float(t_array[3])
        tm1 = max(t1, t2)
        tm2 = min(t1, t2)
        if self.default_slope != None and slope != None:
            if self.default_slope * slope < 0:
                if self.default_intercept < intercept:
                    dt = max(float(d_array[1]), float(d_array[3]))
                    if tm1 > dt and tm2 < dt:
                        return True
                    else:
                        return False
                elif self.default_intercept > intercept:
                    dt = min(float(d_array[1]), float(d_array[3]))
                    if tm1 > dt and tm2 < dt:
                        return True
                    else:
                        return False
                else:
                    return True
            elif self.default_slope != slope and self.default_slope * slope > 0:
                x_intersect = (intercept - self.default_intercept) / (self.default_slope - slope)
                y_intersect = slope * x_intersect + intercept
                if y_intersect > tm2 and y_intersect < tm1:
                    return True
                else:
                    return False
            else:
                return False
        elif self.default_slope == None:
            x = float(d_array[0])
            tx1 = float(t_array[0])
            tx2 = float(t_array[2])
            txm1 = max(tx1, tx2)
            txm2 = min(tx1, tx2)
            if x > txm2 and x < txm1:
                return True
            else:
                return False
        elif slope == None:
            x = float(t_array[0])
            dx1 = float(d_array[0])
            dx2 = float(d_array[2])
            dxm1 = max(dx1, dx2)
            dxm2 = min(dx1, dx2)
            if x > dxm2 and x < dxm1:
                return True
            else:
                return False
        else:
            return False