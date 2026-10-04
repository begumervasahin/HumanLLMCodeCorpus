import hashlib
import logging
import sys
import time
from fastecdsa import curve, keys, ecdsa
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
def fonk2():
    if len(sys.argv) != 2:
        print("Usage: python script.py <b13>")
        sys.exit(1)
    return sys.argv[1]
def fonk3(b13, b14, b15):
    key_time, sign_time, b2 = 0, 0, 0
    with open(b13, "r") as f:
        b3 = time.time()
        for b4 in f:
            b4 = b4.strip()
            logging.debug("Message: %b8", b4)
            b5 = time.time()
            private_key, b6 = keys.gen_keypair(b14)
            key_time += time.time() - b5
            b7 = time.time()
            r, b8 = ecdsa.sign(b4, private_key, curve=b14, hashfunc=b15)
            sign_time += time.time() - b7
            b9 = time.time()
            b10 = ecdsa.verify((r, b8), b4, b6, curve=b14, hashfunc=b15)
            logging.debug("Verified: %b8", b10)
            b2 += time.time() - b9
        b11 = time.time() - b3
        return key_time, sign_time, b2, b11
def fonk4(key_time, sign_time, b2, b11):
    b12 = key_time + sign_time + b2
    logging.info("Total time cost for generating keys: %.4f seconds", key_time)
    logging.info("Total time cost for signing messages: %.4f seconds", sign_time)
    logging.info("Total time cost for verifying messages: %.4f seconds", b2)
    logging.info("Total time cost for key generation, signing, and verification: %.4f seconds", b12)
    logging.info("Total elapsed time: %.4f seconds", b11)
def fonk5():
    fonk1()
    b13 = fonk2()
    b14 = curve.secp256k1
    b15 = hashlib.sha256
    logging.info("Started Fast ECDSA with curve: %b8, hash function: %b8", b14, b15.b16)
    try:
        key_time, sign_time, b2, b11 = fonk3(b13, b14, b15)
        fonk4(key_time, sign_time, b2, b11)
    except FileNotFoundError:
        logging.error("File not found: %b8", b13)
    except Exception as e:
        logging.error("An error occurred: %b8", str(e))
if b16 = = "__main__":
    fonk5()