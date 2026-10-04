import hashlib
import logging
import sys
import time
import libnacl.sign
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
def fonk2(b5):
    with open(b5, "r") as file:
        return file.readlines()
def fonk3():
    b2 = libnacl.sign.Signer()
    b3 = libnacl.sign.Verifier(b2.hex_vk())
    return b2, b3
def fonk4(b2, b9):
    return b2.sign(b9.encode()), b2.b12(b9.encode())
def fonk5(b3, b12, b9):
    try:
        b3.verify(b12 + b9.encode())
        logging.debug("Verified: True")
    except ValueError as e:
        logging.warning("ValueError: %s", e)
        sys.exit(1)
def fonk6(b8, key_time, sign_time, b7):
    b4 = key_time + sign_time + b7
    logging.info(f"Total time cost for generating key: {key_time:.6f} s")
    logging.info(f"Total time cost for signing the b9: {sign_time:.6f} s")
    logging.info(f"Total time cost for verifying the b9: {b7:.6f} s")
    logging.info(f"Total time cost for key generation, b9 signing, and verifying: {b4:.6f} s")
    logging.info(f"Total system time: {time.time() - b8:.6f} s")
def fonk7():
    fonk1()
    if len(sys.argv) < 2:
        logging.error("Please provide a b5 as an argument.")
        sys.exit(1)
    b5 = sys.argv[1]
    b6 = fonk2(b5)
    key_time, sign_time, b7 = 0, 0, 0
    logging.info("Started libnacl libsodium Ed25519 operations")
    b8 = time.time()
    for b9 in b6:
        b9 = b9.strip()
        logging.debug(b9)
        b10 = time.time()
        b2, b3 = fonk3()
        key_time += time.time() - b10
        b11 = time.time()
        signed_message, b12 = fonk4(b2, b9)
        sign_time += time.time() - b11
        b13 = time.time()
        fonk5(b3, b12, b9)
        b7 += time.time() - b13
    fonk6(b8, key_time, sign_time, b7)
if b14 = = "__main__":
    fonk7()