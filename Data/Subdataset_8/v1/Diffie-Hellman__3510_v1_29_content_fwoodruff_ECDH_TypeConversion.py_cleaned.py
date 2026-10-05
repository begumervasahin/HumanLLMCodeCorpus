import string
def stringToBigInt(s):
    '''
    Maps a string to an integer using hexadecimal encoding.
    '''
    m = s.encode("hex")
    return int(m, 16)
def bigIntToString(i):
    '''
    Maps an integer to a string using hexadecimal decoding.
    '''
    s = hex(i)
    return s[2:].decode("hex")
alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
base_count = len(alphabet)
def intTob58(i):
    '''
    Maps an integer to a base-58 string using a custom base-58 alphabet.
    '''
    encode = ''
    if i < 0:
        return ''
    while i >= base_count:
        mod = i % base_count
        encode = alphabet[mod] + encode
        i = i
    if i:
        encode = alphabet[i] + encode
    return encode
def b58toInt(s58):
    '''
    Maps a base-58 string to an integer using a custom base-58 alphabet.
    '''
    i = 0
    multi = 1
    s58 = s58[::-1]
    for char in s58:
        i += multi * alphabet.index(char)
        multi *= base_count
    return i
input_string = "Hello, World!"
print("Input string:", input_string)
bigint = stringToBigInt(input_string)
print("String to BigInt:", bigint)
output_string = bigIntToString(bigint)
print("BigInt to String:", output_string)
base58_string = intTob58(bigint)
print("Int to Base58:", base58_string)
int_from_base58 = b58toInt(base58_string)
print("Base58 to Int:", int_from_base58)