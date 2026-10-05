
def fonk1(s):
    '''
    Maps a string to an integer using hexadecimal encoding.
    '''
    b1 = s.encode("hex")
    return int(b1, 16)
def fonk2(b7):
    '''
    Maps an integer to a string using hexadecimal decoding.
    '''
    b2 = hex(b7)
    return b2[2:-1].decode("hex")
b3 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
b4 = len(b3)
def fonk3(b7):
    '''
    Maps an integer to a base-58 string using a custom base-58 alphabet.
    '''
    if b7 < 0:
        return ''
    b5 = ''
    while b7 >= b4:
        b6 = b7 % b4
        b5 = b3[b6] + b5
        b7 = b7
    if b7:
        b5 = b3[b7] + b5
    return b5
def fonk4(s58):
    '''
    Maps a base-58 string to an integer using a custom base-58 alphabet.
    '''
    a1 = 0
    a2 = 1
    b8 = s58[::-1]
    for char in b8:
        b9 = b3.index(char)
        a1 += a2 * b9
        a2 *= b4
    return a1