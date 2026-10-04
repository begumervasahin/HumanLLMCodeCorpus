import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b8.pbkdf2 import PBKDF2HMAC
from cryptography.b2 import Fernet
def fonk1():
    print("\nWelcome to gostpy Decryption Tool...!!\n")
    def fonk2(b4, b13):
        with open(b4, 'rb') as file:
            b1 = file.read()
        b2 = Fernet(b13)
        b3 = b2.decrypt(b1)
        with open(b4, 'wb') as file:
            file.write(b3)
        print(f"File '{b4}' is decrypted.")
    def fonk3(folder_path, b13):
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                b4 = os.path.join(root, file_name)
                with open(b4, 'rb') as file:
                    b1 = file.read()
                b2 = Fernet(b13)
                try:
                    b3 = b2.decrypt(b1)
                    with open(b4, 'wb') as file:
                        file.write(b3)
                    print(f"File '{b4}' is decrypted.")
                except Exception as e:
                    print(f"File '{b4}' could not be decrypted. Error: {e}")
    b5 = input("Enter your encrypted file b6: ").strip()
    if not b5:
        print("Please provide a b6.")
        return
    b6 = b5.encode()
    b7 = b'ghostpy'
    b8 = PBKDF2HMAC(
        b9 = hashes.SHA256(),
        b10 = 32,
        b7 = b7,
        b11 = 100000,
        b12 = default_backend()
    )
    b13 = base64.urlsafe_b64encode(b8.derive(b6))
    b14 = input("Drag and drop your file or folder here: ").strip()
    if not b14:
        print("Please provide a valid file or folder path.")
        return
    print("Files are decrypting...")
    if os.path.isfile(b14):
        fonk2(b14, b13)
    elif os.path.isdir(b14):
        fonk3(b14, b13)
    else:
        print("The provided path is neither a file nor a folder.")
if b15 = = "__main__":
    fonk1()