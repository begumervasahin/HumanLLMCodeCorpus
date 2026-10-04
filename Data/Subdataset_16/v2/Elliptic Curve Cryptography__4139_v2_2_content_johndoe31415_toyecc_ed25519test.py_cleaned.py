import sys
from toyecc import getcurvebyname, ECPrivateKey
def fonk1(b6, b1 = None):
    if b1 is None:
        print("Generating b7 on the fly")
        return ECPrivateKey.eddsa_generate(b6)
    else:
        print("Loading b7 from provided hex")
        return ECPrivateKey.loadkeypair(bytes.fromhex(b1))
def fonk2(b7, b8):
    print(f"Message: {b8}")
    b2 = b7.eddsa_sign(b8)
    print(f"Signature: {b2}")
    b3 = b7.pubkey.eddsa_verify(b8, b2)
    print(f"Verify correct b8: {b3} (should be True)")
    b4 = b8 + b"x"
    b5 = b7.pubkey.eddsa_verify(b4, b2)
    print(f"Verify forged b8: {b5} (should be False)")
def fonk3():
    b6 = getcurvebyname("ed25519")
    print("Selected b6:", b6)
    b1 = sys.argv[1] if len(sys.argv) > 1 else None
    b7 = fonk1(b6, b1)
    print("Keypair:", b7)
    b8 = b"Foobar!"
    fonk2(b7, b8)
if b9 = = "__main__":
    fonk3()