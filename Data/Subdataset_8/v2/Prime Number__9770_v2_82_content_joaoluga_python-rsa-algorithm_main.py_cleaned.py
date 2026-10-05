import sys
from datetime import datetime
class RSA:
    def __init__(self):
        self._public_key = None
        self._private_key = None
        self._p = None
        self._q = None
    def key_gen(self, message, digits):
        pass
    def encode(self):
        pass
    def decode(self):
        pass
if __name__ == "__main__":
    message = "The information security is of great importance to ensure the privacy of communications"
    rsa = RSA()
    start_time = datetime.now()
    rsa.key_gen(message=message, digits=30)
    total_time = (datetime.now() - start_time).total_seconds()
    print('Message:', message)
    print('Public key:', rsa._public_key)
    print('Private Key:', rsa._private_key)
    print('p:', rsa._p)
    print('q:', rsa._q)
    print('Encode:', rsa.encode())
    print('Decode:', rsa.decode())
    print('Total seconds:', total_time)