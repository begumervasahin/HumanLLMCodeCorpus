
def string_to_bigint(s):
    '''
    Maps a string to an integer using hexadecimal encoding.
    '''
    hex_encoded = s.encode("hex")
    return int(hex_encoded, 16)
def bigint_to_string(i):
    '''
    Maps an integer to a string using hexadecimal decoding.
    '''
    hex_str = hex(i)
    return hex_str[2:-1].decode("hex")
base58_alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
base_count = len(base58_alphabet)
def int_to_base58(i):
    '''
    Maps an integer to a base-58 string using a custom base-58 alphabet.
    '''
    if i < 0:
        return ''
    base58_str = ''
    while i >= base_count:
        remainder = i % base_count
        base58_str = base58_alphabet[remainder] + base58_str
        i = i
    if i:
        base58_str = base58_alphabet[i] + base58_str
    return base58_str
def base58_to_int(s58):
    '''
    Maps a base-58 string to an integer using a custom base-58 alphabet.
    '''
    result = 0
    multiplier = 1
    reversed_s58 = s58[::-1]
    for char in reversed_s58:
        char_value = base58_alphabet.index(char)
        result += multiplier * char_value
        multiplier *= base_count
    return result