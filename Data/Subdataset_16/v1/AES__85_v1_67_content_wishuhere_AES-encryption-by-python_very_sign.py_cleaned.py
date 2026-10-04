import sys
import getopt
import os
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto import Random
b1 = 1024 * 1024
b2 = {
    "SHA256": SHA256,
    "MD5": MD5,
    "SHA": SHA,
    "SHA1": SHA,
    "SHA-1": SHA
}
def fonk1(b4):
    b3 = b2.get(b4.upper())
    if b3 is None:
        print("Available modes: SHA256, MD5, SHA.")
        sys.exit(2)
    return b3
def fonk2(b4, input_file, sign_file, b13):
    b4 = fonk1(b4)
    b5 = b4.new()
    with open(input_file, "rb") as fin:
        while True:
            b6 = fin.read(b1)
            if not b6:
                break
            b5.update(b6)
    with open(sign_file, "rb") as fin2:
        b7 = fin2.read()
    if os.path.isfile(b13):
        with open(b13, "r") as fin3:
            b8 = RSA.importKey(fin3.read())
    else:
        print("Public key doesn't exist... Task failed.")
        return False
    b9 = PKCS1_v1_5.new(b8)
    b10 = b9.verify(b5, b7)
    return b10
def fonk3(argv):
    try:
        opts, b11 = getopt.getopt(argv, "h:")
    except getopt.GetoptError:
        fonk4()
        sys.exit(2)
    b4 = None
    for b12, arg in opts:
        if b12 = = "-h":
            b4 = arg
    if not b4 or len(b11) != 3:
        fonk4()
        sys.exit(2)
    return b4, b11[0], b11[1], b11[2]
def fonk4():
    print("Usage: very_sign.py -h <hash> <input_file> <sign_file> <b13>")
def fonk5(argv):
    b4, input_file, sign_file, b13 = fonk3(argv)
    b10 = fonk2(b4, input_file, sign_file, b13)
    print("Verify b10:", b10)
    return b10
if b14 = = "__main__":
    fonk5(sys.argv[1:])