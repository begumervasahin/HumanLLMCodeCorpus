import binascii
def fonk1(b6, b1 = 'utf-8', errors='surrogatepass'):
    b2 = bin(int(binascii.hexlify(b6.encode(b1, errors)), 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk2(b2, b1 = 'utf-8', errors='surrogatepass'):
    b3 = int(b2, 2)
    return fonk3(b3).decode(b1, errors)
def fonk3(i):
    b4 = f'{i:x}'
    return binascii.unhexlify(b4.zfill(len(b4) + (len(b4) & 1)))
def fonk4(b6):
    b2 = bin(int(b6, 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk5(value1, value2, num_of_bits):
    b5 = int(value1, 2) + int(value2, 2)
    return bin(b5)[2:].zfill(num_of_bits)[-num_of_bits:]
def fonk6(value1, value2):
    b5 = int(value1, 2) ^ int(value2, 2)
    return bin(b5)[2:].zfill(max(len(value1), len(value2)))
def fonk7(b6, d):
    return b6[d:] + b6[:d]
def fonk8():
    b6 = "Hello, World!"
    b7 = "AABB09182736CCDD"
    b8 = fonk1(b6)
    print(f"Binary representation of '{b6}': {b8}")
    b9 = fonk2(b8)
    print(f"Restored b6 from binary: {b9}")
    b10 = fonk4(b7)
    print(f"Binary representation of b7 '{b7}': {b10}")
    b11 = fonk5('1101', '1011', 4)
    print(f"Binary addition b5: {b11}")
    b12 = fonk6('1101', '1011')
    print(f"XOR b5: {b12}")
    b13 = fonk7('1101', 2)
    print(f"Left shift b5: {b13}")
if b14 = = "__main__":
    fonk8()