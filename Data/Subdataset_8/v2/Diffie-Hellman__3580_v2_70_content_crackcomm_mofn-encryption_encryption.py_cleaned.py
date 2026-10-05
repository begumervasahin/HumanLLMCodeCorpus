import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend
def print_key(key):
    print(base64.b64encode(key))
def public_bytes(key):
    return key.public_key().public_bytes(
        serialization.Encoding.Raw,
        serialization.PublicFormat.Raw
    )
def exchange_key(private_key, public_key):
    return private_key.exchange(public_key)
def main():
    secret_alice = X25519PrivateKey.generate()
    secret_bob = X25519PrivateKey.generate()
    secret_joe = X25519PrivateKey.generate()
    ephemeral_key = X25519PrivateKey.generate()
    shared_alice = exchange_key(ephemeral_key, secret_alice.public_key())
    shared_bob = exchange_key(ephemeral_key, secret_bob.public_key())
    shared_joe = exchange_key(ephemeral_key, secret_joe.public_key())
    shared_alice_bob = exchange_key(shared_alice, shared_bob.public_key())
    shared_alice_joe = exchange_key(shared_alice, shared_joe.public_key())
    shared_bob_joe = exchange_key(shared_bob, shared_joe.public_key())
    ephemeral_alice_joe = shared_alice_joe.exchange(ephemeral_key.public_key())
    ephemeral_alice_bob = shared_alice_bob.exchange(ephemeral_key.public_key())
    ephemeral_bob_joe = shared_bob_joe.exchange(ephemeral_key.public_key())
    backend = default_backend()
    hkdf = HKDF(
        algorithm=hashes.BLAKE2s(32),
        length=32,
        salt=public_bytes(ephemeral_key),
        info=b'MofN-Encryption-demo',
        backend=backend
    )
    key = hkdf.derive(ephemeral_alice_joe + b'\x01' +
                      ephemeral_alice_bob + b'\x02' + ephemeral_bob_joe)
    print_key(key)
if __name__ == "__main__":
    main()