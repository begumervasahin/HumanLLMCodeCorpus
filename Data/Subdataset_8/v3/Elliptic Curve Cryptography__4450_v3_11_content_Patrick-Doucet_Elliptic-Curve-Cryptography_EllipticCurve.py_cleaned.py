import matplotlib.pyplot as plt
import math
class EllipticCurve:
    def __init__(self, prime_modulus, coefficient_a, coefficient_b, base_point=None, order=None, cofactor=None):
        self.p = prime_modulus
        self.a = coefficient_a
        self.b = coefficient_b
        self.G = base_point
        self.n = order
        self.h = cofactor
    def plot_curve(self, num_points):
        x_values = []
        y_values = []
        for i in range(num_points):
            x_values.append(i)
            y_values.append(math.sqrt(i**3 + self.a*i + self.b) % self.p)
        plt.plot(x_values, y_values)
        plt.title(f'Elliptic Curve: y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()
class EllipticCurvePoint(EllipticCurve):
    def __init__(self, x_coord, y_coord, curve):
        super().__init__(curve.p, curve.a, curve.b, curve.G, curve.n, curve.h)
        self.x = x_coord % self.p
        self.y = y_coord % self.p
    def __add__(self, other):
        if self.x == other.x and self.y == other.y:
            m = (3 * (self.x**2) + self.a) * self.modular_inverse(2*self.y)
        else:
            m = (other.y - self.y) * self.modular_inverse(other.x - self.x)
        x3 = (m**2 - self.x - other.x) % self.p
        y3 = (m * (self.x - x3) - self.y) % self.p
        return EllipticCurvePoint(x3, y3, self)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.curve == other.curve
    def __ne__(self, other):
        return not self == other
    def modular_inverse(self, x_val):
        return pow(x_val, -1, self.p) if x_val != 0 else 0
    def scalar_multiply(self, scalar_val):
        result_point = EllipticCurvePoint(0, 0, self)
        binary_scalar = bin(scalar_val)[2:]
        for bit in binary_scalar:
            result_point = result_point + result_point
            if bit == '1':
                result_point = result_point + self
        return result_point
curve = EllipticCurve(23, 0, 7)
point1 = EllipticCurvePoint(1, 3, curve)
point2 = EllipticCurvePoint(18, 20, curve)
curve.plot_curve(20)
print(point1 + point2)
print(point1 == point2)
print(point1.scalar_multiply(5))