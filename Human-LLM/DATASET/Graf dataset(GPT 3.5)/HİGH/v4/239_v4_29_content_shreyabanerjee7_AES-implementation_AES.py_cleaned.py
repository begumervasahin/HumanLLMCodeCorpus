
b1 = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
]
b2 = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
]
b3 = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
def fonk1(b17):
    b4 = []
    for i in range(b6):
        b4.append([b17[b6 * i], b17[b6 * i + 1], b17[b6 * i + 2], b17[b6 * i + 3]])
    for i in range(b6, b6 * 11):
        b5 = b4[i-1]
        if i % b6 = = 0:
            b5 = fonk13(fonk4(fonk2(b5, 1)), [b3[int(i/b6)-1], 0, 0, 0])
        b4.append(fonk13(b4[i-b6], b5))
    return b4
def fonk2(word, a):
    return word[a:] + word[0:a]
def fonk3(word, a):
    return word[len(word)-a:] + word[0:len(word)-a]
def fonk4(word):
    return [b1[b] for b in word]
def fonk5(word):
    return [b2[b] for b in word]
def fonk6(state, b4):
    return fonk13(state, b4)
def fonk7(a, b):
    return [x ^ y for x, y in zip(a, b)]
def fonk8(state):
    b7 = [0] * len(state)
    for i in range(b6):
        b8 = [state[0 + i], state[b6 + i], state[b12 + i], state[12 + i]]
        b9 = fonk2(b8, i)
        for j in range(b6):
            b7[b6 * j + i] = b9[j]
    return b7
def fonk9(state):
    b7 = [0] * len(state)
    for i in range(b6):
        b8 = [state[0 + i], state[b6 + i], state[b12 + i], state[12 + i]]
        b9 = fonk3(b8, i)
        for j in range(b6):
            b7[b6 * j + i] = b9[j]
    return b7
def fonk10(va):
    return va
def fonk11(va):
    b10 = 0x11b
    b11 = va << 1
    if b11 >> b12 = = 0:
        return b11
    else:
        return (b11 ^ b10)
def fonk12(la):
    b13 = fonk11(la[0]) ^ into_three(la[1]) ^ fonk10(la[2]) ^ fonk10(la[3])
    b14 = fonk10(la[0]) ^ fonk11(la[1]) ^ into_three(la[2]) ^ fonk10(la[3])
    b15 = fonk10(la[0]) ^ fonk10(la[1]) ^ fonk11(la[2]) ^ into_three(la[3])
    b16 = into_three(la[0]) ^ fonk10(la[1]) ^ fonk10(la[2]) ^ fonk11(la[3])
    return [b13, b14, b15, b16]
def fonk13(a, b):
    return [x ^ y for x, y in zip(a, b)]
def fonk14(la):
    b13 = into_fourteen(la[0]) ^ into_eleven(la[1]) ^ into_thirteen(la[2]) ^ into_nine(la[3])
    b14 = into_nine(la[0]) ^ into_fourteen(la[1]) ^ into_eleven(la[2]) ^ into_thirteen(la[3])
    b15 = into_thirteen(la[0]) ^ into_nine(la[1]) ^ into_fourteen(la[2]) ^ into_eleven(la[3])
    b16 = into_eleven(la[0]) ^ into_thirteen(la[1]) ^ into_nine(la[2]) ^ into_fourteen(la[3])
    return [b13, b14, b15, b16]
def fonk15(s, keystring):
    b17 = [ord(c) for c in keystring]
    b18 = [ord(c) for c in s]
    b19 = len(s)
    b20 = []
    for i in range(int(b19 / 16)):
        b20.append(Cipher(b18[i * 16:(i + 1) * 16], b17))
    if b19 % 16 > 0:
        b20.append(Cipher(b18[int(b19 / 16) * 16:] + [0 for j in range(16 - b19 % 16)], b17))
    return b20
