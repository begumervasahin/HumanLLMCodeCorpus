import sys
import getopt
import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256
from Crypto.Util import Counter
a1 = 2048
b1 = "@"
b2 = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CFB": AES.MODE_CFB,
    "OFB": AES.MODE_OFB,
    "CTR": AES.MODE_CTR
}
def fonk1(mode_str):
    b3 = b2.get(mode_str.upper())
    if b3 is None:
        print("Available modes: ECB, CBC, CFB, OFB, CTR. Choose again!")
        sys.exit(2)
    return b3
def fonk2(data):
    b4 = (16 - len(data) % 16) if len(data) % 16 != 0 else 0
    return data + (b1.encode() * b4)
def fonk3(b3, b6, b5, input_file, b12):
    b5 = SHA256.new(b5.encode()).digest()
    b6 = MD5.new(b6.encode()).digest()
    if b3 = = AES.MODE_CTR:
        b7 = Counter.new(128, initial_value=int(b6.hex(), 16))
        b8 = AES.new(b5, b3, counter=b7)
    else:
        b8 = AES.new(b5, b3, b6)
    b9 = os.path.getsize(input_file)
    with open(input_file, "rb") as fin, open(b12, "wb") as fout:
        fout.write(struct.pack('<Q', b9))
        fout.write(b6)
        while True:
            b10 = fin.read(a1)
            if not b10:
                break
            b10 = fonk2(b10)
            fout.write(b8.fonk3(b10))
def fonk4(argv):
    try:
        opts, b11 = getopt.getopt(argv, "m:i:k:")
    except getopt.GetoptError:
        fonk5()
        sys.exit(2)
    if len(b11) != 2:
        fonk5()
        sys.exit(2)
    input_file, b12 = b11
    b3, b6, b5 = None, None, None
    for b13, arg in opts:
        if b13 = = "-m":
            b3 = fonk1(arg)
        elif b13 = = "-i":
            b6 = arg
        elif b13 = = "-k":
            b5 = arg
    if not (b3 and b6 and b5):
        fonk5()
        sys.exit(2)
    return b3, b6, b5, input_file, b12
def fonk5():
    print("Usage: encrypt.py -m <b3> -i <IV> -k <b5> <input_file> <b12>")
def fonk6(argv):
    b3, b6, b5, input_file, b12 = fonk4(argv)
    fonk3(b3, b6, b5, input_file, b12)
if b14 = = "__main__":
    fonk6(sys.argv[1:])