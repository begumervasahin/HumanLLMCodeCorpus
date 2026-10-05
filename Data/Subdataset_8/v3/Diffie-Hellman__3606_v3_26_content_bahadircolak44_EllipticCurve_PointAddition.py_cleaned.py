class PointAddition:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.discriminant = -16 * (4 * a * a * a + 27 * b * b)
        if not self._is_smooth():
            raise Exception("The curve is not smooth!")
    def _is_smooth(self):
        return self.discriminant != 0
    def test_point(self, x, y):
        return y * y == x * x * x + self.a * x + self.b
    def print_equation(self):
        print(f"Elliptic curve equation: y^2 = x^3 + {self.a}x + {self.b}")
    def __eq__(self, other):
        return (self.a, self.b) == (other.a, other.b)
    def sum_points(self, x1, y1, x2, y2, f):
        E_y = self._egcd(x2 - x1, f)
        m = ((y2 - y1) * E_y) % f
        x3 = (m * m - x1 - x2) % f
        y3 = (m * (x1 - x3) - y1) % f
        return (x3, y3)
    def _egcd(self, a, b):
        r = -1
        B = b
        A = a
        full_set = []
        while r != 1 and r != 0:
            r = b % a
            q = b
            eq_set = [r, b, a, q * -1]
            b = a
            a = r
            full_set.append(eq_set)
        mod_set = [full_set[-1][i] for i in range(4)]
        mod_set.insert(2, 1)
        counter = 0
        for i in range(1, len(full_set)):
            if counter % 2 == 0:
                mod_set[2] = full_set[-1 * (i + 1)][3] * mod_set[4] + mod_set[2]
                mod_set[3] = full_set[-1 * (i + 1)][1]
            elif counter % 2 != 0:
                mod_set[4] = full_set[-1 * (i + 1)][3] * mod_set[2] + mod_set[4]
                mod_set[1] = full_set[-1 * (i + 1)][1]
            counter += 1
        return mod_set[2] % B if mod_set[3] == B else mod_set[4] % B