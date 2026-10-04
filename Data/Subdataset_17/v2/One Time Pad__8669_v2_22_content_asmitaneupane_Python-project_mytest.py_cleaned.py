def make_vernam_cipher(text, key):
    cipher_text = ""
    key_index = 0
    for char in text:
        cipher_text += chr(ord(char) ^ ord(key[key_index]))
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return cipher_text
MY_KEY = "cvwopslweinedvq9fnasdlkfn2"
def main():
    while True:
        print("\n\n--- Vernam Cipher ---")
        plaintext = input("Enter text to encrypt: ")
        cipher = make_vernam_cipher(plaintext, MY_KEY)
        print("Cipher text:", cipher)
        decrypted_text = make_vernam_cipher(cipher, MY_KEY)
        print("Decrypted text:", decrypted_text)
if __name__ == "__main__":
    main()