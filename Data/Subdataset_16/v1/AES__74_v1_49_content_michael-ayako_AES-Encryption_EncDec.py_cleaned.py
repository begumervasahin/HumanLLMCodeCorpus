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
    b4 = SHIFTLEFT(b3)
    b5 = sbox_enc(b4)
    b6 = b5
    for _ in tqdm(range(16)):
        b6 = encXORrounds(b6, b2)
        b6 = SHIFTLEFT(b6)
        b6 = sbox_enc(b6)
    file_converter_enc(b6)
def fonk2(filename):
    b1 = int(input("Input the b1 shared with you\n"))
    b2 = f'{b1:016b}'
    logging.info("Key received")
    logging.info("Decryption has started...")
    b7 = sbox_dec(filename)
    b4 = SHIFTRIGHT(b7)
    b8 = decXOR(b4, b2)
    b6 = b8
    for _ in tqdm(range(16)):
        b6 = sbox_dec_rounds(b6)
        b6 = SHIFTRIGHT(b6)
        b6 = decXOR(b6, b2)
    file_converter_dec(b6)
def fonk3():
    logger()
    b9 = argparse.ArgumentParser(description='Encrypt and Decrypt files')
    b10 = b9.add_mutually_exclusive_group()
    b9.add_argument("FileName", b11 = 'Input a filename')
    b10.add_argument('-e', '--enc', b11 = 'Encrypt the file', action='store_true')
    b10.add_argument('-d', '--dec', b11 = 'Decrypt the file', action='store_true')
    b12 = b9.parse_args()
    filechk(b12.FileName)
    if b12.enc:
        fonk1(b12.FileName)
    elif b12.dec:
        fonk2(b12.FileName)
if b13 = = '__main__':
    fonk3()