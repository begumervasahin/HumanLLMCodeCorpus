import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
def main():
    print("Metadata:")
    print("  Language:\tPython")
    print("  Cryptographic Library:\tcryptography and openssl")
    print("  Task:\ttask 1")
    print("\nRandom Number Test:")
    rbytes1 = os.urandom(128)
    rbytes2 = os.urandom(256)
    print("Random Bytes (128 bits):\n", rbytes1)
    print("Random Bytes (256 bits):\n", rbytes2)
    print("\nAES Test:")
    backend = default_backend()
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    pt = b'Hello This is the secret message'
    print("Plain Text:\n", pt)
    ct = encryptor.update(pt) + encryptor.finalize()
    decryptor = cipher.decryptor()
    pt_new = decryptor.update(ct) + decryptor.finalize()
    print("Cipher Text:\n", ct)
    print("Decrypted Text:\n", pt_new)
    print("\nSHA 256 Test:")
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(b'abc')
    digest.update(b'123')
    print("SHA256 Digest:\n", digest.finalize())
if __name__ == "__main__":
    main()