import math
import sys
import utils.utils as utils
def get_int_blocks(msg, block_size):
    allowed_chars = utils.allowed_chars()
    for character in msg:
        if character not in allowed_chars:
            print(f'Character in the message cannot be encrypted: {character}')
            sys.exit()
    block_ints = []
    for block_start in range(0, len(msg), block_size):
        block_int = 0
        for i in range(block_start, min(block_start + block_size, len(msg))):
            block_int += (allowed_chars.index(msg[i])) * (len(allowed_chars) ** (i % block_size))
        block_ints.append(block_int)
    return block_ints
def get_encrypted_blocks(msg, key, block_size):
    num, enc = key
    int_blocks = get_int_blocks(msg, block_size)
    encrypted_blocks = [pow(block, enc, num) for block in int_blocks]
    return encrypted_blocks
def encrypt(input_file_name, encrypted_file_name, pub_key_file_name):
    msg = utils.read_file(input_file_name)
    key_size, n, e = utils.read_key_file(pub_key_file_name)
    allowed_chars = utils.allowed_chars()
    block_size = int(math.log(2 ** key_size, len(allowed_chars)))
    if not utils.is_valid(key_size, block_size):
        sys.exit('Wrong block size. Encryption aborted.')
    encrypted_blocks = get_encrypted_blocks(msg, (n, e), block_size)
    encrypted_blocks_str = [str(block) for block in encrypted_blocks]
    with open(encrypted_file_name, 'w') as fo:
        fo.write(f'{len(msg)}|{block_size}|{",".join(encrypted_blocks_str)}')
def main():
    print('1. Enter the file name with the message to encrypt:')
    input_file_name = input()
    print('2. Enter the file name containing the public key:')
    pub_key_file_name = input()
    print('3. Enter the file name to save the encrypted message:')
    output_file_name = input()
    print('Encrypting...')
    encrypt(input_file_name, output_file_name, pub_key_file_name)
    print('Encryption complete.')
if __name__ == '__main__':
    main()