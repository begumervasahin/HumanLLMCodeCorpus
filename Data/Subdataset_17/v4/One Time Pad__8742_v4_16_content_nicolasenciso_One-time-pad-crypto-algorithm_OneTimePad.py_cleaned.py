
LETTERS_TO_NUMBERS = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
NUMBERS_TO_LETTERS = {v: k for k, v in LETTERS_TO_NUMBERS.items()}
def cipher(key, message):
    ciphertext = []
    if len(key) == len(message):
        for k_char, m_char in zip(key, message):
            cipher_key = LETTERS_TO_NUMBERS[k_char]
            cipher_msg = LETTERS_TO_NUMBERS[m_char]
            cipher_text = (cipher_key + cipher_msg) % 26
            ciphertext.append(NUMBERS_TO_LETTERS[cipher_text])
    return ciphertext
def num_cipher(key, message):
    cipher_numbers = []
    if len(key) == len(message):
        for k_char, m_char in zip(key, message):
            cipher_number = (int(k_char) - int(m_char)) % 10
            cipher_numbers.append(cipher_number)
    return cipher_numbers
print("Encrypted message:", cipher("EVXLL", "MONTH"))
print("Encrypted numbers:", num_cipher("6", "6"))