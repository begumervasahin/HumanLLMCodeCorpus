import sys
ALPHABET = [chr(n) for n in range(32, 127) if chr(n) != '$']
def shift_char(char1, char2):
    return ALPHABET[(ALPHABET.index(char1) - ALPHABET.index(char2)) % len(ALPHABET)]
def key_char_for(cipher_char, plain_char):
    return shift_char(cipher_char, plain_char)
def decrypt(key, cipher_text):
    plain_text = ""
    for i in range(len(key)):
        plain_text += shift_char(cipher_text[i], key[i])
    return plain_text
def main():
    mode = sys.argv[1].lower()
    if mode == "d":
        print("Decryption Mode, press ctrl + c to exit.")
        cipher_text = input("Enter the ciphertext: ")
        key = input("Enter the key: ")
        print("Plaintext:", decrypt(key, cipher_text))
    elif mode == "e":
        print("Encryption Mode, press ctrl + c to exit.")
        plain_text = input("Enter the plaintext: ")
        cipher_text = input("Enter the ciphertext: ")
        if len(plain_text) <= len(cipher_text):
            key = "".join(key_char_for(cipher_text[i], plain_text[i]) for i in range(len(plain_text)))
            print("Generated Key:")
            print(f"START_KEY_END\n{key}\nSTART_KEY_END")
        else:
            print("The length of the ciphertext must be greater than or equal to the plaintext.")
    else:
        print("Please enter either 'e' for encryption or 'd' for decryption.")
if __name__ == "__main__":
    main()