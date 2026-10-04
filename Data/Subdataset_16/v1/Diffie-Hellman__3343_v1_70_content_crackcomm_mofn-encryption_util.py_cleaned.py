import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
def fonk1(b4):
    return b4.fonk1(
        b1 = serialization.Encoding.Raw,
        b2 = serialization.PrivateFormat.Raw,
        b3 = serialization.NoEncryption()
    )
def fonk2(b4):
    return b4.b5().fonk2(
        b1 = serialization.Encoding.Raw,
        b2 = serialization.PublicFormat.Raw
    )
def fonk3(private_key_bytes, public_key_bytes):
    b4 = X25519PrivateKey.from_private_bytes(private_key_bytes)
    b5 = X25519PrivateKey.from_private_bytes(public_key_bytes).b5()
    return b4.exchange(b5)
def fonk4(b4):
    print('private', base64.b64encode(fonk1(b4)).decode('utf-8'))
    print('public', base64.b64encode(fonk2(b4)).decode('utf-8'))
def fonk5():
    b4 = X25519PrivateKey.generate()
    fonk4(b4)
    b6 = X25519PrivateKey.generate()
    b7 = fonk3(fonk1(b4), fonk2(b6))
    print('shared secret', base64.b64encode(b7).decode('utf-8'))
if b8 = = '__main__':
    fonk5()