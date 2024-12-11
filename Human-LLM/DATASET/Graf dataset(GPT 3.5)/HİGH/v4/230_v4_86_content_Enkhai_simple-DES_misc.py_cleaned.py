import binascii
def fonk1(text, b1 = 'utf-8', errors='surrogatepass'):
    b2 = bin(int(binascii.hexlify(text.encode(b1, errors)), 16))
    return b2[2:].zfill(8 * ((len(b2) + 7)
def fonk2(bits, b1 = 'utf-8', errors='surrogatepass'):
    b3 = int(bits, 2)
    b4 = b3.to_bytes((b3.bit_length() + 7)
    return b4.decode(b1, errors)
def fonk3(text):
    return bin(int(text, 16))[2:].zfill(8 * ((len(text) + 7)
def fonk4(value1, value2, num_of_bits):
    b5 = bin(int(value1, 2) + int(value2, 2))[2:].zfill(num_of_bits)
    return b5[-num_of_bits:]
def fonk5(value1, value2):
    b5 = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return b5.zfill(8 * ((len(b5) + 7)
def fonk6(text, d):
    return text[d:] + text[:d]