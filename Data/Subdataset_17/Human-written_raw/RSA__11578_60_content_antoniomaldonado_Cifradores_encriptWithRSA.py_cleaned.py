import math
import sys
import utils.utils as utils
def get_int_blocks(msg, block_size):
    for character in msg:
        if character not in utils.allowed_chars():
            print('Char in the msg cannot be encrypted %s' % (character))
            sys.exit()
    block_ints = []
    for block_start in range(0, len(msg), block_size):
        block_int = 0
        for i in range(block_start, min(block_start + block_size, len(msg))):
            block_int += (utils.allowed_chars().index(msg[i])) *\
                         (len(utils.allowed_chars()) ** (i % block_size))
        block_ints.append(block_int)
    return block_ints
def get_encrypted_blocks(msg, key, block_size):
    encrypted_blocks = []
    num, enc = key
    for block in get_int_blocks(msg, block_size):
        encrypted_blocks.append(pow(block, enc, num))
    return encrypted_blocks
def encrypt(input_file_name, encrypted_file_name, pub_key_file_name):
    msg = utils.read_file(input_file_name)
    key_size, n, e = utils.read_key_file(pub_key_file_name)
    block_size = int(math.log(2 ** key_size, len(utils.allowed_chars())))
    if not utils.is_valid(key_size, block_size):
        sys.exit('Wrong block size. Encryption aborted.')
    blocks = get_encrypted_blocks(msg, (n, e), block_size)
    for i in range(len(blocks)):
        blocks[i] = str(blocks[i])
    fo = open(encrypted_file_name, 'w')
    fo.write('%s|%s|%s' % (len(msg), block_size, ','.join(blocks)))
    fo.close()
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