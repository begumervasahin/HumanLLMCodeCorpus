import sys
from takeinput import takeinput
import crypt
def handle_encryption(directory, key_directory):
    try:
        crypt.encrypt(directory, key_directory)
        print("Encrypted")
    except Exception as e:
        print(f"Error during encryption: {e}")
def handle_decryption(directory, key_directory):
    try:
        crypt.decrypt(directory, key_directory)
        print("Decrypted")
    except Exception as e:
        print(f"Error during decryption: {e}")
def main():
    inp = sys.argv
    order, directory, key_directory = takeinput(inp)
    if order == "encrypt":
        handle_encryption(directory, key_directory)
    elif order == "decrypt":
        handle_decryption(directory, key_directory)
    else:
        print("Error: can't understand input")
if __name__ == "__main__":
    main()