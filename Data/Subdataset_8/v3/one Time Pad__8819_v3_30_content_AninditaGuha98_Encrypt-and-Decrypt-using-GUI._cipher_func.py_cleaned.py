import string
def caesar_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') + int(key)) % 26
            encrypted_char = chr((shift + ord('a')))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text
def caesar_decrypt(ciphertext, key):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char.lower()) - ord('a') - int(key)) % 26
            decrypted_char = chr((shift + ord('a')))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text
def vigenere_encrypt(plaintext, key):
    key_length = len(key)
    encrypted_text = ''
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = (ord(key[i % key_length].lower()) - ord('a'))
            encrypted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text
def vigenere_decrypt(ciphertext, key):
    key_length = len(key)
    decrypted_text = ''
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = (ord(key[i % key_length].lower()) - ord('a'))
            decrypted_char = chr(((ord(char.lower()) - ord('a') - shift) % 26) + ord('a'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text
def main():
    print("Choose an option:")
    print("1. Caesar Cipher Encryption")
    print("2. Caesar Cipher Decryption")
    print("3. Vigenere Cipher Encryption")
    print("4. Vigenere Cipher Decryption")
    print("5. Exit")
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