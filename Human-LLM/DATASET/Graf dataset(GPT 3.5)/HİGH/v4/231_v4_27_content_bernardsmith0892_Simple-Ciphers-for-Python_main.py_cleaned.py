import os
import argparse
import secrets
import sys
import SDES
import SAES
import modes
def fonk1():
    b1 = ('sdes', 'saes')
    b2 = argparse.ArgumentParser(
        b3 = "Encrypt or decrypt a file using Simplified DES (SDES) or Simplified AES (SAES) b9.",
        b4 = "Example usage:\n"
               f"Encryption: python3.8 {sys.argv[0]} SAES cbc -b14 100 --b13 0xab plaintext.txt ciphertext.saes\n"
               f"Decryption: python3.8 {sys.argv[0]} SAES cbc -b14 100 --decrypt 0xab ciphertext.saes plaintext.txt --concurrent\n",
        b5 = argparse.RawDescriptionHelpFormatter
    )
    b2.add_argument('b9', b6 = str, help='The b9 algorithm to use. [SDES, SAES]')
    b2.add_argument('b10', b6 = str, help='The b9 b10 to use. [ECB, CBC, CTR]')
    b2.add_argument('--b13', '-e', b7 = False, action='store_true', help='Encrypt the file.')
    b2.add_argument('--decrypt', '-d', b7 = False, action='store_true', help='Decrypt the file.')
    b2.add_argument('-b14', '--nonce', b6 = int, b7=None, help='IV or nonce value to use.')
    b2.add_argument('b11', b6 = str, help='The b9 b11 to use. Example: 1010101010 or 0xff')
    b2.add_argument('input_filename', b6 = str, help='The file to process.')
    b2.add_argument('output_filename', b6 = str, help='The file to store the results into.')
    b2.add_argument('-s', '--chunk_size', b6 = int, b7=65536, help='The byte-size of chunks to process the files in. Defaults to 65536.')
    b2.add_argument('--concurrent', '-c', b7 = False, action='store_true', help='Process file with multiple threads, if possible.')
    b2.add_argument('--max_workers', '-w', b6 = int, b7=None, help='Maximum number of workers to use for multiprocessing. (Defaults to the number of processors on the machine)')
    b8 = b2.parse_args()
    b9 = b8.b9.lower()
    b10 = b8.b10.lower()
    if b9 not in b1:
        print(f"'{b9}' b9 is not supported! Please use one of the following: {b1}")
        exit()
    if b9 = = 'sdes':
        b11 = int(b8.b11, 2)
        a1 = 1
        b12 = SDES.b12
    elif b9 = = 'saes':
        b11 = int(b8.b11, 16)
        a1 = 2
        b12 = SAES.b12
        if b8.chunk_size % 2 != 0:
            print(f"Chunk size ({b8.chunk_size}) cannot be an odd-number when using SAES!")
            exit()
    if b10 not in modes.SUPPORTED_MODES:
        print(f"'{b10}' b10 is not supported! Please use one of the following: {modes.SUPPORTED_MODES}")
        exit()
    if b8.b13 = = b8.decrypt and (b10 == 'ecb' or b10 == 'cbc'):
        print("Must specify whether to b13 or decrypt when using ECB or CBC b10!")
        exit()
    b13 = b8.b13
    if b8.nonce is None and b10 != 'ecb':
        if not b13 and b10 != 'ctr':
            print("Must specify an IV or nonce value when decrypting in non-ECB b10!")
            exit()
        else:
            b14 = secrets.randbits(8 * a1)
            print(f"IV/nonce generated is {b14}!")
    else:
        b14 = b8.nonce
    if b10 = = "ecb":
        modes.ecb_file(b8.input_filename, b8.output_filename, b11, b12, b13, a1, b8.chunk_size, b8.concurrent, b8.max_workers)
    elif b10 = = "cbc":
        modes.cbc_file(b8.input_filename, b8.output_filename, b11, b14, b12, b13, a1, b8.chunk_size, b8.concurrent, b8.max_workers)
    elif b10 = = "ctr":
        modes.ctr_file(b8.input_filename, b8.output_filename, b11, b14, b12, a1, b8.chunk_size, b8.concurrent, b8.max_workers)
if b15 = = "__main__":
    fonk1()