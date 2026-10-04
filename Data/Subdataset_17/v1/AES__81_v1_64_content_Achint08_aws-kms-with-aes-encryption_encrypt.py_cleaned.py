import os
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import boto3
key_id = 'arn:aws:kms:xxxxxxx:key/xxxxxxxxxxxxxxxxxxxx'
master_key = 'This is a secret key'
region_name = 'xx-xxxx-1'
def pad(st):
    block_size = 16
    padding = block_size - len(st) % block_size
    padded_st = st + padding * chr(padding)
    return padded_st
def generate_key_from_KMS(master_key):
    kms = boto3.client('kms', region_name=region_name)
    try:
        response = kms.encrypt(
            KeyId=key_id,
            Plaintext=master_key
        )
        encrypted_master_key = response['CiphertextBlob']
        print(f"Encrypted master key: {encrypted_master_key}")
        print("Store the Encrypted master key. Can be used later on.")
        return encrypted_master_key
    except Exception as e:
        print(f"[ERROR]: Error during KMS calls: {e}")
        return None
def encrypt_data(master_key, data):
    try:
        hashed_key = hashlib.sha256(master_key.encode("utf-8")).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(hashed_key, AES.MODE_CBC, iv)
        padded_data = pad(data)
        encrypted_data = iv + cipher.encrypt(padded_data.encode('utf-8'))
        return base64.b64encode(encrypted_data).decode('utf-8')
    except Exception as e:
        print(f"[ERROR]: Error while data encryption: {e}")
        return None
if __name__ == "__main__":
    encrypted_master_key = generate_key_from_KMS(master_key)
    if encrypted_master_key:
        data = "Sensitive data that needs encryption"
        encrypted_data = encrypt_data(master_key, data)
        if encrypted_data:
            print(f"Encrypted data: {encrypted_data}")
        else:
            print("Data encryption failed.")
    else:
        print("Master key encryption failed.")