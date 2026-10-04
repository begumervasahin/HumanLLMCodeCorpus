import base64
import os
from tkinter import filedialog
from ecies.utils import generate_key
from ecies import encrypt, decrypt
def generate_ecc_key_pair():
    secp_k = generate_key()
    privhex = secp_k.to_hex()
    pubhex = secp_k.public_key.format(True).hex()
    return privhex, pubhex
def read_file(filepath):
    with open(filepath, "rb") as file:
        return base64.b64encode(file.read())
def write_file(filepath, data):
    with open(filepath, "wb") as file:
        file.write(base64.b64decode(data))
def main():
    privhex, pubhex = generate_ecc_key_pair()
    filepath = filedialog.askopenfilename()
    if not filepath:
        print("No file selected.")
        return
    head, tail = os.path.split(filepath)
    encrypted_filepath = os.path.join(head, f'encrypted_{tail}')
    decrypted_filepath = os.path.join(head, f'decrypted_{tail}')
    data = read_file(filepath)
    print(f"Private Key: {privhex}\nPublic Key: {pubhex}\nType: {type(privhex)}")
    print(f"Binary of the file: {data}")
    encrypted_data = encrypt(pubhex, data)
    print(f"Encrypted binary: {encrypted_data}")
    write_file(encrypted_filepath, encrypted_data)
    decrypted_data = decrypt(privhex, encrypted_data)
    print(f"\nDecrypted: {decrypted_data}")
    write_file(decrypted_filepath, decrypted_data)
if __name__ == "__main__":
    main()