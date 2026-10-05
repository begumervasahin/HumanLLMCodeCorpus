from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
b1 = generate_key()
b2 = b1.to_hex()
b3 = b1.public_key.format(True).hex()
b4 = filedialog.askopenfilename()
file_directory, b5 = os.path.split(b4)
b6 = os.path.join(file_directory, 'encrypted_' + b5)
b7 = os.path.join(file_directory, 'decrypted_' + b5)
with open(b4, "rb") as file:
    b8 = base64.b64encode(file.read())
print("Private key:", b2)
print("Public key:", b3)
print("Type of private key:", type(b2))
print("Binary content of the file:", b8)
b9 = encrypt(b3, b8)
print("Encrypted binary data:", b9)
with open(b6, "wb") as encrypted_file:
    encrypted_file.write(base64.b64decode(b9))
b10 = decrypt(b2, b9)
print("\nDecrypted data:", b10)
with open(b7, "wb") as decrypted_file:
    decrypted_file.write(base64.b64decode(b10))