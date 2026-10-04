import random
from modules import algorithms
alph = [None, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(plaintext: str) -> Tuple[str, str]:
    pad = [random.choice(alph[1:]) for _ in range(len(plaintext))]
    plaintext_num = algorithms.alph_pos(plaintext)
    pad_num = algorithms.alph_pos(pad)
    ciphertext_num = [(plaintext_num[p] + pad_num[p]) % 26 for p in range(len(plaintext_num))]
    ciphertext = ''.join(alph[num] for num in ciphertext_num)
    pad_str = ''.join(pad)
    return pad_str, ciphertext
if __name__ == "__main__":
    plaintext = input("Enter plaintext data: ").lower()
    if not all(char in alph[1:] for char in plaintext):
        print("Error: Plaintext contains invalid characters. Only alphabetic characters are allowed.")
    else:
        pad, ciphertext = encrypt(plaintext)
        print(f"Your ciphertext encrypted with the pad: {pad} is: {ciphertext}")