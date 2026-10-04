import hashlib
import logging
import sys
import time
import libnacl.sign
def configure_logging():
    logging.basicConfig(level=logging.INFO)
def validate_arguments():
    if len(sys.argv) < 2:
        logging.error("Please provide the filename as a command-line argument.")
        sys.exit(1)
def read_file(filename):
    with open(filename, "r") as file:
        return [line.strip().encode() for line in file]
def generate_keys():
    private_key = libnacl.sign.Signer()
    public_key = libnacl.sign.Verifier(private_key.hex_vk())
    return private_key, public_key
def log_time_taken(key_time, sign_time, verify_time, total_time):
    logging.info("Total time cost for key generation: %s s", key_time)
    logging.info("Total time cost for signing the message: %s s", sign_time)
    logging.info("Total time cost for verifying the message: %s s", verify_time)
    logging.info("Total time cost for key generation, message signing, and verifying: %s s", key_time + sign_time + verify_time)
    logging.info("Total time cost for system: %s s", total_time)
def main():
    configure_logging()
    validate_arguments()
    filename = sys.argv[1]
    key_time, sign_time, verify_time = 0, 0, 0
    logging.info("Started libnacl libsodium Ed25519")
    messages = read_file(filename)
    start = time.time()
    for message in messages:
        logging.debug(message)
        start_keygen = time.time()
        private_key, public_key = generate_keys()
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
    log_time_taken(key_time, sign_time, verify_time, total_time)
if __name__ == "__main__":
    main()
import hashlib
import logging
import sys
import time
import libnacl.sign
def configure_logging():
    logging.basicConfig(level=logging.INFO)
def validate_arguments():
    if len(sys.argv) < 2:
        logging.error("Please provide the filename as a command-line argument.")
        sys.exit(1)
def read_file(filename):
    with open(filename, "r") as file:
        return [line.strip().encode() for line in file]
def generate_keys():
    private_key = libnacl.sign.Signer()
    public_key = libnacl.sign.Verifier(private_key.hex_vk())
    return private_key, public_key
def log_time_taken(key_time, sign_time, verify_time, total_time):
    logging.info("Total time cost for key generation: %s s", key_time)
    logging.info("Total time cost for signing the message: %s s", sign_time)
    logging.info("Total time cost for verifying the message: %s s", verify_time)
    logging.info("Total time cost for key generation, message signing, and verifying: %s s", key_time + sign_time + verify_time)
    logging.info("Total time cost for system: %s s", total_time)
def main():
    configure_logging()
    validate_arguments()
    filename = sys.argv[1]
    key_time, sign_time, verify_time = 0, 0, 0
    logging.info("Started libnacl libsodium Ed25519")
    messages = read_file(filename)
    start = time.time()
    for message in messages:
        logging.debug(message)
        start_keygen = time.time()
        private_key, public_key = generate_keys()
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
    log_time_taken(key_time, sign_time, verify_time, total_time)
if __name__ == "__main__":
    main()