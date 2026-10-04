
S_BOX = [0x9, 0x4, 0xa, 0xb, 0xd, 0x1, 0x8, 0x5,
         0x6, 0x2, 0x0, 0x3, 0xc, 0xe, 0xf, 0x7]
S_BOX_INV = [0xa, 0x5, 0x9, 0xb, 0x1, 0x7, 0x8, 0xf,
             0x6, 0x0, 0x2, 0x3, 0xc, 0x4, 0xd, 0xe]
round_keys = [None] * 6
def multiply(p1, p2):
    p = 0
    while p2:
        if p2 & 0b1:
            p ^= p1
        p1 <<= 1
        if p1 & 0b10000:
            p1 ^= 0b11
        p2 >>= 1
    return p & 0b1111
def int_to_vector(n):
    return [n >> 12, (n >> 4) & 0xf, (n >> 8) & 0xf, n & 0xf]
def vector_to_int(m):
    return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]
def add_keys(s1, s2):
    return [i ^ j for i, j in zip(s1, s2)]
def substitute_nibbles(sbox, s):
    return [sbox[e] for e in s]
def shift_row(s):
    return [s[0], s[1], s[3], s[2]]
def key_expansion(key):
    def sub_2_nibbles(b):
        return S_BOX[b >> 4] + (S_BOX[b & 0x0f] << 4)
    RCON1, RCON2 = 0b10000000, 0b00110000
    round_keys[0] = (key & 0xff00) >> 8
    round_keys[1] = key & 0x00ff
    round_keys[2] = round_keys[0] ^ RCON1 ^ sub_2_nibbles(round_keys[1])
    round_keys[3] = round_keys[2] ^ round_keys[1]
    round_keys[4] = round_keys[2] ^ RCON2 ^ sub_2_nibbles(round_keys[3])
    round_keys[5] = round_keys[4] ^ round_keys[3]
def encrypt(plaintext):
    def mix_columns(s):
        return [s[0] ^ multiply(4, s[2]), s[1] ^ multiply(4, s[3]),
                s[2] ^ multiply(4, s[0]), s[3] ^ multiply(4, s[1])]
    state = int_to_vector(((round_keys[0] << 8) + round_keys[1]) ^ plaintext)
    state = mix_columns(shift_row(substitute_nibbles(S_BOX, state)))
    state = add_keys(int_to_vector((round_keys[2] << 8) + round_keys[3]), state)
    state = shift_row(substitute_nibbles(S_BOX, state))
    return vector_to_int(add_keys(int_to_vector((round_keys[4] << 8) + round_keys[5]), state))
def decrypt(ciphertext):
    def inv_mix_columns(s):
        return [multiply(9, s[0]) ^ multiply(2, s[2]), multiply(9, s[1]) ^ multiply(2, s[3]),
                multiply(9, s[2]) ^ multiply(2, s[0]), multiply(9, s[3]) ^ multiply(2, s[1])]
    state = int_to_vector(((round_keys[4] << 8) + round_keys[5]) ^ ciphertext)
    state = substitute_nibbles(S_BOX_INV, shift_row(state))
    state = inv_mix_columns(add_keys(int_to_vector((round_keys[2] << 8) + round_keys[3]), state))
    state = substitute_nibbles(S_BOX_INV, shift_row(state))
    return vector_to_int(add_keys(int_to_vector((round_keys[0] << 8) + round_keys[1]), state))
if __name__ == "__main__":
    key = 0x3a94d63f
    plaintext = 0x1234
    key_expansion(key)
    ciphertext = encrypt(plaintext)
    decrypted = decrypt(ciphertext)
    print(f"Plaintext: 0x{plaintext:04x}")
    print(f"Ciphertext: 0x{ciphertext:04x}")
    print(f"Decrypted: 0x{decrypted:04x}")