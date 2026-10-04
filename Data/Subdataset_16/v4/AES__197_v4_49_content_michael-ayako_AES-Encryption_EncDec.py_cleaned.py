import os
import sys
import argparse
from tqdm import tqdm
import numpy as np
from util import logging, logger, filechk, create_key, file_converter_enc, file_converter_dec
from xored import encXOR, decXOR, encXORrounds
from bitshift import SHIFTLEFT, SHIFTRIGHT
from sbox import sbox_enc, sbox_dec, sbox_dec_rounds
def fonk1(filename):
    b1 = create_key()
    print(f'Share this Key {b1} with the message receiver')
    b2 = f'{b1:016b}'
    logging.info("Key created")
    logging.info("Encryption has started...")
    b3 = encXOR(filename, b2)
    b3 = SHIFTLEFT(b3)
    b3 = sbox_enc(b3)
    for _ in tqdm(range(16)):
        b3 = encXORrounds(b3, b2)
        b3 = SHIFTLEFT(b3)
        b3 = sbox_enc(b3)
    file_converter_enc(b3)
def fonk2(filename):
    b1 = int(input("Input the b1 shared with you\n"))
    b2 = f'{b1:016b}'
    logging.info("Key received")
    logging.info("Decryption has started...")
    b3 = sbox_dec(filename)
    b3 = SHIFTRIGHT(b3)
    b3 = decXOR(b3, b2)
    for _ in tqdm(range(16)):
        b3 = sbox_dec_rounds(b3)
        b3 = SHIFTRIGHT(b3)
        b3 = decXOR(b3, b2)
    file_converter_dec(b3)
def fonk3():
    logger()
    b4 = argparse.ArgumentParser(description='Encrypt and Decrypt files', add_help=True)
    b5 = b4.add_mutually_exclusive_group()
    b4.add_argument("FileName", b6 = 'Input a filename')
    b5.add_argument('-e', '--enc', b6 = 'Select this option to encrypt the file', action='store_true')
    b5.add_argument('-d', '--dec', b6 = 'Select this option to decrypt the file', action='store_true')
    b4.add_argument('-q', '--quit', b6 = 'Select this option to quit current process', action='store_true')
    b7 = b4.parse_args()
    filechk(b7.FileName)
    if b7.enc:
        fonk1(b7.FileName)
    elif b7.dec:
        fonk2(b7.FileName)
if b8 = = '__main__':
    fonk3()