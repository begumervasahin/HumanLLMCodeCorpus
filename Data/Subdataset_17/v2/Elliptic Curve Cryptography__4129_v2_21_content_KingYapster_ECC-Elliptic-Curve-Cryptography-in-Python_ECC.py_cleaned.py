from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
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
    head, tail = os.path.split(filepath)
    encrypted_filepath = os.path.join(head, f'encrypted_{tail}')
    decrypted_filepath = os.path.join(head, f'decrypted_{tail}')
    data = read_file(filepath)
    print(f"Private_key: {privhex}\nPublic_key: {pubhex}\nType: {type(privhex)}")
    print(f"Binary of the file: {data}")
    encrypted_secp = encrypt(pubhex, data)
    print(f"Encrypted binary: {encrypted_secp}")
    write_file(encrypted_filepath, encrypted_secp)
    decrypted_secp = decrypt(privhex, encrypted_secp)
    print(f"\nDecrypted: {decrypted_secp}")
    write_file(decrypted_filepath, decrypted_secp)
if __name__ == "__main__":
    main()