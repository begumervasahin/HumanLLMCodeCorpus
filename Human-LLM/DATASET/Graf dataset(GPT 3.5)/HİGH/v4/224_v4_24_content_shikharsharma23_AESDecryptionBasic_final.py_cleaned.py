import sys
def fonk1(encrypted_ints, key):
    b1 = bytearray(encrypted_ints)
    b2 = fonk2(b1, key)
    return fonk10(b2)
def fonk2(data, key):
    b3 = fonk3(key)
    b4 = bytearray()
    for byte in data:
        b5 = fonk3(byte)
        b6 = fonk5(b5, b3)
        b4.append(fonk4(b6))
    return b4
def fonk3(byte):
    return [(byte >> (6 - 2 * i)) & 0x03 for i in range(4)]
def fonk4(b7):
    return sum(n << (6 - 2 * i) for i, n in enumerate(b7))
def fonk5(b7, b3):
    b7 = fonk6(b7, b3)
    b7 = fonk7(b7)
    b7 = fonk8(b7)
    b7 = fonk6(b7, b3)
    b7 = fonk9(b7)
    b7 = fonk7(b7)
    b7 = fonk8(b7)
    b7 = fonk6(b7, b3)
    return b7
def fonk6(b7, b3):
    return [n ^ k for n, k in zip(b7, b3)]
def fonk7(b7):
    b7[2], b7[3] = b7[3], b7[2]
    return b7
def fonk8(b7):
    b8 = {0: 2, 1: 0, 2: 3, 3: 1}
    return [b8[n] for n in b7]
def fonk9(b7):
    return [(b7[i] - b7[i + 2]) % 4 for i in range(2)] + b7[2:]
def fonk10(byte_array):
    return ''.join(chr(b) for b in byte_array)
def fonk11():
    b9 = [
        132, 201, 141, 74, 140, 94, 141, 140, 141, 15, 31, 164, 90, 229, 201, 141,
        78, 114, 241, 217, 141, 217, 140, 180, 141, 164, 51, 141, 188, 221, 31, 164,
        241, 177, 141, 140, 51, 217, 141, 201, 229, 152, 141, 78, 241, 114, 78, 102, 94,
        141, 74, 152, 31, 152, 141, 94, 201, 31, 164, 102, 164, 51, 90, 141, 201, 229,
        164, 31, 201, 152, 152, 51, 115
    ]
    a1 = 84
    b10 = fonk1(b9, a1)
    print("Decrypted text:", b10)
if b11 = = '__main__':
    fonk11()