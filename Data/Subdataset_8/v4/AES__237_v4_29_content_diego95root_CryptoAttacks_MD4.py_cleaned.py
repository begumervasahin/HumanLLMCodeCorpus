import struct
def left_rotate(i, n):
    return ((i << n) & 0xffffffff) | (i >> (32 - n))
def F(x, y, z):
    return (x & y) | (~x & z)
def G(x, y, z):
    return (x & y) | (x & z) | (y & z)
def H(x, y, z):
    return x ^ y ^ z
class MD4(object):
    def __init__(self):
        self.remainder = ""
        self.count = 0
        self.h = [
            0x67452301,
            0xefcdab89,
            0x98badcfe,
            0x10325476
        ]
    def _add_chunk(self, chunk):
        self.count += 1
        X = list(struct.unpack("<16I", chunk) + (None,) * (80 - 16))
        h = [x for x in self.h]
        s = ((3, 7, 11, 19), (3, 5, 9, 13), (3, 9, 11, 15))
        k = ((0, 1, 2, 3), (0, 4, 8, 12), (0, 2, 1, 3))
        t = (0x00000000, 0x5a827999, 0x6ed9eba1)
        for i in range(3):
            round_shifts = s[i]
            round_indices = k[i]
            round_constant = t[i]
            for r in range(16):
                idx = (16 - r) % 4
                h[idx] = left_rotate((h[idx] + globals()[chr(72 + i)](h[(idx + 1) % 4], h[(idx + 2) % 4], h[(idx + 3) % 4]) + X[round_indices[r]] + round_constant) % 2 ** 32, round_shifts[r % 4])
        for i, v in enumerate(h):
            self.h[i] = (v + self.h[i]) % 2 ** 32
    def update(self, data):
        message = self.remainder + data
        remainder_length = len(message) % 64
        padding_length = (55 - remainder_length) % 64
        padded_message = "\x80" + "\x00" * padding_length + struct.pack("<Q", len(message) * 8)
        for chunk_start in range(0, len(message) - remainder_length, 64):
            self._add_chunk(message[chunk_start:chunk_start + 64])
        self.remainder = message[-remainder_length:]
        return self
    def finish(self):
        self.update("\x80" + "\x00" * ((55 - len(self.remainder)) % 64) + struct.pack("<Q", len(self.remainder) * 8))
        digest = struct.pack("<4I", *self.h)
        self.__init__()
        return digest.encode("hex")
md4 = MD4()
md4.update("Hello, world!")
print(md4.finish())