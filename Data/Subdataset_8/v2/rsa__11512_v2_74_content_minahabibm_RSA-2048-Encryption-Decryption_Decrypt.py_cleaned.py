
def Decryption(encrypted_message, private_key, modulus):
    return (encrypted_message ** private_key) % modulus
def decrypt_message_from_file():
    encrypted_message_list = []
    decrypted_message_list = []
    modulus = int(input("Enter Modulo: "))
    private_key = int(input("Enter Private Key: "))
    with open("Encrypted_Message.txt", "r") as file:
        encrypted_lines = [line.rstrip('\n') for line in file]
    for line in encrypted_lines:
        encrypted_message_list.append(int(line))
    for encrypted_message in encrypted_message_list:
        decrypted_message_list.append(Decryption(encrypted_message, private_key, modulus))
    decrypted_message = "".join(chr(char_code) for char_code in decrypted_message_list)
    print("Decrypted Message:", decrypted_message)
    with open("Decrypted_Message.txt", "w") as decrypted_file:
        decrypted_file.write(decrypted_message)
def decrypt_file():
    encrypted_integer_list = []
    decrypted_integer_list = []
    modulus = int(input("Enter Modulo: "))
    private_key = int(input("Enter Private Key: "))
    with open("Encrypted_File.txt", "r") as file:
        encrypted_lines = file.readlines()
    for line in encrypted_lines:
        encrypted_integer_list.append(int(line.strip()))
    for encrypted_integer in encrypted_integer_list:
        decrypted_integer_list.append(Decryption(encrypted_integer, private_key, modulus))
    with open("Decrypted_File.txt", "wb") as decrypted_file:
        decrypted_file.write(bytes(decrypted_integer_list))
def main():
    choice = input("Enter 1 to decrypt a message from a file, or 2 to decrypt a file: ")
    if choice == '1':
        decrypt_message_from_file()
    elif choice == '2':
        decrypt_file()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
if __name__ == "__main__":
    main()