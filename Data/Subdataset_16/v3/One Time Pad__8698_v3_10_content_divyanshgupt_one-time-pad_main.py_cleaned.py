import sys
from takeinput import takeinput
import crypt
def fonk1() -> None:
    b1 = sys.argv
    b3, directory, b2 = takeinput(b1)
    try:
        if b3 = = "encrypt":
            crypt.encrypt(directory, b2)
            print("Encrypted successfully.")
        elif b3 = = "decrypt":
            crypt.decrypt(directory, b2)
            print("Decrypted successfully.")
        else:
            print("Error: Unrecognized command. Please use 'encrypt' or 'decrypt'.")
    except Exception as e:
        print(f"Error during {b3}: {e}")
if b4 = = "__main__":
    fonk1()