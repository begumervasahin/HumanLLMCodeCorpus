
s_box = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
]
s_box_inv = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
]
rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
def key_expansion(key):
    w = []
    for i in range(4):
        w.append([key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3]])
    for i in range(4, 4 * 11):
        temp = w[i-1]
        if i % 4 == 0:
            temp = add_lists(sub_word(rot_word(temp, 1)), [rcon[int(i/4)-1], 0, 0, 0])
        w.append(add_lists(w[i-4], temp))
    return w
def rot_word(word, a):
    return word[a:] + word[0:a]
def rot_word_inv(word, a):
    return word[len(word)-a:] + word[0:len(word)-a]
def sub_word(word):
    return [s_box[b] for b in word]
def sub_word_inv(word):
    return [s_box_inv[b] for b in word]
def add_round_key(state, w):
    return add_lists(state, w)
def add_lists(a, b):
    return [x ^ y for x, y in zip(a, b)]
def shift_rows(state):
    output_state = [0] * len(state)
    for i in range(4):
        row = [state[0 + i], state[4 + i], state[8 + i], state[12 + i]]
        rotated_row = rot_word(row, i)
        for j in range(4):
            output_state[4 * j + i] = rotated_row[j]
    return output_state
def inv_shift_rows(state):
    output_state = [0] * len(state)
    for i in range(4):
        row = [state[0 + i], state[4 + i], state[8 + i], state[12 + i]]
        rotated_row = rot_word_inv(row, i)
        for j in range(4):
            output_state[4 * j + i] = rotated_row[j]
    return output_state
def into_one(va):
    return va
def into_two(va):
    op = 0x11b
    out = va << 1
    if out >> 8 == 0:
        return out
    else:
        return (out ^ op)
def mix_column(la):
    fr = into_two(la[0]) ^ into_three(la[1]) ^ into_one(la[2]) ^ into_one(la[3])
    se = into_one(la[0]) ^ into_two(la[1]) ^ into_three(la[2]) ^ into_one(la[3])
    th = into_one(la[0]) ^ into_one(la[1]) ^ into_two(la[2]) ^ into_three(la[3])
    fo = into_three(la[0]) ^ into_one(la[1]) ^ into_one(la[2]) ^ into_two(la[3])
    return [fr, se, th, fo]
def add_lists(a, b):
    return [x ^ y for x, y in zip(a, b)]
def inv_mix_column(la):
    fr = into_fourteen(la[0]) ^ into_eleven(la[1]) ^ into_thirteen(la[2]) ^ into_nine(la[3])
    se = into_nine(la[0]) ^ into_fourteen(la[1]) ^ into_eleven(la[2]) ^ into_thirteen(la[3])
    th = into_thirteen(la[0]) ^ into_nine(la[1]) ^ into_fourteen(la[2]) ^ into_eleven(la[3])
    fo = into_eleven(la[0]) ^ into_thirteen(la[1]) ^ into_nine(la[2]) ^ into_fourteen(la[3])
    return [fr, se, th, fo]
def encrypt(s, keystring):
    key = [ord(c) for c in keystring]
    plaintextint = [ord(c) for c in s]
    l = len(s)
    ciphertext = []
    for i in range(int(l / 16)):
        ciphertext.append(Cipher(plaintextint[i * 16:(i + 1) * 16], key))
    if l % 16 > 0:
        ciphertext.append(Cipher(plaintextint[int(l / 16) * 16:] + [0 for j in range(16 - l % 16)], key))
    return ciphertext
