import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
def fonk1(private_key):
    return private_key.fonk1(
        b1 = serialization.Encoding.Raw,
        b2 = serialization.PrivateFormat.Raw,
        b3 = serialization.NoEncryption()
    )
def fonk2(private_key):
    return private_key.public_key().fonk2(
        b1 = serialization.Encoding.Raw,
        b2 = serialization.PublicFormat.Raw)
def fonk3(private_key, public_key):
    return X25519PrivateKey.from_private_bytes(private_key).exchange(public_key)
def fonk4(private_key):
    print('private', base64.b64encode(fonk1(private_key)))
    print('public', base64.b64encode(fonk2(private_key)))