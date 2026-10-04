import sys
from toyecc import getcurvebyname, ECPrivateKey
def generate_or_load_keypair(curve, key_hex=None):
    if key_hex is None:
        print("Generating keypair on the fly")
        return ECPrivateKey.eddsa_generate(curve)
    else:
        print("Loading keypair from provided hex")
        return ECPrivateKey.loadkeypair(bytes.fromhex(key_hex))
def sign_message(keypair, message):
    signature = keypair.eddsa_sign(message)
    print(f"Signature: {signature}")
    return signature
def verify_signature(keypair, message, signature):
    is_valid = keypair.pubkey.eddsa_verify(message, signature)
    print(f"Verify correct message: {is_valid} (should be True)")
    forged_message = message + b"x"
    is_forged_valid = keypair.pubkey.eddsa_verify(forged_message, signature)
    print(f"Verify forged message: {is_forged_valid} (should be False)")
def main():
    curve = getcurvebyname("ed25519")
    print("Selected curve:", curve)
    key_hex = sys.argv[1] if len(sys.argv) > 1 else None
    keypair = generate_or_load_keypair(curve, key_hex)
    print("Keypair:", keypair)
    message = b"Foobar!"
    print(f"Message: {message}")
    signature = sign_message(keypair, message)
    verify_signature(keypair, message, signature)
if __name__ == "__main__":
    main()