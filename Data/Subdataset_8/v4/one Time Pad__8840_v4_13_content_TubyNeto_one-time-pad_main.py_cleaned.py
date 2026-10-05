import string
import random
def encode_letter(plain_text_letter, key_letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num_plain_text = alphabet.index(plain_text_letter) + 1
    num_key = alphabet.index(key_letter) + 1
    num_cipher_text = (num_plain_text + num_key) % 26
    cipher_text_letter = alphabet[num_cipher_text]
    return cipher_text_letter
def decode_letter(cipher_text_letter, key_letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    num_cipher_text = alphabet.index(cipher_text_letter) + 1
    num_key = alphabet.index(key_letter) + 1
    num_plain_text = num_cipher_text - num_key
    plain_text_letter = alphabet[num_plain_text]
    return plain_text_letter
def decrypt(cipher_text, key):
    plain_text = ''
    for i in range(len(cipher_text)):
        plain_text += decode_letter(cipher_text[i], key[i])
    return plain_text
def encrypt(plain_text, key):
    cipher_text = ''
    for i in range(len(plain_text)):
        cipher_text += encode_letter(plain_text[i], key[i])
    return cipher_text
def generate_key(key_length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(key_length))
while True:
    print("Menu:")
    print("1 - Encrypt")
    print("2 - Decrypt")
    print("3 - Quit")
    selected = input()
    if selected == '1':
        print("Type the Plain Text:")
        plain_text = input()
        key = generate_key(len(plain_text))
        print('Cipher Text:', encrypt(plain_text, key))
    elif selected == '2':
        print("Type the Cipher Text:")
        cipher_text = input()
        key = generate_key(len(cipher_text))
        print('Plain Text:', decrypt(cipher_text, key))
    elif selected == '3':
        break
    else:
        print("Only 1/2/3 options available")