import sys
from toyecc import getcurvebyname, ECPrivateKey
def main():
    curve = getcurvebyname("ed25519")
    if len(sys.argv) < 2:
        keypair = ECPrivateKey.eddsa_generate(curve)
        print("Generating keypair on the fly")
    else:
        keypair = ECPrivateKey.loadkeypair(bytes.fromhex(sys.argv[1]))
    print("Keypair:", keypair)
    msg = b"Foobar!"
    print("Message:", msg)
    signature = keypair.eddsa_sign(msg)
    print("Signature:", signature)
    is_valid = keypair.pubkey.eddsa_verify(msg, signature)
    print(f"Verify correct message: {is_valid} (should be True)")
    is_forged_valid = keypair.pubkey.eddsa_verify(msg + b"x", signature)
    print(f"Verify forged message: {is_forged_valid} (should be False)")
if __name__ == "__main__":
    main()