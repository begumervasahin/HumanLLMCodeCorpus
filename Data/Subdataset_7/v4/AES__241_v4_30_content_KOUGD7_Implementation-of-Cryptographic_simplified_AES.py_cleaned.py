
b1 = [0x9, 0x4, 0xa, 0xb, 0xd, 0x1, 0x8, 0x5,
         0x6, 0x2, 0x0, 0x3, 0xc, 0xe, 0xf, 0x7]
b2 = [0xa, 0x5, 0x9, 0xb, 0x1, 0x7, 0x8, 0xf,
             0x6, 0x0, 0x2, 0x3, 0xc, 0x4, 0xd, 0xe]
b3 = [None] * 6
def fonk1(p1, p2):
    a1 = 0
    while p2:
        if p2 & 0b1:
            a1 ^= p1
        p1 <<= 1
        if p1 & 0b10000:
            p1 ^= 0b11
        p2 >>= 1
    return a1 & 0b1111
def fonk2(n):
    return [n >> 12, (n >> 4) & 0xf, (n >> 8) & 0xf,  n & 0xf]
def fonk3(m):
    return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]
def fonk4(s1, s2):
    return [i ^ j for i, j in zip(s1, s2)]
def fonk5(b1, s):
    return [b1[e] for e in s]
def fonk6(s):
    return [s[0], s[1], s[3], s[2]]
def fonk7(key):
    def fonk8(b):
        return b1[b >> 4] + (b1[b & 0x0f] << 4)
    rcon1, b4 = 0b10000000, 0b00110000
    b3[0] = (key & 0xff00) >> 8
    b3[1] = key & 0x00ff
    b3[2] = b3[0] ^ rcon1 ^ fonk8(b3[1])
    b3[3] = b3[2] ^ b3[1]
    b3[4] = b3[2] ^ b4 ^ fonk8(b3[3])
    b3[5] = b3[4] ^ b3[3]
def fonk9(plaintext):
    def fonk10(s):
        return [s[0] ^ fonk1(4, s[2]), s[1] ^ fonk1(4, s[3]),
                s[2] ^ fonk1(4, s[0]), s[3] ^ fonk1(4, s[1])]
    b5 = fonk2(((b3[0] << 8) + b3[1]) ^ plaintext)
    b5 = fonk10(fonk6(fonk5(b1, b5)))
    b5 = fonk4(fonk2((b3[2] << 8) + b3[3]), b5)
    b5 = fonk6(fonk5(b1, b5))
    return fonk3(fonk4(fonk2((b3[4] << 8) + b3[5]), b5))
def fonk11(ciphertext):
    def fonk12(s):
        return [fonk1(9, s[0]) ^ fonk1(2, s[2]), fonk1(9, s[1]) ^ fonk1(2, s[3]),
                fonk1(9, s[2]) ^ fonk1(2, s[0]), fonk1(9, s[3]) ^ fonk1(2, s[1])]
    b5 = fonk2(((b3[4] << 8) + b3[5]) ^ ciphertext)
    b5 = fonk5(b2, fonk6(b5))
    b5 = fonk12(fonk4(fonk2((b3[2] << 8) + b3[3]), b5))
    b5 = fonk5(b2, fonk6(b5))
    return fonk3(fonk4(fonk2((b3[0] << 8) + b3[1]), b5))