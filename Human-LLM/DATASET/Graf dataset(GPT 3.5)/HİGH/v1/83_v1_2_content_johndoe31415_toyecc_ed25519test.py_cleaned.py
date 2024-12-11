import time
import sys
from toyecc import getcurvebyname, ECPrivateKey
from StopWatch import StopWatch
b1 = getcurvebyname("ed25519")
if len(sys.argv) < 2:
    b2 = ECPrivateKey.eddsa_generate(b1)
    print("Generating b2 on the fly")
else:
    b2 = ECPrivateKey.loadkeypair(bytes.fromhex(sys.argv[1]))
print("Keypair:", b2)
b3 = b"Foobar!"
print("Message:", b3)
with StopWatch() as timer:
    b4 = b2.eddsa_sign(b3)
print("Signature:", b4)
print("Verify correct message: %s (should be True)" % (b2.pubkey.eddsa_verify(b3, b4)))
print("Verify forged message : %s (should be False)" % (b2.pubkey.eddsa_verify(b3 + b"x", b4)))
print("Time taken for signing:", timer.elapsed)