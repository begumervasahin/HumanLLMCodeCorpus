import sys
import getopt
import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256
from Crypto.Util import Counter
a1 = 2048
b1 = "@"
def fonk1(mode_str):
    b2 = {
        "ECB": AES.MODE_ECB,
        "CBC": AES.MODE_CBC,
        "CFB": AES.MODE_CFB,
        "OFB": AES.MODE_OFB,
        "CTR": AES.MODE_CTR
    }
    if mode_str not in b2:
        print("Available b2: ECB, CBC, CFB, OFB, CTR. Choose again!")
        sys.exit()
    return b2[mode_str]
def fonk2(data):
    if len(data) % 16 != 0:
        b3 = 16 - len(data) % 16
        data += b1.encode() * b3
    return data
def fonk3(b13, b5, b4, input_file, b11):
    b4 = SHA256.new(b4.encode()).digest()
    b5 = MD5.new(b5.encode()).digest()
    if b13 != AES.MODE_CTR:
        b6 = AES.new(b4, b13, b5)
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
                b9 = fonk2(b9)
                fout.write(b6.fonk3(b9))
def fonk4(argv):
    try:
        opts, b10 = getopt.getopt(argv, "m:i:k:")
    except getopt.GetoptError:
        fonk5()
        sys.exit(2)
    if len(b10) != 2:
        fonk5()
        sys.exit(2)
    input_file, b11 = b10
    b13, b5, b4 = None, None, None
    for b12, arg in opts:
        if b12 = = "-h":
            fonk5()
            sys.exit()
        elif b12 = = "-m":
            b13 = fonk1(arg.upper())
        elif b12 = = "-i":
            b5 = arg
        elif b12 = = "-k":
            b4 = arg
    if not (b13 and b5 and b4):
        fonk5()
        sys.exit(2)
    return b13, b5, b4, input_file, b11
def fonk5():
    print("Usage: encrypt.py -m <b13> -i <IV> -k <b4> <input_file> <b11>")
def fonk6(argv):
    b13, b5, b4, input_file, b11 = fonk4(argv)
    fonk3(b13, b5, b4, input_file, b11)
if b14 = = "__main__":
    fonk6(sys.argv[1:])