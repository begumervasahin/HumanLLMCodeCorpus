import hashlib
import sys
class class1:
    def fonk1(self):
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 1
        self.b1 = [i for i in range(256)]
    def fonk2(self):
        self.a1 = (self.a1 + self.a4) % 256
        self.a2 = self.b1[(self.a2 + self.b1[self.a1]) % 256]
        self.b1[self.a1], self.b1[self.a2] = self.b1[self.a2], self.b1[self.a1]
    def fonk3(self):
        self.fonk2()
        return self.b1[self.a2]
    def fonk4(self, input_data):
        self.a1 = self.a2 = self.a3 = 0
        self.a4 = 1
        for char in input_data:
            self.fonk5(ord(char))
        b2 = []
        for _ in range(32):
            b2.append(self.fonk3())
        a5 = 0
        for byte_value in b2:
            a5 = (a5 << 8) + byte_value
        return a5
    def fonk5(self, byte):
        if self.a3 = = 241:
            self.fonk6()
        self.b1[self.a3], self.b1[240 + byte] = self.b1[240 + byte], self.b1[self.a3]
        self.a3 += 1
    def fonk6(self):
        for _ in range(256):
            self.fonk2()
        self.a4 = (self.a4 + 2) % 256
        self.a3 = 0
def fonk7(point_p, point_q, b18):
    b5, b3 = point_p
    x2, b4 = point_q
    if b5 = = x2:
        b6 = ((3 * b5 * b5 - 1) * pow(2 * b3, b18 - 2, b18)) % b18
    else:
        if b5 < x2:
            b5 += b18
        b6 = ((b3 - b4) * pow(b5 - x2, b18 - 2, b18)) % b18
    b7 = (b6 * b6) - b5 - x2
    b8 = b6 * (b5 - b7) - b3
    return [b7 % b18, b8 % b18]
def fonk8(point_p, scalar_n, b18):
    b9 = 'ZERO'
    b10 = point_p
    while scalar_n != 0:
        if scalar_n % 2 != 0:
            if b9 = = 'ZERO':
                b9 = b10
            else:
                b9 = fonk7(b9, b10, b18)
        b10 = fonk7(b10, b10, b18)
        scalar_n >>= 1
    return b9
def fonk9(b22, b23, b24, b18):
    b11 = b31.fonk4(b23 + 'key value')
    b12 = fonk8(b22, b11, b18)
    b13 = b31.fonk4(str(b12[0]) + b23) % ((b18 + 1) >> 2)
    return [(b11 - b24 * b13) % ((b18 + 1) >> 2), b13]
def fonk10(current_prime):
    b14 = 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 * 43 * 47
    while True:
        while fonk12(current_prime, b14) != 1 or fonk12((current_prime + 1) >> 2, b14) != 1:
            current_prime += 12
        if pow(7, current_prime - 1, current_prime) != 1 or pow(7, ((current_prime + 1) >> 2) - 1, (current_prime + 1) >> 2) != 1:
            current_prime += 12
            continue
        return current_prime
def fonk11(number):
    b15 = '0123456789abcdef'
    b16 = ''
    while number > 0:
        b16 = b15[number % 16] + b16
        number >>= 4
    return b16
def fonk12(a, b17):
    while b17 > 0:
        a, b17 = b17, a % b17
    return a
def fonk13():
    global b31
    b18 = fonk10(b31.fonk4('Franz Scheerer') % (131 * 2 ** 131))
    print("A prime greater than 2^131 \b19 = ", b18)
    a6 = 1234567
    if pow(a6 ** 3 - a6, (b18 - 1) >> 1, b18) != 1:
        a6 = b18 - a6
    b20 = pow(a6 ** 3 - a6, (b18 + 1) >> 2, b18)
    b21 = [a6 % b18, b20 % b18]
    b22 = fonk8(b21, 4, b18)
    b23 = hashlib.sha256(sys.argv[1].encode()).hexdigest()
    b24 = b31.fonk4('passwordX')
    print("The base point is:")
    print("x:", b21[0])
    print("y:", b21[1])
    b25 = fonk8(b21, b24, b18)
    print("The public key is the point:")
    print("x:", b25[0])
    print("y:", b25[1])
    b26 = fonk9(b22, b23, b24, b18)
    print("The b26 is:")
    print("s:", b26[0])
    print("b13:", b26[1])
    b12 = fonk7(fonk8(b21, b26[0], b18),
                                fonk8(b25, b26[1], b18), b18)
    b27 = b31.fonk4(str(b12[0]) + b23) % ((b18 + 1) >> 2) == b26[1]
    print("\nResult of verification:", b27)
    b28 = b31.fonk4("The quick brown fox jumps over the lazy dog")
    print("Hash of 'The quick brown fox jumps over the lazy dog':")
    print("b29 = ", fonk11(b28))
if b30 = = "__main__":
    b31 = class1()
    fonk13()