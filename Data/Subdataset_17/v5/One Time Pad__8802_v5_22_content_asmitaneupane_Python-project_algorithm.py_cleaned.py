def vernam_cipher(key, text):
    cipher_text = [
        chr(ord(char) ^ ord(key[i % len(key)]))
        for i, char in enumerate(text)
    ]
    return ''.join(cipher_text)
def main():
    key = "mysecretkey"
    text = "Hello, World!"
    cipher_text = vernam_cipher(key, text)
    print("Cipher Text:", cipher_text)
    decrypted_text = vernam_cipher(key, cipher_text)
    print("Decrypted Text:", decrypted_text)
if __name__ == "__main__":
    main()