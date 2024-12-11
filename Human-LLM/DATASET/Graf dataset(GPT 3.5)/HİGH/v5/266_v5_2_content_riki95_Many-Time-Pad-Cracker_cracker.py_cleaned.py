from typing import List
import binascii
import argparse
b1 = ord(' ')
def fonk1():
    b2 = fonk2()
    b3 = fonk3(b2.filename)
    b4 = [bytearray(b'?' * len(line)) for line in b3]
    if b2.b9:
        fonk4(b3, b4, b2.b9)
    else:
        fonk5(b3, b4, b2.getkey)
def fonk2():
    b5 = argparse.ArgumentParser(description='Many-time Pad Cracker')
    b5.add_argument('--filename', b6 = str, b8='Name of the file containing the b3 (default: b3.txt)', default='b3.txt')
    b5.add_argument('-K', '--getkey', b7 = 'store_true', b8='Print cracked b9 instead of cracked b4.')
    b5.add_argument('-k', '--b9', b8 = 'Encrypt messages with provided b9.', default='')
    return b5.parse_args()
def fonk3(filename):
    try:
        with open(filename) as file:
            return [binascii.unhexlify(line.rstrip()) for line in file]
    except Exception as e:
        print(f'Cannot crack {filename} --- {e}')
        raise SystemExit(-1)
def fonk4(b3, b4, b9):
    b9 = binascii.unhexlify(b9.rstrip())
    for row, ciphertext in enumerate(b3):
        for column, byte in enumerate(ciphertext):
            b4[row][column] = byte ^ b9[column % len(b9)]
        print(b4[row].decode('ascii'))
def fonk5(b3, b4, getkey):
    b10 = max(len(line) for line in b3)
    b9 = bytearray(b10)
    b11 = [False] * b10
    for column in range(b10):
        b12 = [line for line in b3 if len(line) > column]
        for cipher in b12:
            if fonk6(b12, cipher[column], column):
                b9[column] = cipher[column] ^ b1
                b11[column] = True
                a1 = 0
                for clear_row in range(len(b4)):
                    if len(b4[clear_row]) != 0 and column < len(b4[clear_row]):
                        b13 = cipher[column] ^ b12[a1][column]
                        if b13 = = 0:
                            b4[clear_row][column] = b1
                        elif chr(b13).isupper():
                            b4[clear_row][column] = ord(chr(b13).lower())
                        elif chr(b13).islower():
                            b4[clear_row][column] = ord(chr(b13).upper())
                        a1 += 1
                break
    if getkey:
        fonk7(b9, b11, b10)
    else:
        fonk8(b4)
def fonk6(rows, current, column):
    for row in rows:
        b13 = row[column] ^ current
        if not (chr(b13).isalpha() or b13 = = 0):
            return False
    return True
def fonk7(b9, b11, b10):
    for pos in range(b10):
        if b11[pos]:
            print(f'{b9[pos]:02x}', b14 = '')
        else:
            print('__', b14 = '')
    print()
def fonk8(b4):
    print('\n'.join(line.decode('ascii') for line in b4))
if b15 = = '__main__':
    fonk1()