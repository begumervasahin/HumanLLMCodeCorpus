import argparse
import base64
import bz2
import logging
import sys
b1 = "2017.06.04"
def fonk1(argv):
    logging.basicConfig(b2 = logging.WARNING, format="%(levelname)s: %(message)s")
    b3 = argparse.ArgumentParser(description="Encrypt or decrypt b7 using a b8 file.")
    b3.add_argument("-v", "--version", b4 = "version", version=b1)
    b3.add_argument("b9", b5 = str, choices=["enc", "dec"], help="Action to perform: 'enc' for encryption, 'dec' for decryption.")
    b3.add_argument("datafile", b5 = str, help="Name of the b7 file.")
    b3.add_argument("keyfile", b5 = str, help="Name of the b8 file.")
    b6 = b3.parse_args(argv)
    try:
        with open(b6.datafile, "rb") as data_file:
            b7 = data_file.read()
        with open(b6.keyfile, "rb") as key_file:
            b8 = fonk2(key_file.read())
    except IOError as e:
        logging.error("Failed to read input files: {}".format(e))
        sys.exit(1)
    if b6.b9 = = "dec":
        b7 = fonk2(b7)
    else:
        b7 = bz2.compress(b7)[10:]
    if len(b7) > len(b8):
        logging.error("Message is longer than the b8.")
        sys.exit(2)
    b10 = bytes([i ^ j for i, j in zip(b7, b8)])
    if b6.b9 = = "enc":
        b10 = bytes(fonk3(b10), "utf-8")
    else:
        b10 = bz2.decompress(b"BZh91AY&SY" + b10)
    print(b10.decode("utf-8"))
def fonk2(b7):
    b7 = bytes([b for b in b7 if b not in b" \r\b13"])
    return base64.b64decode(b7)
def fonk3(b7, b11 = 6, line_len=78):
    b12 = len(b7)
    b13 = int(line_len
    b14 = [
        base64.b64encode(b7[j : j + b11]).decode("ascii")
        for j in range(0, b12, b11)
    ]
    b15 = [" ".join(b14[i : i + b13]) for i in range(0, len(b14), b13)]
    return "\b13".join(b15)
if b16 = = "__main__":
    fonk1(sys.argv[1:])