import random
char_per_block = 2
N = 8 * char_per_block
def build_superincreasing_knapsack():
    SIK = [0] * N
    for i in range(N):
        sum_prev = sum(SIK[:i])
        SIK[i] = sum_prev + random.randint(1, 5)
    total = 0
    for i in range(len(SIK) - 1):
        total += SIK[i]
        if total > SIK[i + 1]:
            print("NON SIK")
    return SIK
SIK = [1, 4, 6, 12, 25, 50, 103, 205, 409, 820, 1639, 3276, 6554, 13106, 26212, 52425]
m, n = 89, 104848
mmi = 87177
GK = [89, 356, 534, 1068, 2225, 4450, 9167, 18245, 36401, 72980, 41023, 81868, 59066, 13106, 26212, 52513]
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def coprime(a, b):
    return gcd(a, b) == 1
def choose_m_n():
    sum_sik = sum(SIK)
    m = random.randint(41, 100)
    n = 0
    while n < sum_sik:
        if coprime(m, sum_sik + 1):
            n = sum_sik + 1
    return m, n
def build_general_knapsack(m, n, SIK):
    return [(ai * m) % n for ai in SIK]
def extended_euclid_gcd(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a
    while r != 0:
        quotient = old_r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t
def modulo_multiplicative_inverse(A, M):
    gcd, x, _ = extended_euclid_gcd(A, M)
    if x < 0:
        x += M
    return x
def str2ascii(char):
    binary = "{0:b}".format(ord(char))
    return binary.zfill(8)
def encrypt_N_char(chars):
    bin_chars = ''.join(str2ascii(c)[::-1] for c in chars)
    return sum(int(bit) * weight for bit, weight in zip(bin_chars, GK))
def decrypt_N_char(number):
    d = (number * mmi) % n
    res = ""
    for sik_i in SIK[::-1]:
        if d >= sik_i:
            res = "1" + res
            d -= sik_i
        else:
            res = "0" + res
    res = res.zfill(8 * char_per_block)
    char1 = chr(bit2Str(res[:8]))
    char2 = chr(bit2Str(res[8:]))
    return char1 + char2
def bit2Str(bitstring):
    return int(bitstring, 2)
def encrypt_mh(message):
    if len(message) % char_per_block != 0:
        message += " " * (char_per_block - len(message) % char_per_block)
    encrypted = [encrypt_N_char(message[i:i + char_per_block]) for i in range(0, len(message), char_per_block)]
    return encrypted
def decrypt_mh(crypto_list):
    plaintext = ''.join(decrypt_N_char(num) for num in crypto_list)
    return plaintext
if __name__ == "__main__":
    encrypted_message = encrypt_mh("ciao, io mi chiamo francesco ")
    print("Encrypted:", encrypted_message)
    decrypted_message = decrypt_mh(encrypted_message)
    print("Decrypted:", decrypted_message)
    try:
        with open("encrypted", "r") as file:
            encrypted_numbers = [int(line.strip(), 16) for line in file]
            decrypted_text = decrypt_mh(encrypted_numbers)
            print("Decrypted from file:", decrypted_text)
    except FileNotFoundError:
        print("The file 'encrypted' was not found.")