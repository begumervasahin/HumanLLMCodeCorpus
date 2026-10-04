import os
import sys
import argparse
from tqdm import tqdm
import time
import numpy as np
from util import logging,logger,filechk,create_key,file_converter_enc,file_converter_dec
from xored import encXOR, decXOR, encXORrounds
from bitshift import SHIFTLEFT, SHIFTRIGHT
from sbox import sbox_enc,sbox_dec,sbox_dec_rounds
def fonk1(filename):
    b1 = create_key()
    print('Share this Key %s with the message reciever'%(b1))
    b1 = '{0:016b}'.format(int(hex(b1),16))
    logging.info("Key created")
    logging.info("Encryption has started...")
    b2 = encXOR(filename,b1)
    b3 = SHIFTLEFT(b2)
    b4 = sbox_enc(b3)
    b5 = b4
    for x in tqdm(range(16)):
        b5 = encXORrounds(b5,b1)
        b5 = SHIFTLEFT(b2)
        b5 = sbox_enc(b3)
    file_converter_enc(b5)
def fonk2(filename):
    b1 = int(input("Input the key shared to you\n"))
    b1 = '{0:016b}'.format(int(hex(b1),16))
    logging.info("Key recieved")
    logging.info("Decryption has started...")
    b6 = sbox_dec(filename)
    b3 = SHIFTRIGHT(b6)
    b7 = decXOR(b3,b1)
    b5 = b7
    for x in tqdm(range(16)):
        b5 = sbox_dec_rounds(b5)
        b5 = SHIFTRIGHT(b6)
        b5 = decXOR(b3,b1)
    file_converter_dec(b5)
def fonk3():
    logger()
    b8 = argparse.ArgumentParser(description='Lets Encrypt and Decrypt some files', add_help=True)
    b9 = b8.add_mutually_exclusive_group()
    b8.add_argument("FileName",b10 = 'Input a filename')
    b9.add_argument('-e','--enc',b10 = 'Select this option to encrypt the file',action = 'store_true')
    b9.add_argument('-d','--dec',b10 = 'Select this option to decrypt the file',action = 'store_true')
    b8.add_argument('-q','--quit',b10 = 'Select this option to quit current proccess',action = 'store_true')
    b11 = b8.parse_args()
    filechk(b11.FileName)
    if b11.enc:
        fonk1(b11.FileName)
    elif b11.dec:
        fonk2(b11.FileName)
if b12 = = '__main__':
    fonk3()