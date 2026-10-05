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
    def check(self, point):
        left_side = self.mod(point.y * point.y)
        right_side = self.mod(point.x * point.x * point.x + self.a * point.x + self.b)
        discriminant = 4 * self.a * self.a * self.a + 27 * self.b * self.b
        return left_side == right_side and discriminant != 0
    def mod(self, x):
        return x % self.prime_modulus
    def inverse_mod(self, x):
        s0, s1 = 0, 1
        r0, r1 = self.prime_modulus, x
        while r0 != 0:
            quotient = r1
            r1, r0 = r0, r1 - quotient * r0
            s1, s0 = s0, s1 - quotient * s0
        return s1 % self.prime_modulus
    def add(self, p, q):
        r = Point(0, 0)
        if p.equals(r):
            return q
        if q.equals(r):
            return p
        if p.equals(q):
            if p.y != 0:
                l = self.mod(self.mod(3 * p.x * p.x + self.a) * self.inverse_mod(2 * p.y))
                r.x = self.mod(l * l - 2 * p.x)
                r.y = self.mod(l * (p.x - r.x) - p.y)
        else:
            if q.x - p.x != 0:
                l = self.mod((q.y - p.y) * self.inverse_mod(q.x - p.x))
                r.x = self.mod(l * l - p.x - q.x)
                r.y = self.mod(l * (p.x - r.x) - p.y)
        return r
    def double(self, p):
        return self.add(p, p)
    def multiply(self, p, n):
        if n == 0:
            return Point(0, 0)
        elif n == 1:
            return p
        elif n % 2 == 1:
            return self.add(p, self.multiply(p, n - 1))
        else:
            return self.multiply(self.double(p), n / 2)
class Decipher:
    def __init__(self, curve, start_point, end_point, limit):
        self.curve = curve
        self.start_point = start_point
        self.end_point = end_point
        self.limit = limit
    def run(self):
        current_point = Point(0, 0)
        for d in range(1, self.limit):
            current_point = self.curve.add(self.start_point, current_point)
            if not self.curve.check(current_point):
                return 0
            if current_point.equals(self.end_point):
                return d
        return 0
def main():
    a = -0x3
    b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
    prime_modulus = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
    start_point = Point(
        0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
    )
    end_point = Point(
        0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe,
        0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562
    )
    curve = EllipticCurve(a, b, prime_modulus)
    if not curve.check(start_point) or not curve.check(end_point):
        return 0
    decipher = Decipher(curve, start_point, end_point, prime_modulus)
    return decipher.run()
if __name__ == "__main__":
    value = main()
    print(value)