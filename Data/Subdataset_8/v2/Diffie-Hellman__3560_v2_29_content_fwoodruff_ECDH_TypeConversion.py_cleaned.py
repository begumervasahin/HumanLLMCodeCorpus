import string
def string_to_bigint(s):
    m = s.encode("hex")
    return int(m, 16)
def bigint_to_string(i):
    s = hex(i)
    return s[2:].decode("hex")
alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
base_count = len(alphabet)
def int_to_base58(i):
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
def base58_to_int(s58):
    i = 0
    multi = 1
    s58 = s58[::-1]
    for char in s58:
        i += multi * alphabet.index(char)
        multi *= base_count
    return i
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