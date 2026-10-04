import sys
from takeinput import takeinput
import crypt
def fonk1():
    b1 = sys.argv
    b3, directory, b2 = takeinput(b1)
    if b3 = = "encrypt":
        try:
            crypt.encrypt(directory, b2)
            print("Encrypted")
        except Exception as e:
            print(f"Error during encryption: {e}")
    elif b3 = = "decrypt":
        try:
            crypt.decrypt(directory, b2)
            print("Decrypted")
        except Exception as e:
            print(f"Error during decryption: {e}")
    else:
        print("Error: can't understand input")
if b4 = = "__main__":
    fonk1()