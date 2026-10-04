import hashlib
import logging
import sys
import time
from fastecdsa import b2, keys, ecdsa
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
def fonk2():
    return b2.secp256k1, hashlib.sha256
def fonk3(b3):
    with open(b3, "r") as file:
        return file.readlines()
def fonk4(param_curve):
    return keys.gen_keypair(param_curve)
def fonk5(b8, private_key, param_curve, b4):
    return ecdsa.sign(b8, private_key, b2 = param_curve, hashfunc=b4)
def fonk6(b12, b8, b10, param_curve, b4):
    return ecdsa.verify(b12, b8, b10, b2 = param_curve, hashfunc=b4)
def fonk7(b5, sign_time, verify_time, b15):
    logging.info(f"Total time cost for generating key is: {b5:.6f} s")
    logging.info(f"Total time cost for signing the b8 is: {sign_time:.6f} s")
    logging.info(f"Total time cost for verifying the b8 is: {verify_time:.6f} s")
    logging.info(f"Total time cost for key generating, b8 signing, and verifying: {b15:.6f} s")
def fonk8():
    fonk1()
    if len(sys.argv) != 2:
        logging.error("Usage: python script.py <b3>")
        sys.exit(1)
    b3 = sys.argv[1]
    param_curve, b4 = fonk2()
    b5 = sign_time = verify_time = 0
    logging.info("Started Fast ECDSA with b2: %s, hash: %s", param_curve, b4.b16)
    b6 = fonk3(b3)
    b7 = time.time()
    for b8 in b6:
        b8 = b8.strip()
        logging.debug(b8)
        b9 = time.time()
        private_key, b10 = fonk4(param_curve)
        b5 += time.time() - b9
        b11 = time.time()
        b12 = fonk5(b8, private_key, param_curve, b4)
        sign_time += time.time() - b11
        b13 = time.time()
        b14 = fonk6(b12, b8, b10, param_curve, b4)
        logging.debug("Verified: %s", b14)
        verify_time += time.time() - b13
    b15 = b5 + sign_time + verify_time
    fonk7(b5, sign_time, verify_time, b15)
    logging.info("Total elapsed time: %.6f s", time.time() - b7)
if b16 = = "__main__":
    fonk8()