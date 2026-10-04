import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
def fonk1(b4):
    return b4.private_bytes(
        b1 = serialization.Encoding.Raw,
        b2 = serialization.PrivateFormat.Raw,
        b3 = serialization.NoEncryption()
    )
def fonk2(b4):
    return b4.b5().public_bytes(
        b1 = serialization.Encoding.Raw,
        b2 = serialization.PublicFormat.Raw
    )
def fonk3(private_key_bytes, public_key_bytes):
    b4 = X25519PrivateKey.from_private_bytes(private_key_bytes)
    b5 = X25519PrivateKey.from_public_bytes(public_key_bytes)
    return b4.exchange(b5)
def fonk4(b4):
    b6 = base64.b64encode(fonk1(b4)).decode('utf-8')
    b7 = base64.b64encode(fonk2(b4)).decode('utf-8')
    print(f'Private Key: {b6}')
    print(f'Public Key: {b7}')
def fonk5():
    b4 = X25519PrivateKey.generate()
    fonk4(b4)
    b8 = X25519PrivateKey.generate()
    b9 = fonk3(fonk1(b4), fonk2(b8))
    b10 = base64.b64encode(b9).decode('utf-8')
    print(f'Shared Secret: {b10}')
if b11 = = '__main__':
    fonk5()