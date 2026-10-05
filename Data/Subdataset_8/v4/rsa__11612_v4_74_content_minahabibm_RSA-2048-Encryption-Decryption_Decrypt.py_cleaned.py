def decrypt_message(encrypted_message, private_key, modulo):
    return (encrypted_message ** private_key) % modulo
def decrypt_message_from_file(filename, private_key, modulo):
    decrypted_message = ""
    with open(filename, "r") as f:
        encrypted_lines = [line.rstrip('\n') for line in f]
    for line in encrypted_lines:
        decrypted_char_code = decrypt_message(int(line), int(private_key), int(modulo))
        decrypted_message += chr(decrypted_char_code)
    return decrypted_message
def decrypt_file(filename, private_key, modulo):
    decrypted_bytes = []
    with open(filename, "r") as f:
        encrypted_lines = f.readlines()
    for line in encrypted_lines:
        encrypted_value = int(line.strip())
        decrypted_value = decrypt_message(encrypted_value, int(private_key), int(modulo))
        decrypted_bytes.append(decrypted_value)
    with open("Decrypted_File", "wb") as fw:
        for value in decrypted_bytes:
            fw.write(bytes([value]))
def main():
    choice = input("Enter 1 to decrypt a message from a file, or 2 to decrypt a file: ")
    modulo = input("Enter Modulo (public key): ")
    private_key = input("Enter Private Key: ")
    if choice == '1':
        decrypted_message = decrypt_message_from_file("Encrypted_Message.txt", private_key, modulo)
        print("Decrypted Message:", decrypted_message)
        with open("Decrypted_Message.txt", "w") as fw:
            fw.write(decrypted_message)
    elif choice == '2':
        decrypt_file("Encrypted_File.txt", private_key, modulo)
        print("File decrypted and saved as 'Decrypted_File'.")
if __name__ == "__main__":
    main()