import os
import sys
from base64 import b64decode
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512
def load_key(key_path):
    with open(key_path, 'r') as key_file:
        key_content = key_file.read()
        decoded_key = b64decode(key_content)
        key = RSA.importKey(decoded_key)
    return key
def sign_data(private_key, data):
    signer = PKCS1_v1_5.new(private_key)
    data_hash = SHA512.new(data.encode())
    signature = signer.sign(data_hash)
    return signature
def get_file_signature(file_path, private_key):
    with open(file_path, "r") as file:
        contents = file.read()
    signature = sign_data(private_key, contents)
    return signature
def verify_file_signature(file_path, public_key, signature):
    with open(file_path, "r") as file:
        contents = file.read()
    verifier = PKCS1_v1_5.new(public_key)
    data_hash = SHA512.new(contents.encode())
    return verifier.verify(data_hash, signature)
def save_signature(file_path, signature):
    with open(file_path, "w") as file:
        file.write(signature.hex())
def load_signature(file_path):
    with open(file_path, "r") as file:
        signature_hex = file.read()
    return bytes.fromhex(signature_hex)
def main():
    if len(sys.argv) < 5:
        print(f"USAGE: {sys.argv[0]} <KEY FILE NAME> <SIGNATURE FILE NAME> <INPUT FILE NAME> <MODE>")
        exit(-1)
    key_file_name = sys.argv[1]
    sig_file_name = sys.argv[2]
    input_file_name = sys.argv[3]
    mode = sys.argv[4]
    key = load_key(key_file_name)
    if mode == "sign":
        signature = get_file_signature(input_file_name, key)
        save_signature(sig_file_name, signature)
        print(f"Signature saved to file {sig_file_name}")
    elif mode == "verify":
        signature = load_signature(sig_file_name)
        if verify_file_signature(input_file_name, key, signature):
            print("Match!")
        else:
            print("No match!")
    else:
        print(f"Invalid mode {mode}")
if __name__ == "__main__":
    main()