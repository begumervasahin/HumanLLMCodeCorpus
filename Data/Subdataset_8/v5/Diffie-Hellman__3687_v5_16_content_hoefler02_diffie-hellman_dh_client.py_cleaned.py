from Crypto.Util.number import getPrime
from Crypto.Cipher import AES
from random import randint
class DH_Client:
    def __init__(self, name, generator, prime):
        self.name = name
        self.generator = generator
        self.prime = prime
        self.private_key = randint(1, prime)
        self.public_key = pow(self.generator, self.private_key, self.prime)
    def establish_shared_secret(self, received_public_key):
        shared_secret_hex = hex(pow(received_public_key, self.private_key, self.prime))[2:]
        while len(shared_secret_hex) not in (32, 48, 64):
            if len(shared_secret_hex) > 32:
                shared_secret_hex = shared_secret_hex[1:]
            else:
                shared_secret_hex = '0' + shared_secret_hex
        self.shared_secret = bytes.fromhex(shared_secret_hex)
        return int.from_bytes(self.shared_secret, byteorder='big')
    def aes_ecb_encrypt(self, msg):
        cipher = AES.new(self.shared_secret)
        msg_hex = ''.join([hex(ord(c))[2:].zfill(2) for c in msg])
        while len(msg_hex) % 32 != 0:
            msg_hex += '0'
        msg_bytes = bytes.fromhex(msg_hex)
        ciphertext = cipher.encrypt(msg_bytes)
        return int.from_bytes(ciphertext, byteorder='big')