import os
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA512
from base64 import b64encode, b64decode
def load_key(key_path):
    with open(key_path, 'r') as key_file:
        key_file_content = key_file.read()
        decoded_key = b64decode(key_file_content)
        key = RSA.import_key(decoded_key)
    return key
def sign_message(sig_key, message):
    hash_obj = SHA512.new(message.encode())
    signature = pkcs1_15.new(sig_key).sign(hash_obj)
    return signature
def get_file_signature(file_name, priv_key):
    with open(file_name, "rb") as f:
        contents = f.read()
        file_hash = SHA512.new(contents)
        signature = pkcs1_15.new(priv_key).sign(file_hash)
    return signature
def verify_file_signature(file_name, pub_key, signature):
    with open(file_name, "rb") as f:
        contents = f.read()
        file_hash = SHA512.new(contents)
        try:
            pkcs1_15.new(pub_key).verify(file_hash, signature)
            return True
        except (ValueError, TypeError):
            return False
def save_signature(file_name, signature):
    with open(file_name, "wb") as f:
        f.write(signature)
def load_signature(file_name):
    with open(file_name, "rb") as f:
        signature = f.read()
    return signature
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
        result = get_file_signature(input_file_name, key)
        save_signature(sig_file_name, result)
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