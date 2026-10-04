import math
alphabet = "abcdefghijklmnopqrstuvwxyz"
def euclid_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    x2, x1, y2, y1 = 1, 0, 0, 1
    while b > 0:
        q = a
        r = a - q * b
        x, y = x2 - q * x1, y2 - q * y1
        a, b = b, r
        x2, x1, y2, y1 = x1, x, y1, y
    return a, x2, y2
def int_to_bit(letter_num, bit_length):
    return f'{letter_num:0{bit_length}b}'
def rsa_encrypt(text, p, q, e):
    n = p * q
    bit_length = int(math.log2(len(alphabet))) + 1
    max_bit_interval_length = int(math.log2(n - 1))
    bit_str = ''.join(int_to_bit(alphabet.index(letter) + 1, bit_length) for letter in text)
    cipher_text = [
        (int(bit_str[i:i + max_bit_interval_length], 2) ** e) % n
        for i in range(0, len(bit_str), max_bit_interval_length)
    ]
    return cipher_text
def rsa_decrypt(cipher_text, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    gcd, _, v = euclid_algorithm(phi, e)
    d = v % phi
    bit_length = int(math.log2(len(alphabet))) + 1
    max_bit_interval_length = int(math.log2(n - 1))
    decoded_numbers = [(code ** d) % n for code in cipher_text]
    bit_str = ''.join(int_to_bit(num, max_bit_interval_length) for num in decoded_numbers)
    decoded_text = ''.join(
        alphabet[int(bit_str[i:i + bit_length], 2) - 1]
        for i in range(0, len(bit_str), bit_length)
    )
    return decoded_text
def main():
    text = 'wonderfull'
    action = 'e'
    p, q, e = 17, 31, 7
    if action == 'e':
        result = rsa_encrypt(text, p, q, e)
    elif action == 'd':
        result = rsa_decrypt(text, p, q, e)
    print(result)
if __name__ == "__main__":
    main()