class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def equals(self, other_point):
        return self.x == other_point.x and self.y == other_point.y
class EllipticCurve:
    def __init__(self, a, b, prime_modulus):
        self.a = a
        self.b = b
        self.prime_modulus = prime_modulus
    def is_valid_point(self, point):
        left_side = self._mod(point.y * point.y)
        right_side = self._mod(point.x * point.x * point.x + self.a * point.x + self.b)
        cubic_curve_condition = 4 * self.a * self.a * self.a + 27 * self.b * self.b
        return left_side == right_side and cubic_curve_condition != 0
    def _mod(self, x):
        return x % self.prime_modulus
    def inverse_mod(self, x):
        s0, s1 = 0, 1
        r0, r1 = self.prime_modulus, x
        while r0 != 0:
            quotient = r1
            r1, r0 = r0, r1 - quotient * r0
            s1, s0 = s0, s1 - quotient * s0
        return s1 % self.prime_modulus
    def point_addition(self, point1, point2):
        result_point = Point(0, 0)
        if point1.equals(result_point):
            return point2
        if point2.equals(result_point):
            return point1
        if point1.equals(point2):
            if point1.y != 0:
                slope = self._mod((3 * point1.x * point1.x + self.a) * self.inverse_mod(2 * point1.y))
                result_point.x = self._mod(slope * slope - 2 * point1.x)
                result_point.y = self._mod(slope * (point1.x - result_point.x) - point1.y)
        else:
            if point2.x - point1.x != 0:
                slope = self._mod((point2.y - point1.y) * self.inverse_mod(point2.x - point1.x))
                result_point.x = self._mod(slope * slope - point1.x - point2.x)
                result_point.y = self._mod(slope * (point1.x - result_point.x) - point1.y)
        return result_point
    def point_doubling(self, point):
        return self.point_addition(point, point)
    def scalar_multiplication(self, point, scalar):
        if scalar == 0:
            return Point(0, 0)
        elif scalar == 1:
            return point
        elif scalar % 2 == 1:
            return self.point_addition(point, self.scalar_multiplication(point, scalar - 1))
        else:
            return self.scalar_multiplication(self.point_doubling(point), scalar / 2)
class Decipher:
    def __init__(self, elliptic_curve, point_p, point_q, n):
        self.elliptic_curve = elliptic_curve
        self.point_p = point_p
        self.point_q = point_q
        self.n = n
    def run(self):
        result_point = Point(0, 0)
        for d in range(1, self.n):
            result_point = self.elliptic_curve.point_addition(self.point_p, result_point)
            if not self.elliptic_curve.is_valid_point(result_point):
                return 0
            if result_point.equals(self.point_q):
                return d
        return 0
def main():
    coefficient_a = -3
    coefficient_b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    prime_modulus = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    point_P = Point(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
    )
    point_Q = Point(
        0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
        0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
    )
    curve = EllipticCurve(coefficient_a, coefficient_b, prime_modulus)
    if not curve.is_valid_point(point_P) or not curve.is_valid_point(point_Q):
        return 0
    decipher = Decipher(curve, point_P, point_Q, prime_modulus)
    return decipher.run()
if __name__ == "__main__":
    value = main()
    print(value)