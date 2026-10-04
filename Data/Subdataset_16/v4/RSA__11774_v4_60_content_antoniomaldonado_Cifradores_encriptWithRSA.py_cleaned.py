import math
import sys
import utils.utils as utils
def fonk1(b6, b8):
    b1 = utils.b1()
    for character in b6:
        if character not in b1:
            print(f'Character in the message cannot be encrypted: {character}')
            sys.exit()
    b2 = []
    for block_start in range(0, len(b6), b8):
        a1 = 0
        for i in range(block_start, min(block_start + b8, len(b6))):
            a1 += (b1.index(b6[i])) * (len(b1) ** (i % b8))
        b2.append(a1)
    return b2
def fonk2(b6, key, b8):
    num, b3 = key
    b4 = fonk1(b6, b8)
    b5 = [pow(block, b3, num) for block in b4]
    return b5
def fonk3(b10, encrypted_file_name, b11):
    b6 = utils.read_file(b10)
    key_size, n, b7 = utils.read_key_file(b11)
    b1 = utils.b1()
    b8 = int(math.log(2 ** key_size, len(b1)))
    if not utils.is_valid(key_size, b8):
        sys.exit('Wrong block size. Encryption aborted.')
    b5 = fonk2(b6, (n, b7), b8)
    b9 = [str(block) for block in b5]
    with open(encrypted_file_name, 'w') as fo:
        fo.write(f'{len(b6)}|{b8}|{",".join(b9)}')
def fonk4():
    print('1. Enter the file name with the message to encrypt:')
    b10 = input()
    print('2. Enter the file name containing the public key:')
    b11 = input()
    print('3. Enter the file name to save the encrypted message:')
    b12 = input()
    print('Encrypting...')
    fonk3(b10, b12, b11)
    print('Encryption complete.')
if b13 = = '__main__':
    fonk4()