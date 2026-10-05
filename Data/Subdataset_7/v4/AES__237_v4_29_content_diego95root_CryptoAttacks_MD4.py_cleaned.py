import struct
def fonk1(i, n):
    return ((i << n) & 0xffffffff) | (i >> (32 - n))
def fonk2(x, y, z):
    return (x & y) | (~x & z)
def fonk3(x, y, z):
    return (x & y) | (x & z) | (y & z)
def fonk4(x, y, z):
    return x ^ y ^ z
class class1(object):
    def fonk5(self):
        self.b1 = ""
        self.a1 = 0
        self.b2 = [
            0x67452301,
            0xefcdab89,
            0x98badcfe,
            0x10325476
        ]
    def fonk6(self, chunk):
        self.a1 += 1
        b3 = list(struct.unpack("<16I", chunk) + (None,) * (80 - 16))
        b2 = [x for x in self.b2]
        b4 = ((3, 7, 11, 19), (3, 5, 9, 13), (3, 9, 11, 15))
        b5 = ((0, 1, 2, 3), (0, 4, 8, 12), (0, 2, 1, 3))
        b6 = (0x00000000, 0x5a827999, 0x6ed9eba1)
        for i in range(3):
            b7 = b4[i]
            b8 = b5[i]
            b9 = b6[i]
            for r in range(16):
                b10 = (16 - r) % 4
                b2[b10] = fonk1((b2[b10] + globals()[chr(72 + i)](b2[(b10 + 1) % 4], b2[(b10 + 2) % 4], b2[(b10 + 3) % 4]) + b3[b8[r]] + b9) % 2 ** 32, b7[r % 4])
        for i, v in enumerate(b2):
            self.b2[i] = (v + self.b2[i]) % 2 ** 32
    def fonk7(self, data):
        b11 = self.b1 + data
        b12 = len(b11) % 64
        b13 = (55 - b12) % 64
        b14 = "\x80" + "\x00" * b13 + struct.pack("<Q", len(b11) * 8)
        for chunk_start in range(0, len(b11) - b12, 64):
            self.fonk6(b11[chunk_start:chunk_start + 64])
        self.b1 = b11[-b12:]
        return self
    def fonk8(self):
        self.fonk7("\x80" + "\x00" * ((55 - len(self.b1)) % 64) + struct.pack("<Q", len(self.b1) * 8))
        b15 = struct.pack("<4I", *self.b2)
        self.fonk5()
        return b15.encode("hex")
b16 = class1()
b16.fonk7("Hello, world!")
print(b16.fonk8())