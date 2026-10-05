from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
secp_k = generate_key()
privhex = secp_k.to_hex()
pubhex = secp_k.public_key.format(True).hex()
filepath = filedialog.askopenfilename()
head, tail = os.path.split(filepath)
newfilepath1 = os.path.join(head, 'encrypted_' + tail)
newfilepath2 = os.path.join(head, 'decrypted_' + tail)
with open(filepath, "rb") as file:
    data = base64.b64encode(file.read())
print("Private key:", privhex)
print("Public key:", pubhex)
print("Type:", type(privhex))
print("Binary of the file:", data)
encrypted_data = encrypt(pubhex, data)
print("Encrypted binary:", encrypted_data)
with open(newfilepath1, "wb") as efile:
    efile.write(base64.b64decode(encrypted_data))
decrypted_data = decrypt(privhex, encrypted_data)
print("\nDecrypted:", decrypted_data)
with open(newfilepath2, "wb") as dfile:
    dfile.write(base64.b64decode(decrypted_data))