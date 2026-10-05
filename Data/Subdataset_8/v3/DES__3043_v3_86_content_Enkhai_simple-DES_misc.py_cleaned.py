import binascii
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    hex_text = binascii.hexlify(text.encode(encoding, errors)).decode()
    bits = bin(int(hex_text, 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7)
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    hex_text = '%x' % n
    hex_text = '0' + hex_text if len(hex_text) % 2 != 0 else hex_text
    bytes_text = binascii.unhexlify(hex_text)
    return bytes_text.decode(encoding, errors)
def hex_to_bits(text):
    bits = bin(int(text, 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7)
def binary_addition(value1, value2, num_of_bits):
    sum_value = bin(int(value1, 2) + int(value2, 2))[2:]
    return sum_value.zfill(num_of_bits)[-num_of_bits:]
def XOR(value1, value2):
    xor_result = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return xor_result.zfill(8 * ((len(xor_result) + 7)
def left_shift(text, d):
    return text[d:] + text[:d]
text = "Hello, World!"
bits = text_to_bits(text)
print("Text to bits:", bits)
text_decoded = text_from_bits(bits)
print("Bits to text:", text_decoded)