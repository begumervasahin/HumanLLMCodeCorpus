import binascii
def fonk1(b8, b1 = 'utf-8', errors='surrogatepass'):
    b2 = binascii.hexlify(b8.encode(b1, errors)).decode()
    b3 = bin(int(b2, 16))[2:]
    return b3.zfill(8 * ((len(b3) + 7)
def fonk2(b3, b1 = 'utf-8', errors='surrogatepass'):
    b4 = int(b3, 2)
    b2 = '%x' % b4
    b2 = '0' + b2 if len(b2) % 2 != 0 else b2
    b5 = binascii.unhexlify(b2)
    return b5.decode(b1, errors)
def fonk3(b8):
    b3 = bin(int(b8, 16))[2:]
    return b3.zfill(8 * ((len(b3) + 7)
def fonk4(value1, value2, num_of_bits):
    b6 = bin(int(value1, 2) + int(value2, 2))[2:]
    return b6.zfill(num_of_bits)[-num_of_bits:]
def fonk5(value1, value2):
    b7 = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return b7.zfill(8 * ((len(b7) + 7)
def fonk6(b8, d):
    return b8[d:] + b8[:d]
b8 = "Hello, World!"
b3 = fonk1(b8)
print("Text to b3:", b3)
b9 = fonk2(b3)
print("Bits to b8:", b9)