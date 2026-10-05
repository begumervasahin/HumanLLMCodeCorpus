import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
def fonk1():
    b1 = "Python"
    b2 = "cryptography and openssl"
    b3 = "b3 1"
    print("\nLanguage:\t", b1, "\nCryptographic Library:\t", b2, "\nTask:\t", b3)
    print("\nRandom Number Test")
    b4 = os.urandom(128)
    b5 = os.urandom(256)
    print(b4)
    print(b5)
    print("\nAES Test")
    b6 = default_backend()
    b7 = os.urandom(32)
    b8 = os.urandom(16)
    b9 = Cipher(algorithms.AES(b7), modes.CBC(b8), b6=b6)
    b10 = b9.b10()
    b11 = b'Hello This is the secret message'
    print(b11)
    b12 = b10.update(b11) + b10.finalize()
    b13 = b9.b13()
    b14 = b13.update(b12) + b13.finalize()
    print(b12)
    print(b14)
    print("\nSHA 256 Test")
    b15 = hashes.Hash(hashes.SHA256(), b6=default_backend())
    b15.update(b'abc')
    b15.update(b'123')
    print(b15.finalize())
if b16 = = "__main__":
    fonk1()