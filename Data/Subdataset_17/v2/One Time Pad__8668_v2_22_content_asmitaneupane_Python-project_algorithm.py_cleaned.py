def vernam_cipher(key: str, text: str) -> str:
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        result.append(chr(ord(char) ^ ord(key[i % key_length])))
    return ''.join(result)
def main() -> None:
    key = "SECRET"
    text = "HELLO WORLD"
    encrypted_text = vernam_cipher(key, text)
    print("Encrypted:", encrypted_text)
    decrypted_text = vernam_cipher(key, encrypted_text)
    print("Decrypted:", decrypted_text)
if __name__ == "__main__":
    main()