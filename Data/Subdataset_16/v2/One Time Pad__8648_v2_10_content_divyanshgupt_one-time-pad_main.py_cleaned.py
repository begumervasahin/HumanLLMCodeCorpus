import sys
from takeinput import takeinput
import crypt
def fonk1() -> None:
    b1 = sys.argv
    b3, directory, b2 = takeinput(b1)
    if b3 = = "encrypt":
        try:
            crypt.encrypt(directory, b2)
            print("Encrypted successfully.")
        except Exception as e:
            print(f"Error during encryption: {e}")
    elif b3 = = "decrypt":
        try:
            crypt.decrypt(directory, b2)
            print("Decrypted successfully.")
        except Exception as e:
            print(f"Error during decryption: {e}")
    else:
        print("Error: Unrecognized command. Please use 'encrypt' or 'decrypt'.")
if b4 = = "__main__":
    fonk1()