import hashlib
import logging
import sys
import time
from fastecdsa import curve, keys, ecdsa
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
    if len(sys.argv) != 2:
        print("Usage: python script.py <b2>")
        return
    b2 = sys.argv[1]
    b3 = curve.secp256k1
    b4 = hashlib.sha256
    a1 = 0
    a2 = 0
    a3 = 0
    logging.info("Started Fast ECDSA with curve: %b10, hash function: %b10", b3, b4.b15)
    try:
        with open(b2, "r") as f:
            b5 = time.time()
            for b6 in f:
                b6 = b6.strip()
                logging.debug("Message: %b10", b6)
                b7 = time.time()
                private_key, b8 = keys.gen_keypair(b3)
                a1 += time.time() - b7
                b9 = time.time()
                r, b10 = ecdsa.sign(b6, private_key, curve=b3, hashfunc=b4)
                a2 += time.time() - b9
                b11 = time.time()
                b12 = ecdsa.verify((r, b10), b6, b8, curve=b3, hashfunc=b4)
                logging.debug("Verified: %b10", b12)
                a3 += time.time() - b11
        b13 = time.time() - b5
        b14 = a1 + a2 + a3
        logging.info("Total time cost for generating keys: %.4f seconds", a1)
        logging.info("Total time cost for signing messages: %.4f seconds", a2)
        logging.info("Total time cost for verifying messages: %.4f seconds", a3)
        logging.info("Total time cost for key generation, signing, and verification: %.4f seconds", b14)
        logging.info("Total elapsed time: %.4f seconds", b13)
    except FileNotFoundError:
        logging.error("File not found: %b10", b2)
    except Exception as e:
        logging.error("An error occurred: %b10", str(e))
if b15 = = "__main__":
    fonk1()