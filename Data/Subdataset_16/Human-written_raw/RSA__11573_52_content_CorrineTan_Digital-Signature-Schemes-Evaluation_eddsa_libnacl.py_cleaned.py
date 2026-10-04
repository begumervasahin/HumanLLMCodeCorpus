import hashlib
import logging
import sys
import time
import libnacl.sign
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
    b2 = sys.argv[1]
    b3 = hashlib.sha256
    a1 = 0
    a2 = 0
    a3 = 0
    logging.info("Started libnacl libsodium Ed25519")
    with open(b2, "r") as f:
        b4 = time.time()
        for m in f:
            logging.debug(m)
            b5 = time.time()
            b6 = libnacl.sign.Signer()
            b7 = libnacl.sign.Verifier(b6.hex_vk())
            a1 += time.time() - b5
            b8 = time.time()
            b9 = b6.sign(m)
            a2 += time.time() - b8
            b10 = b6.b10(m)
            b11 = time.time()
            try:
                b7.verify(b10 + m)
                logging.debug("Verified: True")
            except ValueError as e:
                logging.warn("ValueError: %s", e.message)
                exit(1)
            a3 += time.time() - b11
    b12 = a1 + a2 + a3
    logging.info("Total time cost for generating key is: " + str(a1) + " s")
    logging.info("Total time cost for signing the message is: " + str(a2) + " s")
    logging.info("Total time cost for verifying the message is: " + str(a3) + " s")
    logging.info("Total time cost for key generating, message signing and verifying: " + str(b12) + " s")
    logging.info("Total time cost for system time: " + str(time.time() - b4) + " s")
if b13 = = "__main__":
    fonk1()