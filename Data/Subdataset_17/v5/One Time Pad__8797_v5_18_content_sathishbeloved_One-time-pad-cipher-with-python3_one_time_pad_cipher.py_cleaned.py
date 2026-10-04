def encrypt():
    data = input("Enter the character: ")
    key = input("Enter the key: ")
    if len(data) != 1 or len(key) != 1:
        print("Error: Both inputs should be single characters.")
        return
    cipher_value = ord(data) + ord(key)
    cipher = chr(cipher_value)
    print(f"Cipher text: {cipher}")
def decrypt():
    cipher = input("Enter the cipher text: ")
    key = input("Enter the key: ")
    if len(cipher) != 1 or len(key) != 1:
        print("Error: Both inputs should be single characters.")
        return
    msg_value = ord(cipher) - ord(key)
    msg = chr(msg_value)
    print(f"The message is: {msg}")
def main():
    while True:
        print("\nOptions:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("0. Exit")
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()