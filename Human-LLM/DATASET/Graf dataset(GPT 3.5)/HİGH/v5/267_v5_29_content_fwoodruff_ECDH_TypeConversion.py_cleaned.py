def fonk1(s):
    b1 = s.encode("hex")
    return int(b1, 16)
def fonk2(i):
    b2 = hex(i)
    return b2[2:-1].decode("hex")
b3 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
b4 = len(b3)
def fonk3(i):
    if i < 0:
        return ''
    b5 = ''
    while i >= b4:
        b6 = i % b4
        b5 = b3[b6] + b5
        i
    if i:
        b5 = b3[i] + b5
    return b5
def fonk4(s58):
    a1 = 0
    a2 = 1
    b7 = s58[::-1]
    for char in b7:
        b8 = b3.index(char)
        a1 += a2 * b8
        a2 *= b4
    return a1