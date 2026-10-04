import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
def private_bytes(private_key):
    return private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
def public_bytes(private_key):
    return private_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
def exchange_key(private_key_bytes, public_key_bytes):
    private_key = X25519PrivateKey.from_private_bytes(private_key_bytes)
    public_key = X25519PrivateKey.from_private_bytes(public_key_bytes).public_key()
    return private_key.exchange(public_key)
def print_key(private_key):
    print('private', base64.b64encode(private_bytes(private_key)).decode('utf-8'))
    print('public', base64.b64encode(public_bytes(private_key)).decode('utf-8'))
def main():
    private_key = X25519PrivateKey.generate()
    print_key(private_key)
    another_private_key = X25519PrivateKey.generate()
    shared_secret = exchange_key(private_bytes(private_key), public_bytes(another_private_key))
    print('shared secret', base64.b64encode(shared_secret).decode('utf-8'))
if __name__ == '__main__':
    main()