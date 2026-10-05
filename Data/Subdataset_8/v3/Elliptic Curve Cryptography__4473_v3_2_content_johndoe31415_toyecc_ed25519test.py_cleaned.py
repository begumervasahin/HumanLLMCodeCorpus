import sys
import time
from toyecc import getcurvebyname, ECPrivateKey
from StopWatch import StopWatch
def generate_or_load_keypair():
    curve = getcurvebyname("ed25519")
    if len(sys.argv) < 2:
        keypair = ECPrivateKey.eddsa_generate(curve)
        print("Generating keypair on the fly")
    else:
        keypair = ECPrivateKey.loadkeypair(bytes.fromhex(sys.argv[1]))
    return keypair
def sign_message_and_measure_time(keypair, message):
    with StopWatch() as timer:
        signature = keypair.eddsa_sign(message)
    return signature, timer.elapsed
def main():
    keypair = generate_or_load_keypair()
    print("Keypair:", keypair)
    message = b"Foobar!"
    print("Message:", message)
    signature, signing_time = sign_message_and_measure_time(keypair, message)
    print("Signature:", signature)
    print("Verify correct message: %s (should be True)" % keypair.pubkey.eddsa_verify(message, signature))
    print("Verify forged message : %s (should be False)" % keypair.pubkey.eddsa_verify(message + b"x", signature))
    print("Time taken for signing:", signing_time)
if __name__ == "__main__":
    main()