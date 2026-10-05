import random
class EllipticCurve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b
        self.gen = None
    def extended_euclidean_algorithm(self, a, b):
        if not b:
            return (a, 1, 0)
        d1, x1, y1 = self.extended_euclidean_algorithm(b, a % b)
        return (d1, y1, x1 - (a
    def modular_inverse(self, n):
        return (self.extended_euclidean_algorithm(n, self.p)[1]) % self.p
    def point_check(self, point):
        if point == (-1, -1):
            return True
        x, y = point
        if not ((y * y) % self.p - (x * x + self.a) % self.p * x - self.b) % self.p:
            return True
        return False
    def point_addition(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        if x1 == x2:
            return (-1, -1)
        elif x1 < 0:
            return point2
        elif x2 < 0:
            return point1
        g = ((y2 - y1) * self.modular_inverse((x2 - x1) % self.p)) % self.p
        x3 = ((g * g) % self.p - x1 - x2) % self.p
        y3 = (g * (x1 - x3) - y1) % self.p
        return (x3, y3)
    def point_double(self, point):
        x1, y1 = point
        if x1 < 0 or y1 == 0:
            return (-1, -1)
        g = (((3 * x1 * x1) % self.p + self.a) % self.p * self.modular_inverse((2 * y1) % self.p)) % self.p
        x2 = ((g * g) % self.p - 2 * x1) % self.p
        y2 = ((g * (x1 - x2)) % self.p - y1) % self.p
        return (x2, y2)
    def point_scalar_multiplication(self, n, point):
        if n:
            res = point
            exp = []
            f = 1
            while f <= n:
                exp.append(bool(f & n))
                f <<= 1
            exp.reverse()
            for f in exp[1:]:
                res = self.point_double(res)
                if f:
                    res = self.point_addition(res, point)
            return res
        else:
            return (-1, -1)
    def generate_key_pair(self, dot=None, point=None):
        if not point:
            point = self.gen
        if not dot:
            dot = random.randint(3, self.p - 1)
        return self.point_scalar_multiplication(dot, point)
_p = 785963102379428822376694789446897396207498568951
_a = 317689081251325503476317476413827693272746955927
_b = 79052896607878758718120572025718535432100651934
_x = 771507216262649826170648268565579889907769254176
_y = 390157510246556628525279459266514995562533196655
_mdrmc = EllipticCurve(_p, _a, _b)
_mdrmg = (_x, _y)
key_pair = _mdrmc.generate_key_pair(point=_mdrmg)
print("Generated key pair:", key_pair)