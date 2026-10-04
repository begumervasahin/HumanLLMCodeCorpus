def encrypt():
    data = input("Enter the character: ")
    key = input("Enter the key: ")
    if len(data) != 1 or len(key) != 1:
        print("Error: Please enter a single character for both data and key.")
        return
    cipher_value = ord(data) + ord(key)
    cipher_char = chr(cipher_value)
    print(f"Encrypted character: {cipher_char}")
def decrypt():
    cipher = input("Enter the cipher text: ")
    key = input("Enter the key: ")
    if len(cipher) != 1 or len(key) != 1:
        print("Error: Please enter a single character for both cipher and key.")
        return
    original_value = ord(cipher) - ord(key)
    original_char = chr(original_value)
    print(f"The decrypted character is: {original_char}")
def main():
    while True:
        print("\nOptions:")
        print("1: Encrypt")
        print("2: Decrypt")
        print("0: Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            encrypt()
        elif choice == '2':
            decrypt()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")
if __name__ == '__main__':
    main()