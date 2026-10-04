import binascii
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7)
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
def hex_to_bits(text):
    bits = bin(int(text, 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7)
def binary_addition(value1, value2, num_of_bits):
    bits = bin(int(value1, 2) + int(value2, 2))[2:]
    return bits.zfill(num_of_bits)[-num_of_bits:]
def XOR(value1, value2):
    bits = bin(int(value1, 2) ^ int(value2, 2))[2:]
    return bits.zfill(8 * ((len(bits) + 7)
def left_shift(text, d):
    return text[d:] + text[:d]
def main():
    text = "Hello, World!"
    key = "AABB09182736CCDD"
    binary_text = text_to_bits(text)
    print(f"Binary representation of '{text}': {binary_text}")
    restored_text = text_from_bits(binary_text)
    print(f"Restored text from binary: {restored_text}")
    binary_key = hex_to_bits(key)
    print(f"Binary representation of key '{key}': {binary_key}")
    added_binary = binary_addition('1101', '1011', 4)
    print(f"Binary addition result: {added_binary}")
    xor_result = XOR('1101', '1011')
    print(f"XOR result: {xor_result}")
    shifted_binary = left_shift('1101', 2)
    print(f"Left shift result: {shifted_binary}")
if __name__ == "__main__":
    main()