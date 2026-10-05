import string
def fonk1(s):
    b1 = s.encode("hex")
    return int(b1, 16)
def fonk2(i):
    b2 = hex(i)
    return b2[2:].decode("hex")
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