def make_vernam_cipher(text, key):
    cipher_text = []
    key_length = len(key)
    for i, char in enumerate(text):
        cipher_char = chr(ord(char) ^ ord(key[i % key_length]))
        cipher_text.append(cipher_char)
    return ''.join(cipher_text)
def main():
    MY_KEY = "cvwopslweinedvq9fnasdlkfn2"
    while True:
        print("\n\n--- Vernam Cipher ---")
        plain_text = input("Enter text to encrypt: ")
        cipher_text = make_vernam_cipher(plain_text, MY_KEY)
        print("Cipher text:", cipher_text)
        decrypted_text = make_vernam_cipher(cipher_text, MY_KEY)
        print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()