import random
from typing import Tuple
from modules import algorithms
ALPHABET = [None] + list('abcdefghijklmnopqrstuvwxyz')
def encrypt(plaintext: str) -> Tuple[str, str]:
    pad = [random.choice(ALPHABET[1:]) for _ in range(len(plaintext))]
    plaintext_num = algorithms.alph_pos(plaintext)
    pad_num = algorithms.alph_pos(pad)
    ciphertext_num = [(plaintext_num[i] + pad_num[i]) % 26 for i in range(len(plaintext_num))]
    ciphertext = ''.join(ALPHABET[num] for num in ciphertext_num)
    pad_str = ''.join(pad)
    return pad_str, ciphertext
def validate_plaintext(plaintext: str) -> bool:
    return all(char in ALPHABET[1:] for char in plaintext)
def main():
    plaintext = input("Enter plaintext data: ").lower()
    if not validate_plaintext(plaintext):
        print("Error: Plaintext contains invalid characters. Only alphabetic characters are allowed.")
    else:
        pad, ciphertext = encrypt(plaintext)
        print(f"Your ciphertext encrypted with the pad: {pad} is: {ciphertext}")
if __name__ == "__main__":
    main()