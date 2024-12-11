from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
def fonk1():
    b1 = generate_key()
    b2 = b1.to_hex()
    b3 = b1.b7.format(True).hex()
    return b2, b3
def fonk2():
    b4 = filedialog.askopenfilename()
    file_directory, b5 = os.path.split(b4)
    return b4, file_directory, b5
def fonk3(b4):
    with open(b4, "rb") as file:
        b6 = base64.b64encode(file.read())
    return b6
def fonk4(b7, b6):
    return encrypt(b7, b6)
def fonk5(encrypted_file_path, b8):
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(base64.b64decode(b8))
def fonk6(private_key, b8):
    return decrypt(private_key, b8)
def fonk7(decrypted_file_path, b9):
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(base64.b64decode(b9))
private_key, b7 = fonk1()
b4, file_directory, b5 = fonk2()
b6 = fonk3(b4)
b8 = fonk4(b7, b6)
fonk5(os.path.join(file_directory, 'encrypted_' + b5), b8)
b9 = fonk6(private_key, b8)
fonk7(os.path.join(file_directory, 'decrypted_' + b5), b9)