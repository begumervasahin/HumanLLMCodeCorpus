import hashlib
import logging
import sys
import time
from fastecdsa import curve, keys, ecdsa
def main():
    logging.basicConfig(level=logging.INFO)
    filename = sys.argv[1]
    param_curve = curve.secp256k1
    param_hash = hashlib.sha256
    key_time = 0
    sign_time = 0
    verify_time = 0
    logging.info("Started Fast ECDSA with curve: %s, sha: %s", param_curve, str(param_hash.__name__))
    with open(filename, "r") as f:
        start = time.time()
        for m in f:
            m = m.strip()
            logging.debug(m)
            start_keygen = time.time()
            private_key, public_key = keys.gen_keypair(param_curve)
            key_time += time.time() - start_keygen
            start_sign = time.time()
            r, s = ecdsa.sign(m, private_key, curve=param_curve, hashfunc=param_hash)
            sign_time += time.time() - start_sign
            start_verify = time.time()
            valid = ecdsa.verify((r, s), m, public_key, curve=param_curve, hashfunc=param_hash)
            logging.debug("Verified: %s" % valid)
            verify_time += time.time() - start_verify
    sum_time = key_time + sign_time + verify_time
    logging.info("Total time cost for generating key is: %s s", key_time)
    logging.info("Total time cost for signing the message is: %s s", sign_time)
    logging.info("Total time cost for verifying the message is: %s s", verify_time)
    logging.info("Total time cost for key generating, message signing and verifying: %s s", sum_time)
    logging.info("Total time cost for system time: %s s", time.time() - start)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        main()