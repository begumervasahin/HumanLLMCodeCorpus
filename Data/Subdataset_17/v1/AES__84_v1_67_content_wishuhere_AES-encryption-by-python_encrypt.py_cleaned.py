import sys
import getopt
import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256
from Crypto.Util import Counter
block_size = 2048
padding = "@"
def encrypt(mode, iv, key, input_file, output_file):
    if mode not in ["ECB", "CBC", "CFB", "OFB", "CTR"]:
        print("Available modes: ECB, CBC, CFB, OFB, CTR.")
        print("Choose again!")
        sys.exit()
    mode_dict = {
        "ECB": AES.MODE_ECB,
        "CBC": AES.MODE_CBC,
        "CFB": AES.MODE_CFB,
        "OFB": AES.MODE_OFB,
        "CTR": AES.MODE_CTR
    }
    mode = mode_dict[mode]
    key = SHA256.new(key.encode()).digest()
    iv = MD5.new(iv.encode()).digest()
    if mode != AES.MODE_CTR:
        encryptor = AES.new(key, mode, iv)
    else:
        ctr = Counter.new(128, initial_value=int(iv.hex(), 16))
        encryptor = AES.new(key, AES.MODE_CTR, counter=ctr)
    filesize = os.path.getsize(input_file)
    with open(input_file, "rb") as fin:
        with open(output_file, "wb") as fout:
            fout.write(struct.pack('<Q', filesize))
            fout.write(iv)
            while True:
                block = fin.read(block_size)
                if len(block) == 0:
                    break
                elif len(block) % 16 != 0:
                    block += (16 - len(block) % 16) * padding.encode()
                fout.write(encryptor.encrypt(block))
def main(argv):
    try:
        opts, args = getopt.getopt(argv, "m:i:k:")
    except getopt.GetoptError:
        print("Usage: encrypt.py -m <mode> -i <IV> -k <key> <input_file> <output_file>")
        sys.exit(2)
    if len(args) != 2:
        print("Usage: encrypt.py -m <mode> -i <IV> -k <key> <input_file> <output_file>")
        sys.exit(2)
    input_file, output_file = args
    for opt, arg in opts:
        if opt == "-h":
            print("Usage: encrypt.py -m <mode> -i <IV> -k <key> <input_file> <output_file>")
            sys.exit()
        elif opt == "-m":
            mode = arg.upper()
        elif opt == "-i":
            iv = arg
        elif opt == "-k":
            key = arg
    encrypt(mode, iv, key, input_file, output_file)
if __name__ == "__main__":
    main(sys.argv[1:])