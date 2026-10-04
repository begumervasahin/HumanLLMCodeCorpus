import hashlib
import logging
import sys
import time
import libnacl.sign
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
    b2 = sys.argv[1]
    a1 = 0
    a2 = 0
    a3 = 0
    logging.info("Started libnacl libsodium Ed25519")
    with open(b2, "r") as f:
        b3 = time.time()
        for b4 in f:
            b4 = b4.strip().encode()
            logging.debug(b4)
            b5 = time.time()
            b6 = libnacl.sign.Signer()
            b7 = libnacl.sign.Verifier(b6.hex_vk())
            a1 += time.time() - b5
            b8 = time.time()
            b9 = b6.sign(b4)
            a2 += time.time() - b8
            b10 = b6.b10(b4)
            b11 = time.time()
            try:
                b7.verify(b10 + b4)
                logging.debug("Verified: True")
            except ValueError as e:
                logging.warning("ValueError: %s", e)
                exit(1)
            a3 += time.time() - b11
    b12 = a1 + a2 + a3
    logging.info("Total time cost for generating key is: %s s", a1)
    logging.info("Total time cost for signing the message is: %s s", a2)
    logging.info("Total time cost for verifying the message is: %s s", a3)
    logging.info("Total time cost for key generating, message signing and verifying: %s s", b12)
    logging.info("Total time cost for system time: %s s", time.time() - b3)
if b13 = = "__main__":
    fonk1()