import string
import random
def encode_letter(plain_letter, key_letter):
    alphabet = string.ascii_lowercase
    plain_num = alphabet.index(plain_letter.lower()) + 1
    key_num = alphabet.index(key_letter.lower()) + 1
    cipher_num = (plain_num + key_num) % 26
    cipher_letter = alphabet[cipher_num - 1]
    return cipher_letter
def decode_letter(cipher_letter, key_letter):
    alphabet = string.ascii_lowercase
    cipher_num = alphabet.index(cipher_letter.lower()) + 1
    key_num = alphabet.index(key_letter.lower()) + 1
    plain_num = cipher_num - key_num
    plain_letter = alphabet[plain_num - 1]
    return plain_letter
def decrypt(cipher_text, key):
    plain_text = ''.join(decode_letter(c, k) for c, k in zip(cipher_text, key))
    return plain_text
def encrypt(plain_text, key):
    cipher_text = ''.join(encode_letter(p, k) for p, k in zip(plain_text, key))
    return cipher_text
def generate_key(key_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(key_length))
def main():
    while True:
        print("Menu:")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Quit")
        selected = input()
        if selected == '1':
            plain_text = input("Enter the Plain Text: ")
            key = generate_key(len(plain_text))
            print('Cipher Text:', encrypt(plain_text, key))
        elif selected == '2':
            cipher_text = input("Enter the Cipher Text: ")
            key = generate_key(len(cipher_text))
            print('Plain Text:', decrypt(cipher_text, key))
        elif selected == '3':
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
if __name__ == "__main__":
    main()