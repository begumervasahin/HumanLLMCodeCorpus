from random import randint
CHAR_PER_BLOCK = 2
N = 8 * CHAR_PER_BLOCK
MMI = 87177
SUPER_INCREASING_SEQUENCE = [1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]
GENERAL_KNAPSACK = [89, 356, 534, 1068, 2225, 4450, 9167, 18245, 36401, 72980, 41023, 81868, 59066, 13106, 26212, 52513]
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def are_coprime(a, b):
    return find_gcd(a, b) == 1
def choose_m_n():
    sum_sik = sum(SUPER_INCREASING_SEQUENCE)
    m = randint(41, 100)
    n = 0
    while n < sum_sik:
        if are_coprime(m, sum_sik + 1):
            n = sum_sik + 1
    return m, n
def build_general_knapsack(m, n, sik):
    knapsack = []
    for ai in sik:
        knapsack.append((ai * m) % n)
    return knapsack
def find_modulo_multiplicative_inverse(A, M):
    gcd, x, y = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    return x
def extended_euclid_gcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        quotient = old_r / r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return [old_r, old_s, old_t]
def char_to_ascii_binary(character):
    ascii_value = ord(character)
    binary_representation = "{0:b}".format(ascii_value)
    if len(binary_representation) <= 7:
        binary_representation = '0' * (8 - len(binary_representation)) + binary_representation
    return binary_representation
def encrypt_single_character(character):
    binary_representation = ""
    for i in range(len(character)):
        binary_representation = char_to_ascii_binary(character[i])[::-1] + binary_representation
    return sum([int(x) * y for x, y in zip(list(binary_representation), GENERAL_KNAPSACK)])
def decrypt_single_character(number):
    res = ""
    d = (number * MMI) % N
    for sik_i in SUPER_INCREASING_SEQUENCE[::-1]:
        if d >= sik_i:
            res = "1" + res
            d -= sik_i
        else:
            res = "0" + res
    res = res[::-1]
    char1, char2 = chr(bit_to_int(res[:8])), chr(bit_to_int(res[8:]))
    return char1 + char2
def bit_to_int(binary_string):
    out = 0
    for bit in list(binary_string):
        out = (out << 1) | int(bit)
    return out
def encrypt_message(message):
    msg_blocks = []
    encrypted = []
    if len(message) % CHAR_PER_BLOCK != 0:
        message += " " * (CHAR_PER_BLOCK - len(message) % CHAR_PER_BLOCK)
    for i in range(0, len(message), CHAR_PER_BLOCK):
        msg_blocks.append(message[i:i + CHAR_PER_BLOCK])
    for block in msg_blocks:
        encrypted.append(encrypt_single_character(block))
    return encrypted
def decrypt_message(crypto_list):
    plaintext = ""
    for num in crypto_list:
        plaintext += decrypt_single_character(num)
    return plaintext
print(decrypt_message(encrypt_message("ciao, io mi chiamo francesco ")))
with open("encrypted", "r") as fin:
    text = ""
    for line in fin:
        text += decrypt_message([int(line, 16)])
    print(text)