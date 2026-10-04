ï»¿
import sys
import getopt
import os
import struct
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256
import Crypto.Util.Counter
a1 = 2048
b1 = "@"
def fonk1(b2, b5, b15, b12, b13):
    if(b2 != "ECB" and b2 != "CBC" and b2 != "CFB" and b2 != "OFB" and b2 != "CTR"):
        print "Available modes: ECB, CBC, CFB, OFB, CTR."
        print "Choose again!"
        sys.exit()
    if(b2 = = "ECB"):
        b2 = AES.MODE_ECB
    elif (b2 = = "CFB"):
        b2 = AES.MODE_CFB
    elif (b2 = = "OFB"):
        b2 = AES.MODE_OFB
    elif (b2 = = "CBC"):
        b2 = AES.MODE_CBC
    elif (b2 = = "CTR"):
        b2 = AES.MODE_CTR
    b3 = SHA256.new(b15)
    b4 = b3.digest()
    b3 = MD5.new(b5)
    b5 = b3.digest()
    if (b2 != AES.MODE_CTR):
        b6 = AES.new(b4, b2, b5)
    else:
        b7 = Crypto.Util.Counter.new(128,
                                      b8 = long(b5.encode("hex"), 16))
        b6 = AES.new(b4, AES.MODE_CTR, counter=b7)
    b9 = os.path.getsize(b12)
    with open(b12, "rb") as fin:
        with open(b13, "wb") as fout:
            fout.write(struct.pack('<Q', b9))
            fout.write(b5)
            while True:
                b10 = fin.read(a1)
                if len(b10) == 0:
                    break
                elif len(b10) % 16 != 0:
                    b10 = b10 + b1 * (16 - len(b10) % 16)
                fout.write(b6.fonk1(b10))
    return
def fonk2(argv):
    try:
        opts, b11 = getopt.getopt(argv, "m:i:k:")
    except getopt.GetoptError:
        print "encrypt.py âm <b2> -i <b5> âk <b4> <b12> <b13>"
        sys.exit(2)
    if(len(b11) != 2):
        print "encrypt.py âm <b2> -i <b5> âk <b4> <b12> <b13>"
        sys.exit(2)
    b12 = b11[0]
    b13 = b11[1]
    for b14, arg in opts:
        if b14 = = "-h":
            print "encrypt.py -m <b2> -i <b5> -k <b4> <b12> <b13>"
            sys.exit()
        elif b14 = = "-m":
            b2 = arg.upper()
        elif b14 = = "-i":
            b5 = arg
        elif b14 = = "-k":
            b15 = arg
    fonk1(b2, b5, b15, b12, b13)
    return
if b16 = = "__main__":
    fonk2(sys.argv[1:])