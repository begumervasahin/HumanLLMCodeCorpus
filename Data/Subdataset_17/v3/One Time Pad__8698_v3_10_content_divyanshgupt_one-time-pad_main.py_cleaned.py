import sys
from takeinput import takeinput
import crypt
def main() -> None:
    inp = sys.argv
    order, directory, key_directory = takeinput(inp)
    try:
        if order == "encrypt":
            crypt.encrypt(directory, key_directory)
            print("Encrypted successfully.")
        elif order == "decrypt":
            crypt.decrypt(directory, key_directory)
            print("Decrypted successfully.")
        else:
            print("Error: Unrecognized command. Please use 'encrypt' or 'decrypt'.")
    except Exception as e:
        print(f"Error during {order}: {e}")
if __name__ == "__main__":
    main()