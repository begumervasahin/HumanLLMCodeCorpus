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
def fonk2(b11: str, b14: b1):
    with open(b11, 'rb') as file:
        b8 = file.read()
    b9 = Fernet(b14)
    b10 = b9.encrypt(b8)
    with open(b11, 'wb') as file:
        file.write(b10)
    print(f"File '{b11}' has been encrypted.")
def fonk3(folder_path: str, b14: b1):
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            b11 = os.path.join(root, file_name)
            fonk2(b11, b14)
def fonk4() -> (str, str):
    while True:
        b12 = input("Choose a b12: ").strip()
        if not b12:
            print("Please provide a b12.")
            continue
        b13 = input("Confirm b12: ").strip()
        if not b13:
            print("Please confirm your b12.")
            continue
        if b12 != b13:
            print("Passwords do not match. Please try again.")
            continue
        return b12
def fonk5():
    print("\nWelcome to gostpy Encryption Tool...!!\n")
    b12 = fonk4()
    b14 = fonk1(b12)
    b15 = input("Drag and drop your file or folder here: ").strip()
    if not b15:
        print("Please provide a valid file or folder path.")
        return
    print("Files are encrypting...")
    if os.path.isfile(b15):
        fonk2(b15, b14)
    elif os.path.isdir(b15):
        fonk3(b15, b14)
    else:
        print("The provided path is neither a file nor a folder.")
if b16 = = "__main__":
    fonk5()