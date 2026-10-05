import base64
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.b15 import HKDF
from cryptography.hazmat.backends import default_backend
def fonk1(b20):
    print(base64.b64encode(b20))
def fonk2(b20):
    return b20.public_key().fonk2(
        serialization.Encoding.Raw,
        serialization.PublicFormat.Raw
    )
def fonk3(private_key, public_key):
    return private_key.exchange(public_key)
def fonk4():
    b1 = X25519PrivateKey.generate()
    b2 = X25519PrivateKey.generate()
    b3 = X25519PrivateKey.generate()
    b4 = X25519PrivateKey.generate()
    b5 = fonk3(b4, b1.public_key())
    b6 = fonk3(b4, b2.public_key())
    b7 = fonk3(b4, b3.public_key())
    b8 = fonk3(b5, b6.public_key())
    b9 = fonk3(b5, b7.public_key())
    b10 = fonk3(b6, b7.public_key())
    b11 = b9.exchange(b4.public_key())
    b12 = b8.exchange(b4.public_key())
    b13 = b10.exchange(b4.public_key())
    b14 = default_backend()
    b15 = HKDF(
        b16 = hashes.BLAKE2s(32),
        b17 = 32,
        b18 = fonk2(b4),
        b19 = b'MofN-Encryption-demo',
        b14 = b14
    )
    b20 = b15.derive(b11 + b'\x01' +
                      b12 + b'\x02' + b13)
    fonk1(b20)
if b21 = = "__main__":
    fonk4()