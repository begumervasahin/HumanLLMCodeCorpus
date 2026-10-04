import base64
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
def serialize_private_key(private_key):
    return private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
def serialize_public_key(private_key):
    return private_key.public_key().public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )
def exchange_keys(private_key_bytes, public_key_bytes):
    private_key = X25519PrivateKey.from_private_bytes(private_key_bytes)
    public_key = X25519PrivateKey.from_public_bytes(public_key_bytes)
    return private_key.exchange(public_key)
def print_keys(private_key):
    private_key_encoded = base64.b64encode(serialize_private_key(private_key)).decode('utf-8')
    public_key_encoded = base64.b64encode(serialize_public_key(private_key)).decode('utf-8')
    print(f'Private Key: {private_key_encoded}')
    print(f'Public Key: {public_key_encoded}')
def main():
    private_key = X25519PrivateKey.generate()
    print_keys(private_key)
    another_private_key = X25519PrivateKey.generate()
    shared_secret = exchange_keys(serialize_private_key(private_key), serialize_public_key(another_private_key))
    shared_secret_encoded = base64.b64encode(shared_secret).decode('utf-8')
    print(f'Shared Secret: {shared_secret_encoded}')
if __name__ == '__main__':
    main()