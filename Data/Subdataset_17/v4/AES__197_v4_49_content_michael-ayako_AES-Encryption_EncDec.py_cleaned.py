import os
import sys
import argparse
from tqdm import tqdm
import numpy as np
from util import logging, logger, filechk, create_key, file_converter_enc, file_converter_dec
from xored import encXOR, decXOR, encXORrounds
from bitshift import SHIFTLEFT, SHIFTRIGHT
from sbox import sbox_enc, sbox_dec, sbox_dec_rounds
def encrypt(filename):
    key = create_key()
    print(f'Share this Key {key} with the message receiver')
    key_bin = f'{key:016b}'
    logging.info("Key created")
    logging.info("Encryption has started...")
    bits = encXOR(filename, key_bin)
    bits = SHIFTLEFT(bits)
    bits = sbox_enc(bits)
    for _ in tqdm(range(16)):
        bits = encXORrounds(bits, key_bin)
        bits = SHIFTLEFT(bits)
        bits = sbox_enc(bits)
    file_converter_enc(bits)
def decrypt(filename):
    key = int(input("Input the key shared with you\n"))
    key_bin = f'{key:016b}'
    logging.info("Key received")
    logging.info("Decryption has started...")
    bits = sbox_dec(filename)
    bits = SHIFTRIGHT(bits)
    bits = decXOR(bits, key_bin)
    for _ in tqdm(range(16)):
        bits = sbox_dec_rounds(bits)
        bits = SHIFTRIGHT(bits)
        bits = decXOR(bits, key_bin)
    file_converter_dec(bits)
def main():
    logger()
    parser = argparse.ArgumentParser(description='Encrypt and Decrypt files', add_help=True)
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("FileName", help='Input a filename')
    group.add_argument('-e', '--enc', help='Select this option to encrypt the file', action='store_true')
    group.add_argument('-d', '--dec', help='Select this option to decrypt the file', action='store_true')
    parser.add_argument('-q', '--quit', help='Select this option to quit current process', action='store_true')
    args = parser.parse_args()
    filechk(args.FileName)
    if args.enc:
        encrypt(args.FileName)
    elif args.dec:
        decrypt(args.FileName)
if __name__ == '__main__':
    main()