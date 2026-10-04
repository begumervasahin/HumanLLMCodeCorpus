import math
import sys
import utils.utils as utils
def fonk1(b4, b6):
    for character in b4:
        if character not in utils.allowed_chars():
            print('Char in the b4 cannot be encrypted %s' % (character))
            sys.exit()
    b1 = []
    for block_start in range(0, len(b4), b6):
        a1 = 0
        for i in range(block_start, min(block_start + b6, len(b4))):
            a1 += (utils.allowed_chars().index(b4[i])) *\
                         (len(utils.allowed_chars()) ** (i % b6))
        b1.append(a1)
    return b1
def fonk2(b4, key, b6):
    b2 = []
    num, b3 = key
    for block in fonk1(b4, b6):
        b2.append(pow(block, b3, num))
    return b2
def fonk3(b9, encrypted_file_name, b10):
    b4 = utils.read_file(b9)
    key_size, n, b5 = utils.read_key_file(b10)
    b6 = int(math.log(2 ** key_size, len(utils.allowed_chars())))
    if not utils.is_valid(key_size, b6):
        sys.exit('Wrong block size. Encryption aborted.')
    b7 = fonk2(b4, (n, b5), b6)
    for i in range(len(b7)):
        b7[i] = str(b7[i])
    b8 = open(encrypted_file_name, 'w')
    b8.write('%s|%s|%s' % (len(b4), b6, ','.join(b7)))
    b8.close()
def fonk4():
    print('1. Introduce the file name with the b4 to encrypt:')
    b9 = input()
    print('2. Introduce file name containing the public key:')
    b10 = input()
    print('3. Introduce file name to save the encrypted b4:')
    b11 = input()
    print('Encrypting...')
    fonk3(b9, b11, b10)
if b12 = = '__main__':
    fonk4()