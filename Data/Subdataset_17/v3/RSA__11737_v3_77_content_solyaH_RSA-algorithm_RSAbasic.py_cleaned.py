import math
alphabet = "abcdefghijklmnopqrstuvwxyz"
def euclid_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    x2, x1 = 1, 0
    y2, y1 = 0, 1
    while b > 0:
        q = a
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a, b = b, r
        x2, x1 = x1, x
        y2, y1 = y1, y
    return a, x2, y2
def int_to_bit(number, length):
    return format(number, '0{}b'.format(length))
def rsa_encrypt(text, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    _, _, v = euclid_algorithm(phi, e)
    bit_length = int(math.log2(len(alphabet))) + 1
    max_bit_length = int(math.log2(n - 1))
    bit_string = ''.join(int_to_bit(alphabet.index(char) + 1, bit_length) for char in text)
    encrypted_message = [
        (int(bit_string[i * max_bit_length: (i + 1) * max_bit_length], 2) ** e) % n
        for i in range((len(bit_string) + max_bit_length - 1)
    ]
    return encrypted_message
def rsa_decrypt(ciphertext, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    _, _, v = euclid_algorithm(phi, e)
    d = v % phi
    max_bit_length = int(math.log2(n - 1))
    bit_length = int(math.log2(len(alphabet))) + 1
    decrypted_numbers = [(code ** d) % n for code in ciphertext]
    bit_string = ''.join(
        int_to_bit(num, max_bit_length) if i < len(decrypted_numbers) - 1
        else int_to_bit(num, len(decrypted_numbers) * bit_length - len(bit_string))
        for i, num in enumerate(decrypted_numbers)
    )
    decrypted_text = ''.join(
        alphabet[int(bit_string[i * bit_length: (i + 1) * bit_length], 2) - 1]
        for i in range(len(bit_string)
    )
    return decrypted_text
def main():
    text = 'wonderfull'
    action = 'e'
    p, q, e = 17, 31, 7
    if action == 'e':
        result = rsa_encrypt(text, p, q, e)
    elif action == 'd':
        ciphertext = rsa_encrypt(text, p, q, e)
        result = rsa_decrypt(ciphertext, p, q, e)
    print(result)
if __name__ == "__main__":
    main()