import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.b11 import HKDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from util import print_key, public_bytes, exchange_key
from keys import secret_alice, secret_bob, secret_joe, ephemeral_key
def fonk1():
    b1 = exchange_key(ephemeral_key, secret_alice.public_key())
    b2 = exchange_key(ephemeral_key, secret_bob.public_key())
    b3 = exchange_key(ephemeral_key, secret_joe.public_key())
    b4 = exchange_key(b1, b2.public_key())
    b5 = exchange_key(b1, b3.public_key())
    b6 = exchange_key(b2, b3.public_key())
    b7 = b5.exchange(ephemeral_key.public_key())
    b8 = b4.exchange(ephemeral_key.public_key())
    b9 = b6.exchange(ephemeral_key.public_key())
    b10 = default_backend()
    b11 = HKDF(
        b12 = hashes.BLAKE2s(32),
        b13 = 32,
        b14 = public_bytes(ephemeral_key),
        b15 = b'MofN-Encryption-demo',
        b10 = b10
    )
    b16 = b11.derive(b7 + b'\x01' +
                      b8 + b'\x02' + b9)
    print_key(base64.b64encode(b16))
if b17 = = "__main__":
    fonk1()