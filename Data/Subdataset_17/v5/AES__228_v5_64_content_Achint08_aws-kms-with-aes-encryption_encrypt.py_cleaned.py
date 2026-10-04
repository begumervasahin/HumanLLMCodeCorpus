import os
from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import base64
import boto3
KEY_ID = 'arn:aws:kms:xxxxxxx:key/xxxxxxxxxxxxxxxxxxxx'
MASTER_KEY = 'This is a secret key'
REGION_NAME = 'xx-xxxx-1'
BLOCK_SIZE = 16
def pad(data):
    padding = BLOCK_SIZE - len(data) % BLOCK_SIZE
    padded_data = data + padding * chr(padding)
    return padded_data
def generate_key_from_kms(master_key):
    kms = boto3.client('kms', region_name=REGION_NAME)
    try:
        response = kms.encrypt(
            KeyId=KEY_ID,
            Plaintext=master_key
        )
        encrypted_master_key = response['CiphertextBlob']
        print(f"Encrypted master key: {encrypted_master_key}")
        print("Store the encrypted master key. It can be used later.")
        return encrypted_master_key
    except Exception as e:
        print(f"[ERROR]: Error during KMS calls: {e}")
        return None
def encrypt_data(master_key, data):
    try:
        hashed_key = hashlib.sha256(master_key.encode('utf-8')).digest()
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(hashed_key, AES.MODE_CBC, iv)
        padded_data = pad(data)
        encrypted_data = iv + cipher.encrypt(padded_data.encode('utf-8'))
        return base64.b64encode(encrypted_data).decode('utf-8')
    except Exception as e:
        print(f"[ERROR]: Error while data encryption: {e}")
        return None
if __name__ == "__main__":
    encrypted_master_key = generate_key_from_kms(MASTER_KEY)
    if encrypted_master_key:
        data = "Sensitive data that needs encryption"
        encrypted_data = encrypt_data(MASTER_KEY, data)
        if encrypted_data:
            print(f"Encrypted data: {encrypted_data}")
        else:
            print("Data encryption failed.")
    else:
        print("Master key encryption failed.")