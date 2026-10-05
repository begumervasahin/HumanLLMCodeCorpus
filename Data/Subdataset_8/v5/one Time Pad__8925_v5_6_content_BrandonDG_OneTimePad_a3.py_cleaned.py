import os
def xor_message(message: bytes, key: bytes) -> bytes:
    return bytes(p ^ k for p, k in zip(message, key))
def get_plaintext():
    while True:
        source = input("Is the plaintext provided via stdin or file? ").strip().lower()
        if source == "file":
            filename = input("Please enter the file name: ").strip()
            try:
                with open(filename, 'r') as file:
                    return file.read().encode('utf-8')
            except FileNotFoundError:
                print("File not found. Please enter a valid filename.")
        elif source == "stdin":
            return input("Please enter the plaintext: ").encode('utf-8')
        else:
            print("Please select a valid option ('file' or 'stdin')")
def main():
    print("Welcome to the One-Time Pad encryption tool.")
    plaintext = get_plaintext()
    key = os.urandom(len(plaintext))
    print("------")
    print("Plaintext:\n%s" % plaintext.decode('utf-8'))
    print("\nKey:\n%s" % key)
    print("------")
    ciphertext = xor_message(plaintext, key)
    print("Binary Ciphertext:\n%s" % ciphertext)
    print("------")
    decrypted_text = xor_message(ciphertext, key)
    print("Verify:\n%s" % decrypted_text.decode('utf-8'))
    with open("ciphertext", "wb") as outputfile:
        outputfile.write(ciphertext)
    print("------")
    print("Character Ciphertext:\n")
    os.system("cat ciphertext")
if __name__ == "__main__":
    main()