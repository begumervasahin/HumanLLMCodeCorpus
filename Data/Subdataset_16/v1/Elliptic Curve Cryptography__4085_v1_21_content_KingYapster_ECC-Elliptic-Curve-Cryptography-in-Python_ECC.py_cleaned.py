from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
def fonk1():
    b1 = generate_key()
    b2 = b1.to_hex()
    b3 = b1.public_key.format(True).hex()
    b4 = filedialog.askopenfilename()
    head, b5 = os.path.split(b4)
    b6 = os.path.join(head, f'encrypted_{b5}')
    b7 = os.path.join(head, f'decrypted_{b5}')
    with open(b4, "rb") as file:
        b8 = base64.b64encode(file.read())
    print(f"Private_key: {b2}\nPublic_key: {b3}\nType: {type(b2)}")
    print(f"Binary of the file: {b8}")
    b9 = encrypt(b3, b8)
    print(f"Encrypted binary: {b9}")
    with open(b6, "wb") as efile:
        efile.write(base64.b64decode(b9))
    b10 = decrypt(b2, b9)
    print(f"\nDecrypted: {b10}")
    with open(b7, "wb") as dfile:
        dfile.write(base64.b64decode(b10))
if b11 = = "__main__":
    fonk1()