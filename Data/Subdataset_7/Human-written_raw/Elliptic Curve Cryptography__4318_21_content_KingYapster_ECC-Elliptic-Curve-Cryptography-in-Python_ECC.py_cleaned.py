from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64, os
b1 = generate_key()
b2 = b1.to_hex()
b3 = b1.public_key.format(True).hex()
b4 = filedialog.askopenfilename()
head, b5 = os.path.split(b4)
b6 = head + '/encrypted_' + str(b5)
b7 = head + '/decrypted_' + str(b5)
a1 = 0
with open(b4, "rb") as File:
    a1 = base64.b64encode(File.read())
print("Private_key:",b2,"\nPublic_key:",b3,"Type: ",type(b2))
print("Binary of the file:", a1)
b8 = encrypt(b3,a1)
print("Encrypted binary:", b8)
with open(b6,"wb") as EFile:
    EFile.write(base64.b64decode(b8))
b9 = decrypt(b2, b8)
print("\nDecrypted:",b9)
with open(b7,"wb") as DFile:
    DFile.write(base64.b64decode(b9))