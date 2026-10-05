from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
def generate_ecies_key_pair():
    key_pair = generate_key()
    private_key_hex = key_pair.to_hex()
    public_key_hex = key_pair.public_key.format(True).hex()
    return private_key_hex, public_key_hex
def select_file():
    file_path = filedialog.askopenfilename()
    file_directory, file_name = os.path.split(file_path)
    return file_path, file_directory, file_name
def read_file_and_encode(file_path):
    with open(file_path, "rb") as file:
        file_data = base64.b64encode(file.read())
    return file_data
def encrypt_file(public_key, file_data):
    return encrypt(public_key, file_data)
def write_encrypted_file(encrypted_file_path, encrypted_data):
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(base64.b64decode(encrypted_data))
def decrypt_data(private_key, encrypted_data):
    return decrypt(private_key, encrypted_data)
def write_decrypted_file(decrypted_file_path, decrypted_data):
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(base64.b64decode(decrypted_data))
private_key, public_key = generate_ecies_key_pair()
file_path, file_directory, file_name = select_file()
file_data = read_file_and_encode(file_path)
encrypted_data = encrypt_file(public_key, file_data)
write_encrypted_file(os.path.join(file_directory, 'encrypted_' + file_name), encrypted_data)
decrypted_data = decrypt_data(private_key, encrypted_data)
write_decrypted_file(os.path.join(file_directory, 'decrypted_' + file_name), decrypted_data)