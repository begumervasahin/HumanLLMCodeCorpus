import struct
def fonk1(b5, n):
    return ((b5 << n) & 0xffffffff) | (b5 >> (32 - n))
def fonk2(x,y,z):
    return (x & y) | (~x & z)
def fonk3(x,y,z):
    return (x & y) | (x & z) | (y & z)
def fonk4(x,y,z):
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
        b3 = list( struct.unpack("<16I", chunk) + (None,) * (80-16) )
        b2 = [x for x in self.b2]
        b4 = (3,7,11,19)
        for b8 in xrange(16):
            b5 = (16-b8)%4
            b6 = b8
            b2[b5] = fonk1( (b2[b5] + fonk2(b2[(b5+1)%4], b2[(b5+2)%4], b2[(b5+3)%4]) + b3[b6]) % 2**32, b4[b8%4] )
        b4 = (3,5,9,13)
        for b8 in xrange(16):
            b5 = (16-b8)%4
            b6 = 4*(b8%4) + b8
            b2[b5] = fonk1( (b2[b5] + fonk3(b2[(b5+1)%4], b2[(b5+2)%4], b2[(b5+3)%4]) + b3[b6] + 0x5a827999) % 2**32, b4[b8%4] )
        b4 = (3,9,11,15)
        b6 = (0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15)
        for b8 in xrange(16):
            b5 = (16-b8)%4
            b2[b5] = fonk1( (b2[b5] + fonk4(b2[(b5+1)%4], b2[(b5+2)%4], b2[(b5+3)%4]) + b3[b6[b8]] + 0x6ed9eba1) % 2**32, b4[b8%4] )
        for b5,v in enumerate(b2):
            self.b2[b5] = (v + self.b2[b5]) % 2**32
    def fonk7(self, data):
        b7 = self.b1 + data
        b8 = len(b7) % 64
        if b8 != 0:
            self.b1 = b7[-b8:]
        else:
            self.b1 = ""
        for chunk in xrange(0, len(b7)-b8, 64):
            self.fonk6( b7[chunk:chunk+64] )
        return self
    def fonk8(self):
        b9 = len(self.b1) + 64 * self.a1
        self.fonk7( "\x80" + "\x00" * ((55 - b9) % 64) + struct.pack("<Q", b9 * 8) )
        b10 = struct.pack("<4I", *self.b2)
        self.fonk5()
        return b10.encode("hex")