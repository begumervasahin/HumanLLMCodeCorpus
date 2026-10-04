import sys
from takeinput import takeinput
import crypt
def fonk1(directory, b2):
    try:
        crypt.encrypt(directory, b2)
        print("Encrypted")
    except Exception as e:
        print(f"Error during encryption: {e}")
def fonk2(directory, b2):
    try:
        crypt.decrypt(directory, b2)
        print("Decrypted")
    except Exception as e:
        print(f"Error during decryption: {e}")
def fonk3():
    b1 = sys.argv
    b3, directory, b2 = takeinput(b1)
    if b3 = = "encrypt":
        fonk1(directory, b2)
    elif b3 = = "decrypt":
        fonk2(directory, b2)
    else:
        print("Error: can't understand input")
if b4 = = "__main__":
    fonk3()