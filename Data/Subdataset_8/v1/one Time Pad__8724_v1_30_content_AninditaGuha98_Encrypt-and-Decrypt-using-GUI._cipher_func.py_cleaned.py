import string
def caesar_encrypt(plaintext, key):
    answer_e = ''
    for value in plaintext:
        value = (ord(value) + int(key))
        if value - int(key) == 32:
            value = 32
        elif value > ord('z'):
            value -= 26
        elif value < ord('a'):
            value += 26
        value = chr(value)
        answer_e += value
    return answer_e
def caesar_decrypt(ciphertext, key):
    answer_d = ''
    for value in ciphertext:
        value = (ord(value) - int(key))
        if value + int(key) == 32:
            value = 32
        elif value > ord('z'):
            value -= 26
        elif value < ord('a'):
            value += 26
        value = chr(value)
        answer_d += value
    return answer_d
def vigenere_encrypt(plaintext, key):
    keylength = len(key)
    key_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_int[i % keylength]) % 26
        ciphertext += chr(value + 65)
    return ciphertext
def vigenere_decrypt(ciphertext, key):
    keylength = len(key)
    key_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_int[i % keylength]) % 26
        plaintext += chr(value + 65)
    return plaintext
def main():
    print("Choose an option:\n1. Caesar Cipher Encryption\n2. Caesar Cipher Decryption\n3. Vigenere Cipher Encryption\n4. Vigenere Cipher Decryption\n5. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            print("Encrypted text:", caesar_encrypt(plaintext, key))
        elif choice == "2":
            ciphertext = input("Enter the ciphertext: ")
            key = input("Enter the key: ")
            print("Decrypted text:", caesar_decrypt(ciphertext, key))
        elif choice == "3":
            plaintext = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            print("Encrypted text:", vigenere_encrypt(plaintext, key))
        elif choice == "4":
            ciphertext = input("Enter the ciphertext: ")
            key = input("Enter the key: ")
            print("Decrypted text:", vigenere_decrypt(ciphertext, key))
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")
if __name__ == "__main__":
    main()