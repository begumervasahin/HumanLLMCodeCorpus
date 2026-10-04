import hashlib
import logging
import sys
import time
import libnacl.sign
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
    if len(sys.argv) < 2:
        logging.error("Please provide a b2 as an argument.")
        sys.exit(1)
    b2 = sys.argv[1]
    a1 = 0
    a2 = 0
    a3 = 0
    logging.info("Started libnacl libsodium Ed25519 operations")
    with open(b2, "r") as f:
        b3 = time.time()
        for message in f:
            logging.debug(message.strip())
            b4 = time.time()
            b5 = libnacl.sign.Signer()
            b6 = libnacl.sign.Verifier(b5.hex_vk())
            a1 += time.time() - b4
            b7 = time.time()
            b8 = b5.sign(message.encode())
            a2 += time.time() - b7
            b9 = b5.b9(message.encode())
            b10 = time.time()
            try:
                b6.verify(b9 + message.encode())
                logging.debug("Verified: True")
            except ValueError as e:
                logging.warning("ValueError: %s", e)
                sys.exit(1)
            a3 += time.time() - b10
    b11 = a1 + a2 + a3
    logging.info(f"Total time cost for generating key: {a1:.6f} s")
    logging.info(f"Total time cost for signing the message: {a2:.6f} s")
    logging.info(f"Total time cost for verifying the message: {a3:.6f} s")
    logging.info(f"Total time cost for key generation, message signing, and verifying: {b11:.6f} s")
    logging.info(f"Total system time: {time.time() - b3:.6f} s")
if b12 = = "__main__":
    fonk1()