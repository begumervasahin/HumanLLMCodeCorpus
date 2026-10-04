import hashlib
import logging
import sys
import time
import libnacl.sign
def main():
    logging.basicConfig(level=logging.INFO)
    filename = sys.argv[1]
    key_time = 0
    sign_time = 0
    verify_time = 0
    logging.info("Started libnacl libsodium Ed25519")
    with open(filename, "r") as f:
        start = time.time()
        for m in f:
            m = m.strip().encode()
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
                logging.warning("ValueError: %s", e)
                exit(1)
            verify_time += time.time() - start_verify
    sum_time = key_time + sign_time + verify_time
    logging.info("Total time cost for generating key is: %s s", key_time)
    logging.info("Total time cost for signing the message is: %s s", sign_time)
    logging.info("Total time cost for verifying the message is: %s s", verify_time)
    logging.info("Total time cost for key generating, message signing and verifying: %s s", sum_time)
    logging.info("Total time cost for system time: %s s", time.time() - start)
if __name__ == "__main__":
    main()