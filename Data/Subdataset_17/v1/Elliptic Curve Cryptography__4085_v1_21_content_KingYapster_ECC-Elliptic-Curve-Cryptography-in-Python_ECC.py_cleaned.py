from ecies.utils import generate_key
from ecies import encrypt, decrypt
from tkinter import filedialog
import base64
import os
def main():
    secp_k = generate_key()
    privhex = secp_k.to_hex()
    pubhex = secp_k.public_key.format(True).hex()
    filepath = filedialog.askopenfilename()
    head, tail = os.path.split(filepath)
    encrypted_filepath = os.path.join(head, f'encrypted_{tail}')
    decrypted_filepath = os.path.join(head, f'decrypted_{tail}')
    with open(filepath, "rb") as file:
        data = base64.b64encode(file.read())
    print(f"Private_key: {privhex}\nPublic_key: {pubhex}\nType: {type(privhex)}")
    print(f"Binary of the file: {data}")
    encrypted_secp = encrypt(pubhex, data)
    print(f"Encrypted binary: {encrypted_secp}")
    with open(encrypted_filepath, "wb") as efile:
        efile.write(base64.b64decode(encrypted_secp))
    decrypted_secp = decrypt(privhex, encrypted_secp)
    print(f"\nDecrypted: {decrypted_secp}")
    with open(decrypted_filepath, "wb") as dfile:
        dfile.write(base64.b64decode(decrypted_secp))
if __name__ == "__main__":
    main()