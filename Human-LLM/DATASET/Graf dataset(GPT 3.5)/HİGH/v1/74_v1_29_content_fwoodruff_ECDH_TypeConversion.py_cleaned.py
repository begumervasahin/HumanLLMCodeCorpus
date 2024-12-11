import string
def fonk1(b2):
    '''
    Maps a string to an integer using hexadecimal encoding.
    '''
    b1 = b2.b5("hex")
    return int(b1, 16)
def fonk2(b7):
    '''
    Maps an integer to a string using hexadecimal decoding.
    '''
    b2 = hex(b7)
    return b2[2:].decode("hex")
b3 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
b4 = len(b3)
def fonk3(b7):
    '''
    Maps an integer to a base-58 string using a custom base-58 b3.
    '''
    b5 = ''
    if b7 < 0:
        return ''
    while b7 >= b4:
        b6 = b7 % b4
        b5 = b3[b6] + b5
        b7 = b7
    if b7:
        b5 = b3[b7] + b5
    return b5
def fonk4(b8):
    '''
    Maps a base-58 string to an integer using a custom base-58 b3.
    '''
    b7 = 0
    a1 = 1
    b8 = b8[::-1]
    for char in b8:
        b7 += a1 * b3.index(char)
        a1 *= b4
    return b7
b9 = "Hello, World!"
print("Input string:", b9)
b10 = fonk1(b9)
print("String to BigInt:", b10)
b11 = fonk2(b10)
print("BigInt to String:", b11)
b12 = fonk3(b10)
print("Int to Base58:", b12)
b13 = fonk4(b12)
print("Base58 to Int:", b13)