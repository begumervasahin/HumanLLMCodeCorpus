import matplotlib.pyplot as plt
import math
class EllipticCurve:
    def __init__(self, p, a, b, G=None, n=None, h=None):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.n = n
        self.h = h
    def plot(self, n_points):
        x_values = []
        y_values = []
        for i in range(n_points):
            x_values.append(i)
            y_values.append(math.sqrt(i**3 + self.a*i + self.b) % self.p)
        plt.plot(x_values, y_values)
        plt.title(f'Elliptic Curve: y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
class EllipticCurvePoint(EllipticCurve):
    def __init__(self, x, y, curve):
        super().__init__(curve.p, curve.a, curve.b, curve.G, curve.n, curve.h)
        self.x = x % self.p
        self.y = y % self.p
    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            m = (3 * (self.x**2) + self.a) * self.inv_mod(2*self.y)
        else:
            m = (other.y - self.y) * self.inv_mod(other.x - self.x)
        x3 = (m**2 - self.x - other.x) % self.p
        y3 = (m * (self.x - x3) - self.y) % self.p
        return EllipticCurvePoint(x3, y3, self)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve
    def __ne__(self, other):
        return not self == other
    def inv_mod(self, x):
        return pow(x, -1, self.p) if x != 0 else 0
    def multiply(self, scalar):
        result = EllipticCurvePoint(0, 0, self)
        binary_scalar = bin(scalar)[2:]
        for bit in binary_scalar:
            result = result + result
            if bit == '1':
                result = result + self
        return result
curve = EllipticCurve(23, 0, 7)
point1 = EllipticCurvePoint(1, 3, curve)
point2 = EllipticCurvePoint(18, 20, curve)
curve.plot(20)
print(point1 + point2)
print(point1 == point2)
print(point1.multiply(5))