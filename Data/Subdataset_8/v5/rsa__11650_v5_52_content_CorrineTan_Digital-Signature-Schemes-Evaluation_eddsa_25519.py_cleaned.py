import ed25519
import time
import sys
import hashlib
def ed25519_test(filename):
    time_to_generate_keys = 0
    time_to_sign_messages = 0
    time_to_verify_messages = 0
    with open(filename) as file:
        for line in file:
            message = str.encode(line)
            digest = hashlib.sha256(message).digest()
            keygen_start = time.time()
            signing_key, verifying_key = ed25519.create_keypair()
            keygen_end = time.time()
            time_to_generate_keys += keygen_end - keygen_start
            sign_start = time.time()
            signature = signing_key.sign(digest, encoding="base64")
            sign_end = time.time()
            time_to_sign_messages += sign_end - sign_start
            verify_start = time.time()
            try:
                verifying_key.verify(signature, digest, encoding="base64")
            except ed25519.BadSignatureError:
                print("Invalid signature!")
            verify_end = time.time()
            time_to_verify_messages += verify_end - verify_start
    return time_to_generate_keys, time_to_sign_messages, time_to_verify_messages
if __name__ == '__main__':
    filename = "".join(sys.argv[1:])
    time_to_generate_keys, time_to_sign_messages, time_to_verify_messages = ed25519_test(filename)
    total_time = time_to_generate_keys + time_to_sign_messages + time_to_verify_messages
    print("Time taken to generate key pairs:", time_to_generate_keys)
    print("Time taken to sign messages:", time_to_sign_messages)
    print("Time taken to verify messages:", time_to_verify_messages)
    print("Total time:", total_time)