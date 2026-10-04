import math
import sys
class Utils:
    @staticmethod
    def allowed_chars():
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    @staticmethod
    def read_file(file_name):
        with open(file_name, 'r') as file:
            return file.read()
    @staticmethod
    def read_key_file(file_name):
        with open(file_name, 'r') as file:
            key_data = file.read().split(',')
            return int(key_data[0]), int(key_data[1]), int(key_data[2])
    @staticmethod
    def is_valid(key_size, block_size):
        return block_size > 0 and key_size > 0
def get_int_blocks(msg, block_size):
    allowed_chars = Utils.allowed_chars()
    base = len(allowed_chars)
    for character in msg:
        if character not in allowed_chars:
            print(f'Character in the message cannot be encrypted: {character}')
            sys.exit()
    block_ints = []
    for block_start in range(0, len(msg), block_size):
        block_int = 0
        for i in range(block_start, min(block_start + block_size, len(msg))):
            block_int += allowed_chars.index(msg[i]) * (base ** (i % block_size))
        block_ints.append(block_int)
    return block_ints
def get_encrypted_blocks(msg, key, block_size):
    n, e = key
    int_blocks = get_int_blocks(msg, block_size)
    encrypted_blocks = [pow(block, e, n) for block in int_blocks]
    return encrypted_blocks
def encrypt(input_file_name, encrypted_file_name, pub_key_file_name):
    msg = Utils.read_file(input_file_name)
    key_size, n, e = Utils.read_key_file(pub_key_file_name)
    allowed_chars = Utils.allowed_chars()
    block_size = int(math.log(2 ** key_size, len(allowed_chars)))
    if not Utils.is_valid(key_size, block_size):
        sys.exit('Wrong block size. Encryption aborted.')
    encrypted_blocks = get_encrypted_blocks(msg, (n, e), block_size)
    encrypted_blocks_str = ','.join(map(str, encrypted_blocks))
    with open(encrypted_file_name, 'w') as file:
        file.write(f'{len(msg)}|{block_size}|{encrypted_blocks_str}')
def main():
    input_file_name = input('1. Introduce the file name with the message to encrypt:\n')
    pub_key_file_name = input('2. Introduce file name containing the public key:\n')
    output_file_name = input('3. Introduce file name to save the encrypted message:\n')
    print('Encrypting...')
    encrypt(input_file_name, output_file_name, pub_key_file_name)
    print('Encryption completed.')
if __name__ == '__main__':
    main()