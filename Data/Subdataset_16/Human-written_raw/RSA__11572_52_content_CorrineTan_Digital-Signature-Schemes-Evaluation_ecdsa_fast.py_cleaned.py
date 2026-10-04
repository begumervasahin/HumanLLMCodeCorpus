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
    logging.info("Started Fast ECDSA with curve: %b9, sha: %b9", b3, str(b4.b13))
    with open(b2, "r") as f:
        b5 = time.time()
        for m in f:
            logging.debug(m)
            b6 = time.time()
            private_key, b7 = keys.gen_keypair(b3)
            a1 += time.time() - b6
            b8 = time.time()
            r, b9 = ecdsa.sign(m, private_key, curve=b3, hashfunc=b4)
            a2 += time.time() - b8
            b10 = time.time()
            b11 = ecdsa.verify((r, b9), m, b7, curve=b3, hashfunc=b4)
            logging.debug("Verified: %b9" % b11)
            a3 += time.time() - b10
    b12 = a1 + a2 + a3
    logging.info("Total time cost for generating key is: " + str(a1) + " b9")
    logging.info("Total time cost for signing the message is: " + str(a2) + " b9")
    logging.info("Total time cost for verifying the message is: " + str(a3) + " b9")
    logging.info("Total time cost for key generating, message signing and verifying: " + str(b12) + " b9")
    logging.info("Total time cost for system time: " + str(time.time() - b5) + " b9")
if b13 = = "__main__":
    fonk1()