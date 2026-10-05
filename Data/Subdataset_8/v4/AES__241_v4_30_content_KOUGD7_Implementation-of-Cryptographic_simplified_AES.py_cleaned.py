
s_box = [0x9, 0x4, 0xa, 0xb, 0xd, 0x1, 0x8, 0x5,
         0x6, 0x2, 0x0, 0x3, 0xc, 0xe, 0xf, 0x7]
s_box_inv = [0xa, 0x5, 0x9, 0xb, 0x1, 0x7, 0x8, 0xf,
             0x6, 0x0, 0x2, 0x3, 0xc, 0x4, 0xd, 0xe]
w = [None] * 6
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
def int_to_vec(n):
    return [n >> 12, (n >> 4) & 0xf, (n >> 8) & 0xf,  n & 0xf]
def vec_to_int(m):
    return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]
def add_key(s1, s2):
    return [i ^ j for i, j in zip(s1, s2)]
def sub_nibbles(s_box, s):
    return [s_box[e] for e in s]
def shift_rows(s):
    return [s[0], s[1], s[3], s[2]]
def key_expansion(key):
    def sub_2_nibbles(b):
        return s_box[b >> 4] + (s_box[b & 0x0f] << 4)
    rcon1, rcon2 = 0b10000000, 0b00110000
    w[0] = (key & 0xff00) >> 8
    w[1] = key & 0x00ff
    w[2] = w[0] ^ rcon1 ^ sub_2_nibbles(w[1])
    w[3] = w[2] ^ w[1]
    w[4] = w[2] ^ rcon2 ^ sub_2_nibbles(w[3])
    w[5] = w[4] ^ w[3]
def encrypt(plaintext):
    def mix_columns(s):
        return [s[0] ^ multiply(4, s[2]), s[1] ^ multiply(4, s[3]),
                s[2] ^ multiply(4, s[0]), s[3] ^ multiply(4, s[1])]
    state = int_to_vec(((w[0] << 8) + w[1]) ^ plaintext)
    state = mix_columns(shift_rows(sub_nibbles(s_box, state)))
    state = add_key(int_to_vec((w[2] << 8) + w[3]), state)
    state = shift_rows(sub_nibbles(s_box, state))
    return vec_to_int(add_key(int_to_vec((w[4] << 8) + w[5]), state))
def decrypt(ciphertext):
    def inv_mix_columns(s):
        return [multiply(9, s[0]) ^ multiply(2, s[2]), multiply(9, s[1]) ^ multiply(2, s[3]),
                multiply(9, s[2]) ^ multiply(2, s[0]), multiply(9, s[3]) ^ multiply(2, s[1])]
    state = int_to_vec(((w[4] << 8) + w[5]) ^ ciphertext)
    state = sub_nibbles(s_box_inv, shift_rows(state))
    state = inv_mix_columns(add_key(int_to_vec((w[2] << 8) + w[3]), state))
    state = sub_nibbles(s_box_inv, shift_rows(state))
    return vec_to_int(add_key(int_to_vec((w[0] << 8) + w[1]), state))