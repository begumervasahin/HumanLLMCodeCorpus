import sys
import getopt
import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256
from Crypto.Util import Counter
a1 = 2048
b1 = "@"
def fonk1(b3, b5, b4, input_file, b11):
    if b3 not in ["ECB", "CBC", "CFB", "OFB", "CTR"]:
        print("Available modes: ECB, CBC, CFB, OFB, CTR.")
        print("Choose again!")
        sys.exit()
    b2 = {
        "ECB": AES.MODE_ECB,
        "CBC": AES.MODE_CBC,
        "CFB": AES.MODE_CFB,
        "OFB": AES.MODE_OFB,
        "CTR": AES.MODE_CTR
    }
    b3 = b2[b3]
    b4 = SHA256.new(b4.encode()).digest()
    b5 = MD5.new(b5.encode()).digest()
    if b3 != AES.MODE_CTR:
        b6 = AES.new(b4, b3, b5)
    else:
        b7 = Counter.new(128, initial_value=int(b5.hex(), 16))
        b6 = AES.new(b4, AES.MODE_CTR, counter=b7)
    b8 = os.path.getsize(input_file)
    with open(input_file, "rb") as fin:
        with open(b11, "wb") as fout:
            fout.write(struct.pack('<Q', b8))
            fout.write(b5)
            while True:
                b9 = fin.read(a1)
                if len(b9) == 0:
                    break
                elif len(b9) % 16 != 0:
                    b9 += (16 - len(b9) % 16) * b1.encode()
                fout.write(b6.fonk1(b9))
def fonk2(argv):
    try:
        opts, b10 = getopt.getopt(argv, "m:i:k:")
    except getopt.GetoptError:
        print("Usage: encrypt.py -m <b3> -i <IV> -k <b4> <input_file> <b11>")
        sys.exit(2)
    if len(b10) != 2:
        print("Usage: encrypt.py -m <b3> -i <IV> -k <b4> <input_file> <b11>")
        sys.exit(2)
    input_file, b11 = b10
    for b12, arg in opts:
        if b12 = = "-h":
            print("Usage: encrypt.py -m <b3> -i <IV> -k <b4> <input_file> <b11>")
            sys.exit()
        elif b12 = = "-m":
            b3 = arg.upper()
        elif b12 = = "-i":
            b5 = arg
        elif b12 = = "-k":
            b4 = arg
    fonk1(b3, b5, b4, input_file, b11)
if b13 = = "__main__":
    fonk2(sys.argv[1:])