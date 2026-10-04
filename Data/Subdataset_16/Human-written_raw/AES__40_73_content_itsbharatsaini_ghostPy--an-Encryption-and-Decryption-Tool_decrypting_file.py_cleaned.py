import base64
import getpass
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b9.pbkdf2 import PBKDF2HMAC
from cryptography.b3 import Fernet
def fonk1():
    print("\nWelcome to gostpy Decryption Tool...!!\n")
    def fonk2():
        b1 = b15
        with open(b1, 'rb') as f:
            b2 = f.read()
        b3 = Fernet(b14)
        b4 = b3.decrypt(b2)
        with open(b1, 'wb') as f:
            f.write(b4)
        print("File '" + b1 + "' is Decrypted.")
    def fonk3():
        for root, dirs, files in os.walk(b15):
            b5 = root
            for b16 in files:
                b1 = b5 + '\\' + b16
                with open(b1, 'rb') as f:
                    b2 = f.read()
                b3 = Fernet(b14)
                try:
                    b4 = b3.decrypt(b2)
                    with open(b1, 'wb') as f:
                        f.write(b4)
                    print("File '" + b1 + "' is Decrypted.")
                except:
                    print("File '" + b1 + "' is Not Decrypted.")
    b6 = input("Enter Your Encrypted File Password : ")
    if len(b6) < 1:
        print("Please Provide Password")
    else:
        b7 = b6.encode()
        b8 = b'ghostpy'
        b9 = PBKDF2HMAC(
            b10 = hashes.SHA256(),
            b11 = 32,
            b8 = b8,
            b12 = 100000,
            b13 = default_backend()
        )
        b14 = base64.urlsafe_b64encode(b9.derive(b7))
        b15 = input("Drag and Drop your file or folder here : ")
        print("Files are Decrypting ... ")
        b16 = os.path.isfile(b15)
        if b16 = = True:
            fonk2()
        else:
            fonk3()