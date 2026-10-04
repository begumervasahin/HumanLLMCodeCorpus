LETTERS_TO_NUMBERS = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
    'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
    'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}
NUMBERS_TO_LETTERS = {v: k for k, v in LETTERS_TO_NUMBERS.items()}
def cipher(key, msg):
    if len(key) != len(msg):
        raise ValueError("Key and message must be of the same length.")
    return [
        NUMBERS_TO_LETTERS[(LETTERS_TO_NUMBERS[key[i]] + LETTERS_TO_NUMBERS[msg[i]]) % 26]
        for i in range(len(key))
    ]
def num_cipher(key, msg):
    if len(key) != len(msg):
        raise ValueError("Key and message must be of the same length.")
    return [
        (int(key[i]) + int(msg[i])) % 10
        for i in range(len(key))
    ]
if __name__ == "__main__":
    encrypted_message = cipher("EVXLL", "MONTH")
    print("Encrypted message:", "".join(encrypted_message))
    encrypted_numeric = num_cipher("6", "6")
    print("Encrypted numeric message:", encrypted_numeric)
