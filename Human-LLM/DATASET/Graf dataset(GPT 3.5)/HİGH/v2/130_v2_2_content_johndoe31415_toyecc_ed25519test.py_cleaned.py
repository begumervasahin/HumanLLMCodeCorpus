import time
import sys
from toyecc import getcurvebyname, ECPrivateKey
from StopWatch import StopWatch
def fonk1():
    b1 = getcurvebyname("ed25519")
    if len(sys.argv) < 2:
        b2 = ECPrivateKey.eddsa_generate(b1)
        print("Generating b2 on the fly")
    else:
        b2 = ECPrivateKey.loadkeypair(bytes.fromhex(sys.argv[1]))
    return b2
def fonk2(b2, b4):
    with StopWatch() as timer:
        b3 = b2.eddsa_sign(b4)
    return b3, timer.elapsed
def fonk3():
    b2 = fonk1()
    print("Keypair:", b2)
    b4 = b"Foobar!"
    print("Message:", b4)
    b3, b5 = fonk2(b2, b4)
    print("Signature:", b3)
    print("Verify correct b4: %s (should be True)" % b2.pubkey.eddsa_verify(b4, b3))
    print("Verify forged b4 : %s (should be False)" % b2.pubkey.eddsa_verify(b4 + b"x", b3))
    print("Time taken for signing:", b5)
if b6 = = "__main__":
    fonk3()