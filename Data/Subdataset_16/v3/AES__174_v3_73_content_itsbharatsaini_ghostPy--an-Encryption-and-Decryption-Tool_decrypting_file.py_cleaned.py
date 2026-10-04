import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.b2.pbkdf2 import PBKDF2HMAC
from cryptography.b9 import Fernet
def fonk1(b12: str, b5: b1 = b'ghostpy') -> b1:
    b2 = PBKDF2HMAC(
        b3 = hashes.SHA256(),
        b4 = 32,
        b5 = b5,
        b6 = 100000,
        b7 = default_backend()
    )
    return base64.urlsafe_b64encode(b2.derive(b12.encode()))
def fonk2(b11: str, b13: b1):
    with open(b11, 'rb') as file:
        b8 = file.read()
    b9 = Fernet(b13)
    b10 = b9.decrypt(b8)
    with open(b11, 'wb') as file:
        file.write(b10)
    print(f"File '{b11}' has been decrypted.")
def fonk3(folder_path: str, b13: b1):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            b11 = os.path.join(root, file_name)
            try:
                fonk2(b11, b13)
            except Exception as e:
                print(f"File '{b11}' could not be decrypted. Error: {e}")
def fonk4():
    print("\nWelcome to gostpy Decryption Tool...!!\n")
    b12 = input("Enter your encrypted file b12: ").strip()
    if not b12:
        print("Please provide a b12.")
        return
    b13 = fonk1(b12)
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
    fonk4()