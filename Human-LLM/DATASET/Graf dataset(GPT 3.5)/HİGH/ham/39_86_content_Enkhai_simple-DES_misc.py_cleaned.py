import binascii
def fonk1(text, b1 = 'utf-8', errors='surrogatepass'):
    b2 = bin(int(binascii.hexlify(text.encode(b1, errors)), 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk2(b2, b1 = 'utf-8', errors='surrogatepass'):
    b3 = int(b2, 2)
    return fonk3(b3).decode(b1, errors)
def fonk3(i):
    b4 = '%x' % i
    b3 = len(b4)
    return binascii.unhexlify(b4.zfill(b3 + (b3 & 1)))
def fonk4(text):
    b2 = bin(int(text, 16))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk5(value1, value2, num_of_bits):
    b2 = bin(int(value1, 2) + int(value2, 2))[2:]
    return b2.zfill(num_of_bits)[-num_of_bits:]
def fonk6(value1, value2):
    b2 = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return b2.zfill(8 * ((len(b2) + 7)
def fonk7(text, d):
    b5 = text[0:d]
    b6 = text[d:]
    return b6 + b5