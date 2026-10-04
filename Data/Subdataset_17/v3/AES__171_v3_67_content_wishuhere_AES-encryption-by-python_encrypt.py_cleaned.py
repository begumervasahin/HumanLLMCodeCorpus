import sys
import getopt
import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256
from Crypto.Util import Counter
BLOCK_SIZE = 2048
PADDING_CHAR = "@"
MODES = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CFB": AES.MODE_CFB,
    "OFB": AES.MODE_OFB,
    "CTR": AES.MODE_CTR
}
def get_mode(mode_str):
    mode = MODES.get(mode_str.upper())
    if mode is None:
        print("Available modes: ECB, CBC, CFB, OFB, CTR. Choose again!")
        sys.exit(2)
    return mode
def pad_data(data):
    padding_length = (16 - len(data) % 16) if len(data) % 16 != 0 else 0
    return data + (PADDING_CHAR.encode() * padding_length)
def encrypt(mode, iv, key, input_file, output_file):
    key = SHA256.new(key.encode()).digest()
    iv = MD5.new(iv.encode()).digest()
    if mode == AES.MODE_CTR:
        ctr = Counter.new(128, initial_value=int(iv.hex(), 16))
        encryptor = AES.new(key, mode, counter=ctr)
    else:
        encryptor = AES.new(key, mode, iv)
    filesize = os.path.getsize(input_file)
    with open(input_file, "rb") as fin, open(output_file, "wb") as fout:
        fout.write(struct.pack('<Q', filesize))
        fout.write(iv)
        while True:
            block = fin.read(BLOCK_SIZE)
            if not block:
                break
            block = pad_data(block)
            fout.write(encryptor.encrypt(block))
def parse_arguments(argv):
    try:
        opts, args = getopt.getopt(argv, "m:i:k:")
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    if len(args) != 2:
        print_usage()
        sys.exit(2)
    input_file, output_file = args
    mode, iv, key = None, None, None
    for opt, arg in opts:
        if opt == "-m":
            mode = get_mode(arg)
        elif opt == "-i":
            iv = arg
        elif opt == "-k":
            key = arg
    if not (mode and iv and key):
        print_usage()
        sys.exit(2)
    return mode, iv, key, input_file, output_file
def print_usage():
    print("Usage: encrypt.py -m <mode> -i <IV> -k <key> <input_file> <output_file>")
def main(argv):
    mode, iv, key, input_file, output_file = parse_arguments(argv)
    encrypt(mode, iv, key, input_file, output_file)
if __name__ == "__main__":
    main(sys.argv[1:])