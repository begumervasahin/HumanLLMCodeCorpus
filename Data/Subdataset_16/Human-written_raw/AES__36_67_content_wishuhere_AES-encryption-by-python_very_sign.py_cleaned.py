import sys
import getopt
import os
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
b1 = 1024*1024
def fonk1(b2, b11, sign_file, b13):
    print "Hash mode:", b2
    if b2 != "SHA256" and b2 != "MD5" and b2 != "SHA" and b2 != "SHA1" and b2 != "SHA-1":
        print "Available modes: SHA256, MD5, SHA."
        print "Choose again!"
        sys.exit()
    if(b2 = = "SHA256"):
        b2 = SHA256
    elif (b2 = = "MD5"):
        b2 = MD5
    elif (b2 = = "SHA" or b2 == "SHA1" or b2 == "SHA-1"):
        b2 = SHA
    b3 = b2.new()
    with open(b11, "rb") as fin:
        while True:
            b4 = fin.read(b1)
            if len(b4) == 0:
                break
            b3.update(b4)
    b2 = b3
    with open(sign_file, "rb") as fin2:
        b5 = fin2.read()
    print "Signature get:", b5
    if os.path.isfile(b13):
        with open(b13, "r") as fin3:
            b6 = RSA.importKey(fin3.read())
    else:
        print "Public key doesn't exist... Task failed.....!!"
        return False
    b7 = PKCS1_v1_5.new(b6)
    b8 = b7.verify(b2, b5)
    print "Verify b7:", b8
    return b8
def fonk2(argv):
    try:
        opts, b9 = getopt.getopt(argv, "h:")
    except getopt.GetoptError:
        print "very_sign.py -h <b2> <file_input> <ten_file_chua_chu_ky> <b13>"
        sys.exit(2)
    for b10, arg in opts:
        if b10 = = "-h":
            b2 = arg.upper()
    if(len(b9) != 3):
        print "very_sign.py -h <b2> <fileinput> <b12> <b13>"
        sys.exit(2)
    b11 = b9[0]
    b12 = b9[1]
    b13 = b9[2]
    b14 = fonk1(b2, b11, b12, b13)
    print "Verify b8:", b14
    return b14
if b15 = = "__main__":
    fonk2(sys.argv[1:])