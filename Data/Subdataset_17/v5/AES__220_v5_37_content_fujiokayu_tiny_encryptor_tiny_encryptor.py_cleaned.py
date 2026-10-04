import sys
import os
import argparse
import json
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from AesEncipher import AesEncipher
MAX_BUFFER_SIZE = 4096
KEY_LENGTH = 32
def parse_args():
    parser = argparse.ArgumentParser(description='AES(CTR Mode) Encipher Program')
    parser.add_argument('tool_mode', choices=['e', 'd'], help='Choose e (encrypt) or d (decrypt)')
    parser.add_argument('input_file', help='File to encrypt or decrypt')
    parser.add_argument('--nonce', help='Nonce for decryption', type=str, default="")
    parser.add_argument('--key', help='Key for decryption', type=str, default="")
    return parser.parse_args()
def check_args(args):
    if not os.path.isfile(args.input_file):
        print("Error: The input file does not exist.")
        sys.exit(1)
    if args.tool_mode == 'd':
        if not args.nonce:
            print("Error: --nonce is required in decrypt mode.")
            sys.exit(1)
        if not args.key:
            print("Error: --key is required in decrypt mode.")
            sys.exit(1)
def process_file(input_file, aes_encipher, encrypt_mode):
    translated_bytes = bytearray()
    with open(input_file, 'rb') as f:
        for chunk in iter(lambda: f.read(MAX_BUFFER_SIZE), b''):
            if encrypt_mode:
                translated_bytes.extend(aes_encipher.encrypt(chunk))
            else:
                translated_bytes.extend(aes_encipher.decrypt(chunk))
    return translated_bytes
def save_output_file(output_file, translated_bytes):
    with open(output_file, 'wb') as f:
        f.write(translated_bytes)
def print_encryption_info(aes_encipher):
    encrypt_info = json.dumps({
        'nonce': b64encode(aes_encipher.get_nonce()).decode('utf-8'),
        'key': b64encode(aes_encipher.get_key()).decode('utf-8')
    })
    print("Encryption information:", encrypt_info)
def main():
    args = parse_args()
    check_args(args)
    encrypt_mode = args.tool_mode == 'e'
    key = get_random_bytes(KEY_LENGTH) if not args.key else b64decode(args.key)
    nonce = b64decode(args.nonce) if args.nonce else None
    aes_encipher = AesEncipher(AES.MODE_CTR, key, nonce)
    translated_bytes = process_file(args.input_file, aes_encipher, encrypt_mode)
    output_file = f"{args.input_file}_{'encrypted' if encrypt_mode else 'decrypted'}"
    save_output_file(output_file, translated_bytes)
    if encrypt_mode:
        print_encryption_info(aes_encipher)
if __name__ == '__main__':
    main()