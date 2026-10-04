import sys
import getopt
import os
from Crypto.Hash import SHA256, MD5, SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
b1 = 1024 * 1024
b2 = {
    "SHA256": SHA256,
    "MD5": MD5,
    "SHA": SHA,
    "SHA1": SHA,
    "SHA-1": SHA
}
def fonk1(hash_mode_str):
    b3 = b2.get(hash_mode_str.upper())
    if b3 is None:
        print("Available modes: SHA256, MD5, SHA.")
        sys.exit(2)
    return b3
def fonk2(hash_mode_str, input_file, signature_file, b11):
    b4 = fonk1(hash_mode_str)
    b5 = b4.new()
    with open(input_file, "rb") as f:
        while block := f.read(b1):
            b5.update(block)
    with open(signature_file, "rb") as f:
        b6 = f.read()
    if not os.path.isfile(b11):
        print("Public key doesn't exist... Task failed.")
        return False
    with open(b11, "r") as f:
        b7 = RSA.importKey(f.read())
    b8 = PKCS1_v1_5.new(b7)
    return b8.verify(b5, b6)
def fonk3(argv):
    try:
        opts, b9 = getopt.getopt(argv, "h:")
    except getopt.GetoptError:
        fonk4()
        sys.exit(2)
    b4 = None
    for b10, arg in opts:
        if b10 = = "-h":
            b4 = arg
    if not b4 or len(b9) != 3:
        fonk4()
        sys.exit(2)
    return b4, b9[0], b9[1], b9[2]
def fonk4():
    print("Usage: very_sign.py -h <hash> <input_file> <sign_file> <b11>")
def fonk5(argv):
    b4, input_file, signature_file, b11 = fonk3(argv)
    b12 = fonk2(b4, input_file, signature_file, b11)
    print("Verify b12:", b12)
    return b12
if b13 = = "__main__":
    fonk5(sys.argv[1:])