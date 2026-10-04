
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
    return [n >> 12, (n >> 4) & 0xf, (n >> 8) & 0xf, n & 0xf]
def fonk3(m):
    return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]
def fonk4(s1, s2):
    return [i ^ j for i, j in zip(s1, s2)]
def fonk5(sbox, s):
    return [sbox[e] for e in s]
def fonk6(s):
    return [s[0], s[1], s[3], s[2]]
def fonk7(b7):
    def fonk8(b):
        return b1[b >> 4] + (b1[b & 0x0f] << 4)
    Rcon1, b4 = 0b10000000, 0b00110000
    b3[0] = (b7 & 0xff00) >> 8
    b3[1] = b7 & 0x00ff
    b3[2] = b3[0] ^ Rcon1 ^ fonk8(b3[1])
    b3[3] = b3[2] ^ b3[1]
    b3[4] = b3[2] ^ b4 ^ fonk8(b3[3])
    b3[5] = b3[4] ^ b3[3]
def fonk9(b8):
    def fonk10(s):
        return [s[0] ^ fonk1(4, s[2]), s[1] ^ fonk1(4, s[3]),
                s[2] ^ fonk1(4, s[0]), s[3] ^ fonk1(4, s[1])]
    b5 = fonk2(((b3[0] << 8) + b3[1]) ^ b8)
    b5 = fonk10(fonk6(fonk5(b1, b5)))
    b5 = fonk4(fonk2((b3[2] << 8) + b3[3]), b5)
    b5 = fonk6(fonk5(b1, b5))
    return fonk3(fonk4(fonk2((b3[4] << 8) + b3[5]), b5))
def fonk11(b9):
    def fonk12(s):
        return [fonk1(9, s[0]) ^ fonk1(2, s[2]), fonk1(9, s[1]) ^ fonk1(2, s[3]),
                fonk1(9, s[2]) ^ fonk1(2, s[0]), fonk1(9, s[3]) ^ fonk1(2, s[1])]
    b5 = fonk2(((b3[4] << 8) + b3[5]) ^ b9)
    b5 = fonk5(b2, fonk6(b5))
    b5 = fonk12(fonk4(fonk2((b3[2] << 8) + b3[3]), b5))
    b5 = fonk5(b2, fonk6(b5))
    return fonk3(fonk4(fonk2((b3[0] << 8) + b3[1]), b5))
if b6 = = "__main__":
    b7 = 0x3a94d63f
    b8 = 0x1234
    fonk7(b7)
    b9 = fonk9(b8)
    b10 = fonk11(b9)
    print(f"Plaintext: 0x{b8:04x}")
    print(f"Ciphertext: 0x{b9:04x}")
    print(f"Decrypted: 0x{b10:04x}")