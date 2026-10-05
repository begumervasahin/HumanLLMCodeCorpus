from typing import List
import binascii
import argparse
SPACE = ord(' ')
def main():
    args = parse_arguments()
    ciphertexts = read_ciphertexts(args.filename)
    cleartexts = [bytearray(b'?' * len(line)) for line in ciphertexts]
    if args.key:
        decrypt_with_key(ciphertexts, cleartexts, args.key)
    else:
        crack_ciphertexts(ciphertexts, cleartexts, args.getkey)
def parse_arguments():
    parser = argparse.ArgumentParser(description='Many-time Pad Cracker')
    parser.add_argument('--filename', type=str, help='Name of the file containing the ciphertexts (default: ciphertexts.txt)', default='ciphertexts.txt')
    parser.add_argument('-K', '--getkey', action='store_true', help='Print cracked key instead of cracked cleartexts.')
    parser.add_argument('-k', '--key', help='Encrypt messages with provided key.', default='')
    return parser.parse_args()
def read_ciphertexts(filename):
    try:
        with open(filename) as file:
            return [binascii.unhexlify(line.rstrip()) for line in file]
    except Exception as e:
        print(f'Cannot crack {filename} --- {e}')
        raise SystemExit(-1)
def decrypt_with_key(ciphertexts, cleartexts, key):
    key = binascii.unhexlify(key.rstrip())
    for row, ciphertext in enumerate(ciphertexts):
        for column, byte in enumerate(ciphertext):
            cleartexts[row][column] = byte ^ key[column % len(key)]
        print(cleartexts[row].decode('ascii'))
def crack_ciphertexts(ciphertexts, cleartexts, getkey):
    max_length = max(len(line) for line in ciphertexts)
    key = bytearray(max_length)
    key_mask = [False] * max_length
    for column in range(max_length):
        pending_ciphers = [line for line in ciphertexts if len(line) > column]
        for cipher in pending_ciphers:
            if is_space(pending_ciphers, cipher[column], column):
                key[column] = cipher[column] ^ SPACE
                key_mask[column] = True
                i = 0
                for clear_row in range(len(cleartexts)):
                    if len(cleartexts[clear_row]) != 0 and column < len(cleartexts[clear_row]):
                        result = cipher[column] ^ pending_ciphers[i][column]
                        if result == 0:
                            cleartexts[clear_row][column] = SPACE
                        elif chr(result).isupper():
                            cleartexts[clear_row][column] = ord(chr(result).lower())
                        elif chr(result).islower():
                            cleartexts[clear_row][column] = ord(chr(result).upper())
                        i += 1
                break
    if getkey:
        print_cracked_key(key, key_mask, max_length)
    else:
        print_cracked_cleartexts(cleartexts)
def is_space(rows, current, column):
    for row in rows:
        result = row[column] ^ current
        if not (chr(result).isalpha() or result == 0):
            return False
    return True
def print_cracked_key(key, key_mask, max_length):
    for pos in range(max_length):
        if key_mask[pos]:
            print(f'{key[pos]:02x}', end='')
        else:
            print('__', end='')
    print()
def print_cracked_cleartexts(cleartexts):
    print('\n'.join(line.decode('ascii') for line in cleartexts))
if __name__ == '__main__':
    main()