import binascii
def fonk1(b8, b1 = 'utf-8', errors='surrogatepass'):
    b2 = bin(int(binascii.hexlify(b8.encode(b1, errors)), 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk2(b2, b1 = 'utf-8', errors='surrogatepass'):
    b3 = int(b2, 2)
    return fonk3(b3).decode(b1, errors)
def fonk3(i):
    b4 = '%x' % i
    b3 = len(b4)
    return binascii.unhexlify(b4.zfill(b3 + (b3 & 1)))
def fonk4(b8):
    b2 = bin(int(b8, 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk5(value1, value2, num_of_bits):
    b2 = bin(int(value1, 2) + int(value2, 2))[2:]
    return b2.zfill(num_of_bits)[-num_of_bits:]
def fonk6(value1, value2):
    b2 = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk7(b8, d):
    b5 = b8[0:d]
    b6 = b8[d:]
    return b6 + b5
if b7 = = "__main__":
    b8 = "Hello, World!"
    b9 = "AABB09182736CCDD"
    b10 = fonk1(b8)
    print(f"Binary representation of '{b8}': {b10}")
    b11 = fonk2(b10)
    print(f"Restored b8 from binary: {b11}")
    b12 = fonk4(b9)
    print(f"Binary representation of b9 '{b9}': {b12}")
    b13 = fonk5('1101', '1011', 4)
    print(f"Binary addition result: {b13}")
    b14 = fonk6('1101', '1011')
    print(f"XOR result: {b14}")
    b15 = fonk7('1101', 2)
    print(f"Left shift result: {b15}")