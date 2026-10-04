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
    def fonk4(key_size, b9):
        return b9 > 0 and key_size > 0
def fonk5(b8, b9):
    b2 = class1.fonk1()
    b3 = len(b2)
    for character in b8:
        if character not in b2:
            print(f'Character in the message cannot be encrypted: {character}')
            sys.exit()
    b4 = []
    for block_start in range(0, len(b8), b9):
        a1 = 0
        for i in range(block_start, min(block_start + b9, len(b8))):
            a1 += b2.index(b8[i]) * (b3 ** (i % b9))
        b4.append(a1)
    return b4
def fonk6(b8, key, b9):
    n, b5 = key
    b6 = fonk5(b8, b9)
    b7 = [pow(block, b5, n) for block in b6]
    return b7
def fonk7(b11, encrypted_file_name, b12):
    b8 = class1.fonk2(b11)
    key_size, n, b5 = class1.fonk3(b12)
    b2 = class1.fonk1()
    b9 = int(math.log(2 ** key_size, len(b2)))
    if not class1.fonk4(key_size, b9):
        sys.exit('Wrong block size. Encryption aborted.')
    b7 = fonk6(b8, (n, b5), b9)
    b10 = ','.join(map(str, b7))
    with open(encrypted_file_name, 'w') as file:
        file.write(f'{len(b8)}|{b9}|{b10}')
def fonk8():
    b11 = input('1. Introduce the file name with the message to encrypt:\n')
    b12 = input('2. Introduce file name containing the public key:\n')
    b13 = input('3. Introduce file name to save the encrypted message:\n')
    print('Encrypting...')
    fonk7(b11, b13, b12)
    print('Encryption completed.')
if b14 = = '__main__':
    fonk8()