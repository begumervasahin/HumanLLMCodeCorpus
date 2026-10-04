import matplotlib.pyplot as plt
import math
class EllipticCurve:
    def __init__(self, p, a, b, G, n, h):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h
    def plot(self, n):
        x_values = []
        y_values = []
        for x in range(n):
            y_squared = (x ** 3 + self.a * x + self.b) % self.p
            if self.is_quadratic_residue(y_squared):
                y = self.sqrt_mod(y_squared)
                x_values.append(x)
                y_values.append(y)
                x_values.append(x)
                y_values.append(self.p - y)
        plt.scatter(x_values, y_values, s=1)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(f"Elliptic Curve: y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})")
        plt.show()
    def is_quadratic_residue(self, x):
        return pow(x, (self.p - 1)
    def sqrt_mod(self, x):
        return pow(x, (self.p + 1)
class EllipticCurvePoint:
    def __init__(self, x, y, curve):
        self.x = x
        self.y = y
        self.curve = curve
    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            return self.double()
        elif self.x == other.x:
            return EllipticCurvePoint(0, 0, self.curve)
        m = (other.y - self.y) * self.inv_mod(other.x - self.x)
        x_r = (m ** 2 - self.x - other.x) % self.curve.p
        y_r = (m * (self.x - x_r) - self.y) % self.curve.p
        return EllipticCurvePoint(x_r, y_r, self.curve)
    def double(self):
        m = (3 * self.x ** 2 + self.curve.a) * self.inv_mod(2 * self.y)
        x_r = (m ** 2 - 2 * self.x) % self.curve.p
        y_r = (m * (self.x - x_r) - self.y) % self.curve.p
        return EllipticCurvePoint(x_r, y_r, self.curve)
    def inv_mod(self, x):
        return pow(x, self.curve.p - 2, self.curve.p)
    def ec_inv(self):
        return EllipticCurvePoint(self.x, -self.y % self.curve.p, self.curve)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve
    def __ne__(self, other):
        return not self.__eq__(other)
    def multiply(self, scalar):
        result = EllipticCurvePoint(0, 0, self.curve)
        addend = self
        while scalar:
            if scalar & 1:
                result += addend
            addend += addend
            scalar >>= 1
        return result
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def __repr__(self):
        return self.__str__()
if __name__ == "__main__":
    p = 103
    a = 1
    b = 1
    G = EllipticCurvePoint(0, 1, None)
    n = 97
    h = 1
    curve = EllipticCurve(p, a, b, G, n, h)
    G.curve = curve
    curve.plot(p)
    point = EllipticCurvePoint(3, 6, curve)
    print(f"Point: {point}")
    result = point.multiply(10)
    print(f"10 * Point: {result}")