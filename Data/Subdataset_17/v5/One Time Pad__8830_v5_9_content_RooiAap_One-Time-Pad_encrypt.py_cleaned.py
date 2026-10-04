import random
from modules import algorithms
def generate_pad(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return [random.choice(alphabet) for _ in range(length)]
def encrypt(plaintext, pad):
    plaintext_positions = algorithms.alph_pos(list(plaintext))
    pad_positions = algorithms.alph_pos(pad)
    ciphertext_positions = [
        (plaintext_positions[i] + pad_positions[i]) % 26
        for i in range(len(plaintext_positions))
    ]
    ciphertext = algorithms.num_alph(ciphertext_positions)
    return "".join(ciphertext)
def main():
    plaintext = input("Enter plaintext data: ")
    pad = generate_pad(len(plaintext))
    ciphertext = encrypt(plaintext, pad)
    print(f"Your ciphertext encrypted with the pad: {''.join(pad)} is: {ciphertext}")
if __name__ == "__main__":
    main()