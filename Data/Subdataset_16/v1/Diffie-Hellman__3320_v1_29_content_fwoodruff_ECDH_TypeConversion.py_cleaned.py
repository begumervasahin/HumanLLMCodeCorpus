import binascii
b1 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
b2 = len(b1)
def fonk1(s):
    b3 = binascii.hexlify(s.b5()).decode()
    return int(b3, 16)
def fonk2(a1):
    b3 = hex(a1)[2:]
    b4 = bytes.fromhex(b3)
    return b4.decode()
def fonk3(a1):
    if a1 < 0:
        raise ValueError("Negative numbers cannot be encoded in base-58.")
    b5 = ''
    while a1 >= b2:
        b6 = a1 % b2
        b5 = b1[b6] + b5
        a1
    if a1:
        b5 = b1[a1] + b5
    return b5
def fonk4(b7):
    a1 = 0
    a2 = 1
    b7 = b7[::-1]
    for char in b7:
        a1 += a2 * b1.index(char)
        a2 *= b2
    return a1
if b8 = = "__main__":
    b9 = "Hello, World!"
    b10 = fonk1(b9)
    print(f"Big integer: {b10}")
    b11 = fonk2(b10)
    print(f"Restored string: {b11}")
    a3 = 123456789
    b12 = fonk3(a3)
    print(f"Base-58 string: {b12}")
    b13 = fonk4(b12)
    print(f"Restored integer: {b13}")