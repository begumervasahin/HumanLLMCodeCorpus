import ed25519
import time
import sys
import hashlib
def ed25519_test(filename):
    keygen_time = 0
    sign_time = 0
    verify_time = 0
    with open(filename) as file:
        for line in file:
            message = line.strip().encode()
            digest = hashlib.sha256(message).digest()
            keygen_start = time.time()
            signing_key, verifying_key = ed25519.create_keypair()
            keygen_end = time.time()
            keygen_time += keygen_end - keygen_start
            sign_start = time.time()
            signature = signing_key.sign(digest, encoding="base64")
            sign_end = time.time()
            sign_time += sign_end - sign_start
            verify_start = time.time()
            try:
                verifying_key.verify(signature, digest, encoding="base64")
            except ed25519.BadSignatureError:
                print("Invalid signature!")
            verify_end = time.time()
            verify_time += verify_end - verify_start
    return keygen_time, sign_time, verify_time
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    keygen_time, sign_time, verify_time = ed25519_test(filename)
    total_time = keygen_time + sign_time + verify_time
    print("Time taken for key pair generation:", keygen_time)
    print("Time taken for message signing:", sign_time)
    print("Time taken for message verification:", verify_time)
    print("Total time taken:", total_time)