import sys
alphabet = [chr(n) for n in range(32, 127) if chr(n) not in ['$']]
def shift_char(c1, c2):
    return alphabet[(alphabet.index(c1) - alphabet.index(c2)) % len(alphabet)]
def key_char_for(c_cipher, p_plain):
    return shift_char(c_cipher, p_plain)
def decrypt(key, cipher):
    plaintext = ""
    for i in range(len(key)):
        plaintext += shift_char(cipher[i], key[i])
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
        key = "".join(key_char_for(ciphertext[i], plaintext[i]) for i in range(len(plaintext)))
        print("KEY, make sure you copy everything between the start and the end:")
        print(f"START_KEY_END\n{key}\nSTART_KEY_END")
    else:
        print("The length of ciphertext must be >= to plaintext to encrypt all of it")
else:
    print("Please enter either the character 'e' or 'd' for either encryption or decryption")
    exit(-1)