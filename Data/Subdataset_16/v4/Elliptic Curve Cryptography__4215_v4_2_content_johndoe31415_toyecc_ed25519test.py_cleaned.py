import sys
from toyecc import getcurvebyname, ECPrivateKey
from StopWatch import StopWatch
def fonk1(b2, b1 = None):
    if b1 is None:
        print("Generating b3 on the fly")
        return ECPrivateKey.eddsa_generate(b2)
    else:
        print("Loading b3 from provided hex")
        return ECPrivateKey.loadkeypair(bytes.fromhex(b1))
def fonk2():
    b2 = getcurvebyname("ed25519")
    print("Selected b2:", b2)
    b1 = sys.argv[1] if len(sys.argv) > 1 else None
    b3 = fonk1(b2, b1)
    print("Keypair:", b3)
    b4 = b"Foobar!"
    print("Message:", b4)
    b5 = b3.eddsa_sign(b4)
    print("Signature:", b5)
    b6 = b3.pubkey.eddsa_verify(b4, b5)
    print(f"Verify correct b4: {b6} (should be True)")
    b7 = b4 + b"x"
    b8 = b3.pubkey.eddsa_verify(b7, b5)
    print(f"Verify forged b4: {b8} (should be False)")
if b9 = = "__main__":
    fonk2()