import ed25519
import time
import sys
import hashlib
def ed25519test(filename):
    keygen_time = 0
    sign_time = 0
    verify_time = 0
    with open(filename) as file:
        for line in file:
            message = str.encode(line.strip())
            digest = hashlib.sha256(message).digest()
            keygen_start_time = time.time()
            signing_key, verifying_key = ed25519.create_keypair()
            keygen_end_time = time.time()
            keygen_time += keygen_end_time - keygen_start_time
            sign_start_time = time.time()
            signature = signing_key.sign(digest, encoding="base64")
            sign_end_time = time.time()
            sign_time += sign_end_time - sign_start_time
            verify_start_time = time.time()
            try:
                verifying_key.verify(signature, digest, encoding="base64")
            except ed25519.BadSignatureError:
                print("Signature is invalid!")
            verify_end_time = time.time()
            verify_time += verify_end_time - verify_start_time
    return keygen_time, sign_time, verify_time
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    keygen_time, sign_time, verify_time = ed25519test(filename)
    total_time = keygen_time + sign_time + verify_time
    print("Time taken for key pair generation:", keygen_time)
    print("Time taken for message signing:", sign_time)
    print("Time taken for message verification:", verify_time)
    print("Total time taken:", total_time)