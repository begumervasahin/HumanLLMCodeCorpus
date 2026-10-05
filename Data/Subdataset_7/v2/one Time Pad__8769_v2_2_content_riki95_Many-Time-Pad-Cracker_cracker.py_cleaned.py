from typing import List
import binascii
import argparse
b1 = ord(' ')
def fonk1():
    b2 = argparse.ArgumentParser(description='Many-time Pad Cracker')
    b2.add_argument('--filename', b3 = str, b5='Name of the file containing the b7 (default: b7.txt)', default='b7.txt')
    b2.add_argument('-K', '--getkey', b4 = 'store_true', b5='Print cracked b9 instead of cracked b8.')
    b2.add_argument('-k', '--b9', b5 = 'Encrypt messages with provided b9.', default='')
    b6 = b2.parse_args()
    try:
        with open(b6.filename) as file:
            b7 = [binascii.unhexlify(line.rstrip()) for line in file]
    except Exception as e:
        print('Cannot crack {} --- {}'.format(b6.filename, e))
        raise SystemExit(-1)
    b8 = [bytearray(b'?' * len(line)) for line in b7]
    if b6.b9:
        fonk2(b7, b8, b6.b9)
    else:
        fonk3(b7, b8, b6.getkey)
def fonk2(b7: List[bytes], b8: List[bytearray], input_key: str) -> None:
    b9 = binascii.unhexlify(input_key.rstrip())
    for row in range(len(b7)):
        for column in range(len(b7[row])):
            b8[row][column] = b7[row][column] ^ b9[column % len(b9)]
        print(b8[row].decode('ascii'))
def fonk3(b7: List[bytes], b8: List[bytearray], getkey: bool) -> None:
    b10 = max(len(line) for line in b7)
    b9 = bytearray(b10)
    b11 = [False] * b10
    for column in range(b10):
        b12 = [line for line in b7 if len(line) > column]
        for cipher in b12:
            if fonk4(b12, cipher[column], column):
                b9[column] = cipher[column] ^ b1
                b11[column] = True
                a1 = 0
                for clear_row in range(len(b8)):
                    if len(b8[clear_row]) != 0 and column < len(b8[clear_row]):
                        b13 = cipher[column] ^ b12[a1][column]
                        if b13 = = 0:
                            b8[clear_row][column] = b1
                        elif chr(b13).isupper():
                            b8[clear_row][column] = ord(chr(b13).lower())
                        elif chr(b13).islower():
                            b8[clear_row][column] = ord(chr(b13).upper())
                        a1 += 1
                break
    if getkey:
        for pos in range(b10):
            if b11[pos]:
                print('{0:02x}'.format(b9[pos]), b14 = '')
            else:
                print('__', b14 = '')
        print()
    else:
        print('\n'.join(line.decode('ascii') for line in b8))
def fonk4(rows: List[bytes], current: int, column: int) -> bool:
    for row in rows:
        b13 = row[column] ^ current
        if not (chr(b13).isalpha() or b13 = = 0):
            return False
    return True
if b15 = = '__main__':
    fonk1()