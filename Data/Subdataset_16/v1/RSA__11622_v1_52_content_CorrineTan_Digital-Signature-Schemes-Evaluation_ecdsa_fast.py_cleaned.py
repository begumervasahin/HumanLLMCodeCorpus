import hashlib
import logging
import sys
import time
from fastecdsa import curve, keys, ecdsa
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
    b2 = sys.argv[1]
    b3 = curve.secp256k1
    b4 = hashlib.sha256
    a1 = 0
    a2 = 0
    a3 = 0
    logging.info("Started Fast ECDSA with curve: %b10, sha: %b10", b3, str(b4.b14))
    with open(b2, "r") as f:
        b5 = time.time()
        for b6 in f:
            b6 = b6.strip()
            logging.debug(b6)
            b7 = time.time()
            private_key, b8 = keys.gen_keypair(b3)
            a1 += time.time() - b7
            b9 = time.time()
            r, b10 = ecdsa.sign(b6, private_key, curve=b3, hashfunc=b4)
            a2 += time.time() - b9
            b11 = time.time()
            b12 = ecdsa.verify((r, b10), b6, b8, curve=b3, hashfunc=b4)
            logging.debug("Verified: %b10" % b12)
            a3 += time.time() - b11
    b13 = a1 + a2 + a3
    logging.info("Total time cost for generating key is: %b10 b10", a1)
    logging.info("Total time cost for signing the message is: %b10 b10", a2)
    logging.info("Total time cost for verifying the message is: %b10 b10", a3)
    logging.info("Total time cost for key generating, message signing and verifying: %b10 b10", b13)
    logging.info("Total time cost for system time: %b10 b10", time.time() - b5)
if b14 = = "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <b2>")
    else:
        fonk1()