import hashlib
import logging
import sys
import time
import libnacl.sign
def main():
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) < 2:
        logging.error("Please provide the filename as a command-line argument.")
        sys.exit(1)
    filename = sys.argv[1]
    key_time = 0
    sign_time = 0
    verify_time = 0
    logging.info("Started libnacl libsodium Ed25519")
    with open(filename, "r") as f:
        start = time.time()
        for line in f:
            message = line.strip().encode()
            logging.debug(message)
            start_keygen = time.time()
            private_key = libnacl.sign.Signer()
            public_key = libnacl.sign.Verifier(private_key.hex_vk())
            key_time += time.time() - start_keygen
            start_sign = time.time()
            signed_message = private_key.sign(message)
            sign_time += time.time() - start_sign
            signature = private_key.signature(message)
            start_verify = time.time()
            try:
                public_key.verify(signature + message)
                logging.debug("Verified: True")
            except ValueError as e:
                logging.warning("Verification failed: %s", e)
                sys.exit(1)
            verify_time += time.time() - start_verify
    total_time = time.time() - start
    logging.info("Total time cost for key generation: %s s", key_time)
    logging.info("Total time cost for signing the message: %s s", sign_time)
    logging.info("Total time cost for verifying the message: %s s", verify_time)
    logging.info("Total time cost for key generation, message signing, and verifying: %s s", key_time + sign_time + verify_time)
    logging.info("Total time cost for system: %s s", total_time)
if __name__ == "__main__":
    main()