import math
import sys
class class1:
    @staticmethod
    def fonk1():
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    @staticmethod
    def fonk2(file_name):
        with open(file_name, 'r') as file:
            return file.read()
    @staticmethod
    def fonk3(file_name):
        with open(file_name, 'r') as file:
            b1 = file.read().split(',')
            return int(b1[0]), int(b1[1]), int(b1[2])
    @staticmethod
    def fonk4(key_size, b7):
        return b7 > 0 and key_size > 0
def fonk5(b5, b7):
    for character in b5:
        if character not in class1.fonk1():
            print(f'Char in the b5 cannot be encrypted {character}')
            sys.exit()
    b2 = []
    for block_start in range(0, len(b5), b7):
        a1 = 0
        for i in range(block_start, min(block_start + b7, len(b5))):
            a1 += (class1.fonk1().index(b5[i])) *\
                         (len(class1.fonk1()) ** (i % b7))
        b2.append(a1)
    return b2
def fonk6(b5, key, b7):
    b3 = []
    num, b4 = key
    for block in fonk5(b5, b7):
        b3.append(pow(block, b4, num))
    return b3
def fonk7(b9, encrypted_file_name, b10):
    b5 = class1.fonk2(b9)
    key_size, n, b6 = class1.fonk3(b10)
    b7 = int(math.log(2 ** key_size, len(class1.fonk1())))
    if not class1.fonk4(key_size, b7):
        sys.exit('Wrong block size. Encryption aborted.')
    b8 = fonk6(b5, (n, b6), b7)
    for i in range(len(b8)):
        b8[i] = str(b8[i])
    with open(encrypted_file_name, 'w') as fo:
        fo.write('%s|%s|%s' % (len(b5), b7, ','.join(b8)))
def fonk8():
    print('1. Introduce the file name with the b5 to encrypt:')
    b9 = input()
    print('2. Introduce file name containing the public key:')
    b10 = input()
    print('3. Introduce file name to save the encrypted b5:')
    b11 = input()
    print('Encrypting...')
    fonk7(b9, b11, b10)
if b12 = = '__main__':
    fonk8()