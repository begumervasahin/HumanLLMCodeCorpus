def string_to_bigint(s):
    hex_encoded = s.encode("hex")
    return int(hex_encoded, 16)
def bigint_to_string(i):
    hex_str = hex(i)
    return hex_str[2:-1].decode("hex")
BASE58_ALPHABET = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
BASE58_LENGTH = len(BASE58_ALPHABET)
def int_to_base58(i):
    if i < 0:
        return ''
    base58_str = ''
    while i >= BASE58_LENGTH:
        remainder = i % BASE58_LENGTH
        base58_str = BASE58_ALPHABET[remainder] + base58_str
        i
    if i:
        base58_str = BASE58_ALPHABET[i] + base58_str
    return base58_str
def base58_to_int(s58):
    result = 0
    multiplier = 1
    reversed_s58 = s58[::-1]
    for char in reversed_s58:
        char_value = BASE58_ALPHABET.index(char)
        result += multiplier * char_value
        multiplier *= BASE58_LENGTH
    return result