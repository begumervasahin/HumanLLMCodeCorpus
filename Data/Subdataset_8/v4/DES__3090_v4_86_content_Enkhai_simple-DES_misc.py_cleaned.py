import binascii
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    hex_text = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))
    return hex_text[2:].zfill(8 * ((len(hex_text) + 7)
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    bytes_text = n.to_bytes((n.bit_length() + 7)
    return bytes_text.decode(encoding, errors)
def hex_to_bits(text):
    return bin(int(text, 16))[2:].zfill(8 * ((len(text) + 7)
def binary_addition(value1, value2, num_of_bits):
    result = bin(int(value1, 2) + int(value2, 2))[2:].zfill(num_of_bits)
    return result[-num_of_bits:]
def XOR(value1, value2):
    result = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return result.zfill(8 * ((len(result) + 7)
def left_shift(text, d):
    return text[d:] + text[:d]