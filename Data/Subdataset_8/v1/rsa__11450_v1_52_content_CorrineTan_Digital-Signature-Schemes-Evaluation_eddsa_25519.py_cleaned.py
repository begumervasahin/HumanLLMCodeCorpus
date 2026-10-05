import ed25519
import time
import sys
import hashlib
def ed25519test(filename):
    time1 = 0
    time2 = 0
    time3 = 0
    with open(filename) as f:
        for line in f:
            message = str.encode(line.strip())
            digest = hashlib.sha256(message).digest()
            keygen_start = time.time()
            signing_key, verifying_key = ed25519.create_keypair()
            keygen_end = time.time()
            time1 += keygen_end - keygen_start
            sign_start = time.time()
            signature = signing_key.sign(digest, encoding="base64")
            sign_end = time.time()
            time2 += sign_end - sign_start
            verify_start = time.time()
            try:
                verifying_key.verify(signature, digest, encoding="base64")
            except ed25519.BadSignatureError:
                print("Signature is bad!")
            verify_end = time.time()
            time3 += verify_end - verify_start
    return time1, time2, time3
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    time1, time2, time3 = ed25519test(filename)
    total_time = time1 + time2 + time3
    print("The time used to generate key pairs:", time1)
    print("The time used to sign messages:", time2)
    print("The time used to verify messages:", time3)
    print("Total time:", total_time)