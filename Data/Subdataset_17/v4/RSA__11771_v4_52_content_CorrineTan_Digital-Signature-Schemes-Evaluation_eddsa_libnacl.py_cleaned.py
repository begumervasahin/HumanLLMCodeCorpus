import hashlib
import logging
import sys
import time
import libnacl.sign
def main():
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) < 2:
        logging.error("Please provide a filename as an argument.")
        sys.exit(1)
    filename = sys.argv[1]
    key_time = 0
    sign_time = 0
    verify_time = 0
    logging.info("Started libnacl libsodium Ed25519 operations")
    with open(filename, "r") as f:
        start = time.time()
        for message in f:
            logging.debug(message.strip())
            start_keygen = time.time()
            private_key = libnacl.sign.Signer()
            public_key = libnacl.sign.Verifier(private_key.hex_vk())
            key_time += time.time() - start_keygen
            start_sign = time.time()
            signed_message = private_key.sign(message.encode())
            sign_time += time.time() - start_sign
            signature = private_key.signature(message.encode())
            start_verify = time.time()
            try:
                public_key.verify(signature + message.encode())
                logging.debug("Verified: True")
            except ValueError as e:
                logging.warning("ValueError: %s", e)
                sys.exit(1)
            verify_time += time.time() - start_verify
    sum_time = key_time + sign_time + verify_time
    logging.info(f"Total time cost for generating key: {key_time:.6f} s")
    logging.info(f"Total time cost for signing the message: {sign_time:.6f} s")
    logging.info(f"Total time cost for verifying the message: {verify_time:.6f} s")
    logging.info(f"Total time cost for key generation, message signing, and verifying: {sum_time:.6f} s")
    logging.info(f"Total system time: {time.time() - start:.6f} s")
if __name__ == "__main__":
    main()