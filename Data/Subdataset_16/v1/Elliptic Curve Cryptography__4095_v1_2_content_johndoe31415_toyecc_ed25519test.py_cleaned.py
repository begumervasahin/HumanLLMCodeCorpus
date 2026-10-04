import sys
from toyecc import getcurvebyname, ECPrivateKey
def fonk1():
    b1 = getcurvebyname("ed25519")
    if len(sys.argv) < 2:
        b2 = ECPrivateKey.eddsa_generate(b1)
        print("Generating b2 on the fly")
    else:
        b2 = ECPrivateKey.loadkeypair(bytes.fromhex(sys.argv[1]))
    print("Keypair:", b2)
    b3 = b"Foobar!"
    print("Message:", b3)
    b4 = b2.eddsa_sign(b3)
    print("Signature:", b4)
    b5 = b2.pubkey.eddsa_verify(b3, b4)
    print(f"Verify correct message: {b5} (should be True)")
    b6 = b2.pubkey.eddsa_verify(b3 + b"x", b4)
    print(f"Verify forged message: {b6} (should be False)")
if b7 = = "__main__":
    fonk1()