import hashlib
import logging
import sys
import time
import libnacl.sign
def main():
    logging.basicConfig(level=logging.INFO)
    filename = sys.argv[1]
    param_hash = hashlib.sha256
    key_time = 0
    sign_time = 0
    verify_time = 0
    logging.info("Started libnacl libsodium Ed25519")
    with open(filename, "r") as f:
        start = time.time()
        for m in f:
            logging.debug(m)
            start_keygen = time.time()
            private_key = libnacl.sign.Signer()
            public_key = libnacl.sign.Verifier(private_key.hex_vk())
            key_time += time.time() - start_keygen
            start_sign = time.time()
            signed = private_key.sign(m)
            sign_time += time.time() - start_sign
            signature = private_key.signature(m)
            start_verify = time.time()
            try:
                public_key.verify(signature + m)
                logging.debug("Verified: True")
            except ValueError as e:
                logging.warn("ValueError: %s", e.message)
                exit(1)
            verify_time += time.time() - start_verify
    sum_time = key_time + sign_time + verify_time
    logging.info("Total time cost for generating key is: " + str(key_time) + " s")
    logging.info("Total time cost for signing the message is: " + str(sign_time) + " s")
    logging.info("Total time cost for verifying the message is: " + str(verify_time) + " s")
    logging.info("Total time cost for key generating, message signing and verifying: " + str(sum_time) + " s")
    logging.info("Total time cost for system time: " + str(time.time() - start) + " s")
if __name__ == "__main__":
    main()