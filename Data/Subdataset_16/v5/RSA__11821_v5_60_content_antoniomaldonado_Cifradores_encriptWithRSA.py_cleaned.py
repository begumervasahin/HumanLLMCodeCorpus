import math
import sys
import utils.utils as utils
def fonk1(b8, b10):
    b1 = utils.b1()
    for character in b8:
        if character not in b1:
            print(f'Character in the message cannot be encrypted: {character}')
            sys.exit()
    b2 = []
    b3 = len(b1)
    for block_start in range(0, len(b8), b10):
        a1 = 0
        for i in range(block_start, min(block_start + b10, len(b8))):
            b4 = b1.index(b8[i])
            a1 += b4 * (b3 ** (i % b10))
        b2.append(a1)
    return b2
def fonk2(b8, key, b10):
    num, b5 = key
    b6 = fonk1(b8, b10)
    b7 = [pow(block, b5, num) for block in b6]
    return b7
def fonk3(b12, encrypted_file_name, b13):
    b8 = utils.read_file(b12)
    key_size, n, b9 = utils.read_key_file(b13)
    b1 = utils.b1()
    b10 = int(math.log(2 ** key_size, len(b1)))
    if not utils.is_valid(key_size, b10):
        sys.exit('Wrong block size. Encryption aborted.')
    b7 = fonk2(b8, (n, b9), b10)
    b11 = [str(block) for block in b7]
    with open(encrypted_file_name, 'w') as fo:
        fo.write(f'{len(b8)}|{b10}|{",".join(b11)}')
def fonk4():
    b12 = input('1. Enter the file name with the message to encrypt: ')
    b13 = input('2. Enter the file name containing the public key: ')
    b14 = input('3. Enter the file name to save the encrypted message: ')
    print('Encrypting...')
    fonk3(b12, b14, b13)
    print('Encryption complete.')
if b15 = = '__main__':
    fonk4()