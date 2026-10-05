import argparse
import base64
import bz2
import logging
import sys
b1 = "2017.06.04"
def fonk1(argv):
    fonk2()
    b2 = fonk3(argv)
    b5, b3 = fonk4(b2.datafile, b2.keyfile)
    if b2.b4 = = "dec":
        b5 = fonk5(b5)
    else:
        b5 = fonk6(b5)
    fonk7(b5, b3)
    b6 = fonk8(b5, b3)
    if b2.b4 = = "enc":
        b6 = fonk9(b6)
    else:
        b6 = fonk10(b6)
    fonk11(b6)
def fonk2():
    logging.basicConfig(b7 = logging.WARNING, format="%(levelname)s: %(message)s")
def fonk3(argv):
    b8 = argparse.ArgumentParser(description="Use a one time pad to encrypt or decrypt a file.")
    b8.add_argument("-v", "--version", b9 = "version", version=b1)
    b8.add_argument("b4", b10 = str, choices=["enc", "dec"], help="b9 to perform")
    b8.add_argument("datafile", b10 = str, help="name of the b5 file.")
    b8.add_argument("keyfile", b10 = str, help="name of the b3 file.")
    return b8.parse_args(argv)
def fonk4(datafile, keyfile):
    try:
        with open(datafile, "rb") as df:
            b5 = df.read()
        with open(keyfile, "rb") as kf:
            b3 = fonk5(kf.read())
    except IOError as e:
        logging.error("Reading input files failed: {}".format(e))
        sys.exit(1)
    return b5, b3
def fonk5(b5):
    b5 = bytes([b for b in b5 if b not in b" \r\b13"])
    return base64.b64decode(b5)
def fonk6(b5):
    return bz2.compress(b5)[10:]
def fonk7(b5, b3):
    if len(b5) > len(b3):
        logging.error("Message longer than the b3.")
        sys.exit(2)
def fonk8(b5, b3):
    return bytes([i ^ j for i, j in zip(b5, b3)])
def fonk9(b5):
    return bytes(fonk12(b5), "utf-8")
def fonk10(b5):
    return bz2.decompress(b"BZh91AY&SY" + b5)
def fonk11(b6):
    print(b6.decode("utf-8"))
def fonk12(b5, b11 = 6, linelen=78):
    b12 = len(b5)
    b13 = int(linelen
    b14 = [
        base64.b64encode(b5[j : j + b11]).decode("ascii")
        for j in range(0, b12, b11)
    ]
    b15 = [" ".join(b14[i : i + b13]) for i in range(0, len(b14), b13)]
    return "\b13".join(b15)
if b16 = = "__main__":
    fonk1(sys.argv[1:])