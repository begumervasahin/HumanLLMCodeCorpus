import string
def string_to_bigint(s):
    encoded_hex = s.encode("hex")
    return int(encoded_hex, 16)
def bigint_to_string(i):
    hex_str = hex(i)
    return hex_str[2:].decode("hex")
BASE58_ALPHABET = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
BASE58_LENGTH = len(BASE58_ALPHABET)
def int_to_base58(i):
    if i < 0:
        return ''
    encoded_str = ''
    while i >= BASE58_LENGTH:
        remainder = i % BASE58_LENGTH
        encoded_str = BASE58_ALPHABET[remainder] + encoded_str
        i
    if i:
        encoded_str = BASE58_ALPHABET[i] + encoded_str
    return encoded_str
def base58_to_int(s58):
    result = 0
    multiplier = 1
    reversed_s58 = s58[::-1]
    for char in reversed_s58:
        char_value = BASE58_ALPHABET.index(char)
        result += multiplier * char_value
        multiplier *= BASE58_LENGTH
    return result
input_string = "Hello, World!"
print("Input string:", input_string)
bigint = string_to_bigint(input_string)
print("String to BigInt:", bigint)
output_string = bigint_to_string(bigint)
print("BigInt to String:", output_string)
base58_string = int_to_base58(bigint)
print("Int to Base58:", base58_string)
int_from_base58 = base58_to_int(base58_string)
print("Base58 to Int:", int_from_base58)