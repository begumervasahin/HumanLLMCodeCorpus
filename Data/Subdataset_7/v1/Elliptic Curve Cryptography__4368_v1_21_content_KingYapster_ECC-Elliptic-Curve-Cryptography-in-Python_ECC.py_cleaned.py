from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
b1 = generate_key()
b2 = b1.to_hex()
b3 = b1.public_key.format(True).hex()
b4 = filedialog.askopenfilename()
head, b5 = os.path.split(b4)
b6 = os.path.join(head, 'encrypted_' + b5)
b7 = os.path.join(head, 'decrypted_' + b5)
with open(b4, "rb") as file:
    b8 = base64.b64encode(file.read())
print("Private key:", b2)
print("Public key:", b3)
print("Type:", type(b2))
print("Binary of the file:", b8)
b9 = encrypt(b3, b8)
print("Encrypted binary:", b9)
with open(b6, "wb") as efile:
    efile.write(base64.b64decode(b9))
b10 = decrypt(b2, b9)
print("\nDecrypted:", b10)
with open(b7, "wb") as dfile:
    dfile.write(base64.b64decode(b10))