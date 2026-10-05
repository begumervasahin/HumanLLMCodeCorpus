import argparse
import base64
import bz2
import logging
import sys
b1 = "2017.06.04"
def fonk1(argv):
    fonk2()
    b2 = fonk3(argv)
    b8, b3 = fonk4(b2.datafile, b2.keyfile)
    fonk5(b2, b8, b3)
def fonk2():
    logging.basicConfig(b4 = logging.WARNING, format="%(levelname)s: %(message)s")
def fonk3(argv):
    b5 = argparse.ArgumentParser(description="Encrypt or decrypt b8 using a b3 file.")
    b5.add_argument("-v", "--version", b6 = "version", version=b1)
    b5.add_argument("b9", b7 = str, choices=["enc", "dec"], help="Action to perform: 'enc' for encryption, 'dec' for decryption.")
    b5.add_argument("datafile", b7 = str, help="Name of the b8 file.")
    b5.add_argument("keyfile", b7 = str, help="Name of the b3 file.")
    return b5.parse_args(argv)
def fonk4(datafile, keyfile):
    try:
        with open(datafile, "rb") as data_file:
            b8 = data_file.read()
        with open(keyfile, "rb") as key_file:
            b3 = fonk6(key_file.read())
    except IOError as e:
        logging.error("Failed to read input files: {}".format(e))
        sys.exit(1)
    return b8, b3
def fonk5(b2, b8, b3):
    if b2.b9 = = "dec":
        b8 = fonk6(b8)
    else:
        b8 = fonk7(b8)
    if len(b8) > len(b3):
        logging.error("Message is longer than the b3.")
        sys.exit(2)
    b10 = bytes([i ^ j for i, j in zip(b8, b3)])
    if b2.b9 = = "enc":
        b10 = bytes(fonk9(b10), "utf-8")
    else:
        b10 = fonk8(b10)
    print(b10.decode("utf-8"))
def fonk6(b8):
    b8 = bytes([b for b in b8 if b not in b" \r\b13"])
    return base64.b64decode(b8)
def fonk7(b8):
    return bz2.compress(b8)[10:]
def fonk8(b8):
    return bz2.decompress(b"BZh91AY&SY" + b8)
def fonk9(b8, b11 = 6, line_len=78):
    b12 = len(b8)
    b13 = int(line_len
    b14 = [
        base64.b64encode(b8[j : j + b11]).decode("ascii")
        for j in range(0, b12, b11)
    ]
    b15 = [" ".join(b14[i : i + b13]) for i in range(0, len(b14), b13)]
    return "\b13".join(b15)
if b16 = = "__main__":
    fonk1(sys.argv[1:])