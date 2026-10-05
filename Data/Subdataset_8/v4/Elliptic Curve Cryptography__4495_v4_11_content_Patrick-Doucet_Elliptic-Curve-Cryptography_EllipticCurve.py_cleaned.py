import matplotlib.pyplot as plt
import math
class EllipticCurve:
    def __init__(self, prime_modulus, coefficient_a, coefficient_b, base_point, order, cofactor):
        self.p = prime_modulus
        self.a = coefficient_a
        self.b = coefficient_b
        self.G = base_point
        self.n = order
        self.h = cofactor
    def plot_curve(self, n_points):
        x_values = []
        y_values = []
        for i in range(n_points):
            x_values.append(i)
            y_values.append(math.sqrt(i**3 + self.a*i + self.b))
        plt.plot(x_values, y_values)
        plt.show()
class EllipticCurvePoint(EllipticCurve):
    def __init__(self, x_coord, y_coord, curve):
        super().__init__(curve.p, curve.a, curve.b, curve.G, curve.n, curve.h)
        self.x = x_coord
        self.y = y_coord
        self.curve = curve
    def __add__(self, other):
        if self.x < other.x:
            a = self
            b = other
        else:
            a = other
            b = self
        if a.x == 0 and a.y == 0:
            return b
        elif b.x == 0 and b.y == 0:
            return a
        elif b == a.ec_inv():
            return EllipticCurvePoint(0, 0, a.curve)
        else:
            if a == b:
                m = (3 * (a.x**2) + a.curve.a) * a.inv_mod(2*a.y)
            else:
                m = (b.y - a.y) * a.inv_mod(b.x - a.x)
        point = EllipticCurvePoint(0, 0, a.curve)
        point.x = ((m**2 % a.curve.p) - a.x - b.x) % a.curve.p
        point.y = (m * (a.x - point.x) - a.y) % a.curve.p
        return point
    def inv_mod(self, x):
        return pow(x, self.curve.p-2, self.curve.p)
    def ec_inv(self):
        if self.x == 0 and self.y == 0:
            return self
        return EllipticCurvePoint(self.x, (-self.y) % self.curve.p, self.curve)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve
    def __ne__(self, other):
        return not self == other
    def multiply(self, scalar):
        binary_string = bin(scalar)[2:]
        temp_point = EllipticCurvePoint(self.x, self.y, self.curve)
        p_point = EllipticCurvePoint(self.x, self.y, self.curve)
        binary_string.pop()
        binary_string.reverse()
        for bit in binary_string:
            if bit == '0':
                temp_point = temp_point + temp_point
                temp_point.x %= self.curve.p
                temp_point.y %= self.curve.p
            else:
                temp_point = temp_point + temp_point
                temp_point.x %= self.curve.p
                temp_point.y %= self.curve.p
                temp_point = temp_point + p_point
                temp_point.x %= self.curve.p
                temp_point.y %= self.curve.p
        return temp_point