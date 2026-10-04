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
def fonk2(hash_mode_str, input_file, signature_file, b12):
    print(f"Hash mode: {hash_mode_str}")
    b4 = fonk1(hash_mode_str)
    b5 = b4.new()
    with open(input_file, "rb") as f:
        while block := f.read(b1):
            b5.update(block)
    with open(signature_file, "rb") as f:
        b6 = f.read()
    print(f"Signature retrieved: {b6}")
    if not os.path.isfile(b12):
        print("Public key doesn't exist... Task failed.")
        return False
    with open(b12, "r") as f:
        b7 = RSA.importKey(f.read())
    b8 = PKCS1_v1_5.new(b7)
    b9 = b8.verify(b5, b6)
    print(f"Verification b9: {b9}")
    return b9
def fonk3(argv):
    try:
        opts, b10 = getopt.getopt(argv, "h:")
    except getopt.GetoptError:
        fonk4()
        sys.exit(2)
    b4 = None
    for b11, arg in opts:
        if b11 = = "-h":
            b4 = arg
    if not b4 or len(b10) != 3:
        fonk4()
        sys.exit(2)
    return b4, b10[0], b10[1], b10[2]
def fonk4():
    print("Usage: very_sign.py -h <hash> <input_file> <signature_file> <b12>")
def fonk5(argv):
    b4, input_file, signature_file, b12 = fonk3(argv)
    b9 = fonk2(b4, input_file, signature_file, b12)
    print(f"Verify b9: {b9}")
    return b9
if b13 = = "__main__":
    fonk5(sys.argv[1:])