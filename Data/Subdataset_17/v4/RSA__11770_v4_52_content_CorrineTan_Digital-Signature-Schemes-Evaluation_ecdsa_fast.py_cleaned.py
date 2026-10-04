import hashlib
import logging
import sys
import time
from fastecdsa import curve, keys, ecdsa
def initialize_logger():
    logging.basicConfig(level=logging.INFO)
def get_curve_and_hash():
    return curve.secp256k1, hashlib.sha256
def read_file(filename):
    with open(filename, "r") as file:
        return file.readlines()
def generate_keypair(param_curve):
    return keys.gen_keypair(param_curve)
def sign_message(message, private_key, param_curve, param_hash):
    return ecdsa.sign(message, private_key, curve=param_curve, hashfunc=param_hash)
def verify_signature(signature, message, public_key, param_curve, param_hash):
    return ecdsa.verify(signature, message, public_key, curve=param_curve, hashfunc=param_hash)
def log_time_cost(key_time, sign_time, verify_time, total_time):
    logging.info(f"Total time cost for generating key is: {key_time:.6f} s")
    logging.info(f"Total time cost for signing the message is: {sign_time:.6f} s")
    logging.info(f"Total time cost for verifying the message is: {verify_time:.6f} s")
    logging.info(f"Total time cost for key generating, message signing and verifying: {total_time:.6f} s")
def main():
    initialize_logger()
    if len(sys.argv) != 2:
        logging.error("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    param_curve, param_hash = get_curve_and_hash()
    key_time = sign_time = verify_time = 0
    logging.info("Started Fast ECDSA with curve: %s, hash: %s", param_curve, param_hash.__name__)
    messages = read_file(filename)
    start = time.time()
    for message in messages:
        logging.debug(message.strip())
        start_keygen = time.time()
        private_key, public_key = generate_keypair(param_curve)
        key_time += time.time() - start_keygen
        start_sign = time.time()
        signature = sign_message(message.strip(), private_key, param_curve, param_hash)
        sign_time += time.time() - start_sign
        start_verify = time.time()
        valid = verify_signature(signature, message.strip(), public_key, param_curve, param_hash)
        logging.debug("Verified: %s", valid)
        verify_time += time.time() - start_verify
    total_time = key_time + sign_time + verify_time
    log_time_cost(key_time, sign_time, verify_time, total_time)
    logging.info("Total elapsed time: %.6f s", time.time() - start)
if __name__ == "__main__":
    main()