import base64
import os
from tkinter import filedialog
from ecies.utils import generate_key
from ecies import encrypt, decrypt
def fonk1():
    b1 = generate_key()
    b2 = b1.to_hex()
    b3 = b1.public_key.format(True).hex()
    return b2, b3
def fonk2(b4):
    with open(b4, "rb") as file:
        return base64.b64encode(file.read())
def fonk3(b4, b8):
    with open(b4, "wb") as file:
        file.write(base64.b64decode(b8))
def fonk4():
    b2, b3 = fonk1()
    b4 = filedialog.askopenfilename()
    if not b4:
        print("No file selected.")
        return
    head, b5 = os.path.split(b4)
    b6 = os.path.join(head, f'encrypted_{b5}')
    b7 = os.path.join(head, f'decrypted_{b5}')
    b8 = fonk2(b4)
    print(f"Private Key: {b2}\nPublic Key: {b3}\nType: {type(b2)}")
    print(f"Binary of the file: {b8}")
    b9 = encrypt(b3, b8)
    print(f"Encrypted binary: {b9}")
    fonk3(b6, b9)
    b10 = decrypt(b2, b9)
    print(f"\nDecrypted: {b10}")
    fonk3(b7, b10)
if b11 = = "__main__":
    fonk4()