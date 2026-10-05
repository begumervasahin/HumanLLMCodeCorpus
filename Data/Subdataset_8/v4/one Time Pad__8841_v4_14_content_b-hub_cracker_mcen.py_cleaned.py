import sys
alphabet = [chr(n) for n in range(32, 127) if chr(n) not in ['$']]
def shift_char(cipher_char, key_char):
    return alphabet[(alphabet.index(cipher_char) - alphabet.index(key_char)) % len(alphabet)]
def key_char_for(cipher_char, plaintext_char):
    return shift_char(cipher_char, plaintext_char)
def decrypt(key, ciphertext):
    plaintext = ""
    for i in range(len(key)):
        plaintext += shift_char(ciphertext[i], key[i])
    return plaintext
mode = sys.argv[1]
if mode == "d":
    print("Decryption Mode, to exit press: ctrl + c")
    ciphertext = input("Enter the ciphertext: ")
    key = input("Now enter the key: ")
    print("Plaintext: " + decrypt(key, ciphertext))
elif mode == "e":
    print("Encryption Mode, to exit press: ctrl + c")
    plaintext = input("Enter the plaintext: ")
    ciphertext = input("Now enter the ciphertext: ")
    if len(plaintext) <= len(ciphertext):
        key = "".join([key_char_for(ciphertext[i], plaintext[i]) for i in range(len(plaintext))])
        print("KEY: " + key)
    else:
        print("The length of ciphertext must be >= plaintext to encrypt all of it")
else:
    print("Please enter either 'e' for encryption or 'd' for decryption.")
    sys.exit(-1)
import sys
alphabet = [chr(n) for n in range(32, 127) if chr(n) not in ['$']]
def shift_char(cipher_char, key_char):
    return alphabet[(alphabet.index(cipher_char) - alphabet.index(key_char)) % len(alphabet)]
def key_char_for(cipher_char, plaintext_char):
    return shift_char(cipher_char, plaintext_char)
def decrypt(key, ciphertext):
    plaintext = ""
    for i in range(len(key)):
        plaintext += shift_char(ciphertext[i], key[i])
    return plaintext
mode = sys.argv[1]
if mode == "d":
    print("Decryption Mode, to exit press: ctrl + c")
    ciphertext = input("Enter the ciphertext: ")
    key = input("Now enter the key: ")
    print("Plaintext: " + decrypt(key, ciphertext))
elif mode == "e":
    print("Encryption Mode, to exit press: ctrl + c")
    plaintext = input("Enter the plaintext: ")
    ciphertext = input("Now enter the ciphertext: ")
    if len(plaintext) <= len(ciphertext):
        key = "".join([key_char_for(ciphertext[i], plaintext[i]) for i in range(len(plaintext))])
        print("KEY: " + key)
    else:
        print("The length of ciphertext must be >= plaintext to encrypt all of it")
else:
    print("Please enter either 'e' for encryption or 'd' for decryption.")
    sys.exit(-1)