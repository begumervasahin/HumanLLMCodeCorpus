import argparse
from os import path
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
def get_key(password):
    if password is None:
        password = "MyDefaultPassword"
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()
def encrypt(filename, key):
    key = get_key(key)
    chunksize = 64 * 1024
    output_file = f"{filename}.enc"
    filesize = str(path.getsize(filename)).zfill(16)
    iv = Random.new().read(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    with open(filename, 'rb') as infile:
        with open(output_file, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(iv)
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))
def decrypt(filename, key):
    key = get_key(key)
    chunksize = 64 * 1024
    output_file = filename[:-4]
    with open(filename, 'rb') as infile:
        filesize = int(infile.read(16))
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files using AES encryption.")
    parser.add_argument('-e', '--encrypt-file', help='Encrypt a given file')
    parser.add_argument('-p', '--password', help='Password used for encryption and decryption')
    parser.add_argument('-d', '--decrypt-file', help='Decrypt a given file')
    args = parser.parse_args()
    if args.encrypt_file:
        print(f'Encrypting: {args.encrypt_file}')
        encrypt(args.encrypt_file, args.password)
        print('Encryption complete!')
    elif args.decrypt_file:
        print(f'Decrypting: {args.decrypt_file}')
        decrypt(args.decrypt_file, args.password)
        print('Decryption complete!')
    else:
        parser.print_help()
if __name__ == "__main__":
    main()