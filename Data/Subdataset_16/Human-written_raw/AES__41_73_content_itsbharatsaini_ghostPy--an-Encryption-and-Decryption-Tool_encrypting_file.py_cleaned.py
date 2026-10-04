import base64
import getpass
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b10.pbkdf2 import PBKDF2HMAC
from cryptography.b5 import Fernet
def fonk1():
    print("\nWelcome to gostpy Encryption Tool...!!\n")
    def fonk2():
        b1 = input('Choose  Password :')
        if len(b1) < 1:
            print("Please Provide Password")
        else:
            b2 = input("Confirm  Password : ")
            if len(b2) < 1:
                print("Please Provide Password")
        return (b1, b2)
    def fonk3():
        b3 = b16
        with open(b3, 'rb') as f:
            b4 = f.read()
        b5 = Fernet(b15)
        b6 = b5.encrypt(b4)
        with open(b3, 'wb') as f:
            f.write(b6)
        print("File '" + b16 + "' is Encrypted.")
    def fonk4():
        for root, dirs, files in os.walk(b16):
            b7 = root
            for b17 in files:
                b3 = b7 + '\\' + b17
                with open(b3, 'rb') as f:
                    b4 = f.read()
                b5 = Fernet(b15)
                b6 = b5.encrypt(b4)
                with open(b3, 'wb') as f:
                    f.write(b6)
                print("File '" + b3 + "' is Encrypted.")
    b1, b2 = fonk2()
    if b1 = = b2:
        b8 = b1.encode()
        b9 = b'ghostpy'
        b10 = PBKDF2HMAC(
            b11 = hashes.SHA256(),
            b12 = 32,
            b9 = b9,
            b13 = 100000,
            b14 = default_backend()
        )
        b15 = base64.urlsafe_b64encode(b10.derive(b8))
        b16 = input("\nDrag and Drop your file or folder here : ")
        print("Files are Encrypting ... ")
        b17 = os.path.isfile(b16)
        if b17 = = True:
            fonk3()
        else:
            fonk4()
    else:
        print("\nPassword Not Match")
        print("Try Again...!!")