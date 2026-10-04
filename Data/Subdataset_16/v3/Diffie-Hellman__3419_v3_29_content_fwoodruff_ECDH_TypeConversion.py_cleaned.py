import binascii
b1 = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
b2 = len(b1)
def fonk1(s):
    b3 = binascii.hexlify(s.encode()).decode()
    return int(b3, 16)
def fonk2(b5):
    b3 = hex(b5)[2:]
    b4 = bytes.fromhex(b3)
    return b4.decode()
def fonk3(b5):
    if b5 < 0:
        raise ValueError("Negative numbers cannot be encoded in base-58.")
    if b5 = = 0:
        return b1[0]
    b6 = ''
    while b5 > 0:
        b5, b7 = divmod(b5, b2)
        b6 = b1[b7] + b6
    return b6
def fonk4(s58):
    b5 = 0
    for char in s58:
        b5 = b5 * b2 + b1.index(char)
    return b5
if b8 = = "__main__":
    b9 = "Hello, World!"
    b10 = fonk1(b9)
    print(f"Big integer: {b10}")
    b11 = fonk2(b10)
    print(f"Restored string: {b11}")
    a1 = 123456789
    b12 = fonk3(a1)
    print(f"Base-58 string: {b12}")
    b13 = fonk4(b12)
    print(f"Restored integer: {b13}")