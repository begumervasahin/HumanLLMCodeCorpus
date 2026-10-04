import binascii
def fonk1(b5, b1 = 'utf-8', errors='surrogatepass'):
    b2 = bin(int(binascii.hexlify(b5.encode(b1, errors)), 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk2(b2, b1 = 'utf-8', errors='surrogatepass'):
    b3 = int(b2, 2)
    return fonk3(b3).decode(b1, errors)
def fonk3(i):
    b4 = '%x' % i
    b3 = len(b4)
    return binascii.unhexlify(b4.zfill(b3 + (b3 & 1)))
def fonk4(b5):
    b2 = bin(int(b5, 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk5(value1, value2, num_of_bits):
    b2 = bin(int(value1, 2) + int(value2, 2))[2:]
    return b2.zfill(num_of_bits)[-num_of_bits:]
def fonk6(value1, value2):
    b2 = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk7(b5, d):
    return b5[d:] + b5[:d]
def fonk8():
    b5 = "Hello, World!"
    b6 = "AABB09182736CCDD"
    b7 = fonk1(b5)
    print(f"Binary representation of '{b5}': {b7}")
    b8 = fonk2(b7)
    print(f"Restored b5 from binary: {b8}")
    b9 = fonk4(b6)
    print(f"Binary representation of b6 '{b6}': {b9}")
    b10 = fonk5('1101', '1011', 4)
    print(f"Binary addition result: {b10}")
    b11 = fonk6('1101', '1011')
    print(f"XOR result: {b11}")
    b12 = fonk7('1101', 2)
    print(f"Left shift result: {b12}")
if b13 = = "__main__":
    fonk8()