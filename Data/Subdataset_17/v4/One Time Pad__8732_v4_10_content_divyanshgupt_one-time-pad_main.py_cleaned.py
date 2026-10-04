import sys
from takeinput import takeinput
import crypt
def main():
    inp = sys.argv
    order, directory, key_directory = takeinput(inp)
    if order == "encrypt":
        try:
            crypt.encrypt(directory, key_directory)
            print("Encrypted")
        except Exception as e:
            print(f"Error during encryption: {e}")
    elif order == "decrypt":
        try:
            crypt.decrypt(directory, key_directory)
            print("Decrypted")
        except Exception as e:
            print(f"Error during decryption: {e}")
    else:
        print("Error: can't understand input")
if __name__ == "__main__":
    main()