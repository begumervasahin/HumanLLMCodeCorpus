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
def int_to_bit(letter_numb, bit_length):
    return '{0:0b}'.format(letter_numb).zfill(bit_length)
def rsa(text, p, q, e, action):
    n = p * q
    phi = (p - 1) * (q - 1)
    _, _, v = euclid_algorithm(phi, e)
    bit_length = int(math.log(len(alphabet), 2)) + 1
    max_bit_interval_length = int(math.log(n - 1, 2))
    if action == 'e':
        bit_str = ''.join(int_to_bit(alphabet.find(letter) + 1, bit_length) for letter in text)
        cipher_text = [
            (int(bit_str[i * max_bit_interval_length: (i + 1) * max_bit_interval_length], 2) ** e) % n
            for i in range((len(bit_str) + max_bit_interval_length - 1)
        ]
        return cipher_text
    elif action == 'd':
        d = v % phi
        decoded_numbers = [(code ** d) % n for code in text]
        bit_str = ''.join(
            int_to_bit(num, max_bit_interval_length) if i < len(decoded_numbers) - 1
            else int_to_bit(num, len(decoded_numbers) * bit_length - len(bit_str))
            for i, num in enumerate(decoded_numbers)
        )
        decoded_text = ''.join(
            alphabet[int(bit_str[i * bit_length: (i + 1) * bit_length], 2) - 1]
            for i in range(len(bit_str)
        )
        return decoded_text
def main():
    text = 'wonderfull'
    action = 'e'
    p, q, e = 17, 31, 7
    result = rsa(text, p, q, e, action)
    print(result)
if __name__ == "__main__":
    main()