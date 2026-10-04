import base58
class TypeConversion:
    @staticmethod
    def int_to_b58(number):
        return base58.b58encode_int(number).decode()
    @staticmethod
    def b58_to_int(b58_string):
        return base58.b58decode_int(b58_string)
class ModularOperations:
    @staticmethod
    def modular_sqrt(a, p):
        if a % p == 0:
            return 0
        if p % 4 == 3:
            return pow(a, (p + 1)
        s = 0
        q = p - 1
        while q % 2 == 0:
            s += 1
            q
        z = 2
        while pow(z, (p - 1)
            z += 1
        m = s
        c = pow(z, q, p)
        t = pow(a, q, p)
        r = pow(a, (q + 1)
        while t != 0 and t != 1:
            t2i = t
            i = 0
            for i in range(1, m):
                t2i = pow(t2i, 2, p)
                if t2i == 1:
                    break
            b = pow(c, 2 ** (m - i - 1), p)
            m = i
            c = pow(b, 2, p)
            t = (t * b) % p
            r = (r * b) % p
        return r
class ECRing:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
def point_to_base58(P, curve):
    key58 = TypeConversion.int_to_b58(P.x)
    if P.y > (curve.p / 2):
        return '03' + key58
    else:
        return '02' + key58
def base58_to_point(P58, curve):
    a = curve.a
    p = curve.p
    b = curve.b
    keyX = TypeConversion.b58_to_int(P58[2:])
    keyY_sq = (keyX ** 3 + a * keyX + b) % p
    keyY = ModularOperations.modular_sqrt(keyY_sq, p)
    if P58.startswith('03'):
        if keyY > (p / 2):
            return ECRing.Point(keyX, keyY)
        else:
            return ECRing.Point(keyX, p - keyY)
    else:
        if keyY > (p / 2):
            return ECRing.Point(keyX, p - keyY)
        else:
            return ECRing.Point(keyX, keyY)
class Curve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
if __name__ == "__main__":
    example_curve = Curve(a=2, b=3, p=23)
    point = ECRing.Point(x=5, y=10)
    base58_string = point_to_base58(point, example_curve)
    print(f"Base-58 representation: {base58_string}")
    restored_point = base58_to_point(base58_string, example_curve)
    print(f"Restored point: ({restored