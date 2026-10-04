import hashlib
import logging
import sys
import time
from fastecdsa import curve, keys, ecdsa
def main():
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        return
    filename = sys.argv[1]
    param_curve = curve.secp256k1
    param_hash = hashlib.sha256
    key_time = 0
    sign_time = 0
    verify_time = 0
    logging.info("Started Fast ECDSA with curve: %s, hash function: %s", param_curve, param_hash.__name__)
    try:
        with open(filename, "r") as f:
            start = time.time()
            for message in f:
                message = message.strip()
                logging.debug("Message: %s", message)
                start_keygen = time.time()
                private_key, public_key = keys.gen_keypair(param_curve)
                key_time += time.time() - start_keygen
                start_sign = time.time()
                r, s = ecdsa.sign(message, private_key, curve=param_curve, hashfunc=param_hash)
                sign_time += time.time() - start_sign
                start_verify = time.time()
                valid = ecdsa.verify((r, s), message, public_key, curve=param_curve, hashfunc=param_hash)
                logging.debug("Verified: %s", valid)
                verify_time += time.time() - start_verify
        total_time = time.time() - start
        sum_time = key_time + sign_time + verify_time
        logging.info("Total time cost for generating keys: %.4f seconds", key_time)
        logging.info("Total time cost for signing messages: %.4f seconds", sign_time)
        logging.info("Total time cost for verifying messages: %.4f seconds", verify_time)
        logging.info("Total time cost for key generation, signing, and verification: %.4f seconds", sum_time)
        logging.info("Total elapsed time: %.4f seconds", total_time)
    except FileNotFoundError:
        logging.error("File not found: %s", filename)
    except Exception as e:
        logging.error("An error occurred: %s", str(e))
if __name__ == "__main__":
    main()