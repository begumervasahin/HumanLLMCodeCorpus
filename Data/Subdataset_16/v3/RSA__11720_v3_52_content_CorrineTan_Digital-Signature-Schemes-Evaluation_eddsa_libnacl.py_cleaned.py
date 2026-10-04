import hashlib
import logging
import sys
import time
import libnacl.sign
def fonk1():
    logging.basicConfig(b1 = logging.INFO)
def fonk2():
    if len(sys.argv) < 2:
        logging.error("Please provide the b4 as a command-line argument.")
        sys.exit(1)
def fonk3(b4):
    with open(b4, "r") as file:
        return [line.strip().encode() for line in file]
def fonk4():
    b2 = libnacl.sign.Signer()
    b3 = libnacl.sign.Verifier(b2.hex_vk())
    return b2, b3
def fonk5(key_time, sign_time, b5, b13):
    logging.info("Total time cost for key generation: %s s", key_time)
    logging.info("Total time cost for signing the message: %s s", sign_time)
    logging.info("Total time cost for verifying the message: %s s", b5)
    logging.info("Total time cost for key generation, message signing, and verifying: %s s", key_time + sign_time + b5)
    logging.info("Total time cost for system: %s s", b13)
def fonk6():
    fonk7()
    fonk8()
    b4 = sys.argv[1]
    key_time, sign_time, b5 = 0, 0, 0
    logging.info("Started libnacl libsodium Ed25519")
    b6 = fonk9(b4)
    b7 = time.time()
    for message in b6:
        logging.debug(message)
        b8 = time.time()
        b2, b3 = fonk10()
        key_time += time.time() - b8
        b9 = time.time()
        b10 = b2.sign(message)
        sign_time += time.time() - b9
        b11 = b2.b11(message)
        b12 = time.time()
        try:
            b3.verify(b11 + message)
            logging.debug("Verified: True")
        except ValueError as e:
            logging.warning("Verification failed: %s", e)
            sys.exit(1)
        b5 += time.time() - b12
    b13 = time.time() - b7
    fonk11(key_time, sign_time, b5, b13)
if b14 = = "__main__":
    fonk12()
import hashlib
import logging
import sys
import time
import libnacl.sign
def fonk7():
    logging.basicConfig(b1 = logging.INFO)
def fonk8():
    if len(sys.argv) < 2:
        logging.error("Please provide the b4 as a command-line argument.")
        sys.exit(1)
def fonk9(b4):
    with open(b4, "r") as file:
        return [line.strip().encode() for line in file]
def fonk10():
    b2 = libnacl.sign.Signer()
    b3 = libnacl.sign.Verifier(b2.hex_vk())
    return b2, b3
def fonk11(key_time, sign_time, b5, b13):
    logging.info("Total time cost for key generation: %s s", key_time)
    logging.info("Total time cost for signing the message: %s s", sign_time)
    logging.info("Total time cost for verifying the message: %s s", b5)
    logging.info("Total time cost for key generation, message signing, and verifying: %s s", key_time + sign_time + b5)
    logging.info("Total time cost for system: %s s", b13)
def fonk12():
    fonk7()
    fonk8()
    b4 = sys.argv[1]
    key_time, sign_time, b5 = 0, 0, 0
    logging.info("Started libnacl libsodium Ed25519")
    b6 = fonk9(b4)
    b7 = time.time()
    for message in b6:
        logging.debug(message)
        b8 = time.time()
        b2, b3 = fonk10()
        key_time += time.time() - b8
        b9 = time.time()
        b10 = b2.sign(message)
        sign_time += time.time() - b9
        b11 = b2.b11(message)
        b12 = time.time()
        try:
            b3.verify(b11 + message)
            logging.debug("Verified: True")
        except ValueError as e:
            logging.warning("Verification failed: %s", e)
            sys.exit(1)
        b5 += time.time() - b12
    b13 = time.time() - b7
    fonk11(key_time, sign_time, b5, b13)
if b14 = = "__main__":
    fonk12()