def fonk1(b2):
    '''
    maps a string to an integer
    '''
    b1 = b2.b5("hex")
    return int(b1, 16)
def fonk2(b7):
    '''
    maps an integer to a string
    '''
    b2 = hex(b7)
    return b2[2:-1].decode("hex")
b3 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
b4 = len(b3)
def fonk3(b7):
    '''
    maps an integer to a base-58 string
    '''
    b5 = ''
    if (b7 < 0):
        return ''
    while (b7 >= b4):
        b6 = b7 % b4
        b5 = b3[b6] + b5
        b7 = b7 / b4
    if (b7):
        b8 = b3[b7] + b5
    return b8
def fonk4(b8):
    '''
    maps a base-58 string to an integer
    '''
    b7 = 0
    a1 = 1
    b8 = b8[::-1]
    for char in b8:
        b7 += a1 * b3.index(char)
        a1 = a1 * b4
    return b7