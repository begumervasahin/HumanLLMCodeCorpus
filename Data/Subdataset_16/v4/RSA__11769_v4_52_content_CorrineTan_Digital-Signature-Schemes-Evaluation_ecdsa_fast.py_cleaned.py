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
def fonk5(message, private_key, param_curve, b4):
    return ecdsa.sign(message, private_key, b2 = param_curve, hashfunc=b4)
def fonk6(b11, message, b9, param_curve, b4):
    return ecdsa.verify(b11, message, b9, b2 = param_curve, hashfunc=b4)
def fonk7(b5, sign_time, verify_time, b14):
    logging.info(f"Total time cost for generating key is: {b5:.6f} s")
    logging.info(f"Total time cost for signing the message is: {sign_time:.6f} s")
    logging.info(f"Total time cost for verifying the message is: {verify_time:.6f} s")
    logging.info(f"Total time cost for key generating, message signing and verifying: {b14:.6f} s")
def fonk8():
    fonk1()
    if len(sys.argv) != 2:
        logging.error("Usage: python script.py <b3>")
        sys.exit(1)
    b3 = sys.argv[1]
    param_curve, b4 = fonk2()
    b5 = sign_time = verify_time = 0
    logging.info("Started Fast ECDSA with b2: %s, hash: %s", param_curve, b4.b15)
    b6 = fonk3(b3)
    b7 = time.time()
    for message in b6:
        logging.debug(message.strip())
        b8 = time.time()
        private_key, b9 = fonk4(param_curve)
        b5 += time.time() - b8
        b10 = time.time()
        b11 = fonk5(message.strip(), private_key, param_curve, b4)
        sign_time += time.time() - b10
        b12 = time.time()
        b13 = fonk6(b11, message.strip(), b9, param_curve, b4)
        logging.debug("Verified: %s", b13)
        verify_time += time.time() - b12
    b14 = b5 + sign_time + verify_time
    fonk7(b5, sign_time, verify_time, b14)
    logging.info("Total elapsed time: %.6f s", time.time() - b7)
if b15 = = "__main__":
    fonk8()