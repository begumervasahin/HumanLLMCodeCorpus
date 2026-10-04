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
    for character in msg:
        if character not in Utils.allowed_chars():
            print(f'Char in the msg cannot be encrypted {character}')
            sys.exit()
    block_ints = []
    for block_start in range(0, len(msg), block_size):
        block_int = 0
        for i in range(block_start, min(block_start + block_size, len(msg))):
            block_int += (Utils.allowed_chars().index(msg[i])) *\
                         (len(Utils.allowed_chars()) ** (i % block_size))
        block_ints.append(block_int)
    return block_ints
def get_encrypted_blocks(msg, key, block_size):
    encrypted_blocks = []
    num, enc = key
    for block in get_int_blocks(msg, block_size):
        encrypted_blocks.append(pow(block, enc, num))
    return encrypted_blocks
def encrypt(input_file_name, encrypted_file_name, pub_key_file_name):
    msg = Utils.read_file(input_file_name)
    key_size, n, e = Utils.read_key_file(pub_key_file_name)
    block_size = int(math.log(2 ** key_size, len(Utils.allowed_chars())))
    if not Utils.is_valid(key_size, block_size):
        sys.exit('Wrong block size. Encryption aborted.')
    blocks = get_encrypted_blocks(msg, (n, e), block_size)
    for i in range(len(blocks)):
        blocks[i] = str(blocks[i])
    with open(encrypted_file_name, 'w') as fo:
        fo.write('%s|%s|%s' % (len(msg), block_size, ','.join(blocks)))
def main():
    print('1. Introduce the file name with the msg to encrypt:')
    input_file_name = input()
    print('2. Introduce file name containing the public key:')
    pub_key_file_name = input()
    print('3. Introduce file name to save the encrypted msg:')
    output_file_name = input()
    print('Encrypting...')
    encrypt(input_file_name, output_file_name, pub_key_file_name)
if __name__ == '__main__':
    main()