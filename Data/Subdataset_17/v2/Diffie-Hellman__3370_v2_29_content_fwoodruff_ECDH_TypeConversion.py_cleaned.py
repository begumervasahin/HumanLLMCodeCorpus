import binascii
ALPHABET = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
BASE_COUNT = len(ALPHABET)
def string_to_big_int(s):
    hex_string = binascii.hexlify(s.encode()).decode()
    return int(hex_string, 16)
def big_int_to_string(i):
    hex_string = hex(i)[2:]
    byte_array = bytes.fromhex(hex_string)
    return byte_array.decode()
def int_to_b58(i):
    if i < 0:
        raise ValueError("Negative numbers cannot be encoded in base-58.")
    if i == 0:
        return ALPHABET[0]
    encoded_string = ''
    while i > 0:
        i, mod = divmod(i, BASE_COUNT)
        encoded_string = ALPHABET[mod] + encoded_string
    return encoded_string
def b58_to_int(s58):
    i = 0
    for char in s58:
        i = i * BASE_COUNT + ALPHABET.index(char)
    return i
if __name__ == "__main__":
    example_string = "Hello, World!"
    big_int = string_to_big_int(example_string)
    print(f"Big integer: {big_int}")
    restored_string = big_int_to_string(big_int)
    print(f"Restored string: {restored_string}")
    example_int = 123456789
    b58_string = int_to_b58(example_int)
    print(f"Base-58 string: {b58_string}")
    restored_int = b58_to_int(b58_string)
    print(f"Restored integer: {restored_int}")