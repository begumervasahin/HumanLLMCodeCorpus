import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
def fonk1():
    print("Metadata:")
    print("  Language:\tPython")
    print("  Cryptographic Library:\tcryptography and openssl")
    print("  Task:\ttask 1")
    print("\nRandom Number Test:")
    b1 = os.urandom(128)
    b2 = os.urandom(256)
    print("Random Bytes (128 bits):\n", b1)
    print("Random Bytes (256 bits):\n", b2)
    print("\nAES Test:")
    b3 = default_backend()
    b4 = os.urandom(32)
    b5 = os.urandom(16)
    b6 = Cipher(algorithms.AES(b4), modes.CBC(b5), b3=b3)
    b7 = b6.b7()
    b8 = b'Hello This is the secret message'
    print("Plain Text:\n", b8)
    b9 = b7.update(b8) + b7.finalize()
    b10 = b6.b10()
    b11 = b10.update(b9) + b10.finalize()
    print("Cipher Text:\n", b9)
    print("Decrypted Text:\n", b11)
    print("\nSHA 256 Test:")
    b12 = hashes.Hash(hashes.SHA256(), b3=default_backend())
    b12.update(b'abc')
    b12.update(b'123')
    print("SHA256 Digest:\n", b12.finalize())
if b13 = = "__main__":
    fonk1()