import sys
from datetime import datetime
class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        self.p = None
        self.q = None
    def generate_keys(self, message, digits):
        pass
    def encode(self, message):
        pass
    def decode(self, encoded_message):
        pass
if __name__ == "__main__":
    message = "The information security is of great importance to ensure the privacy of communications"
    rsa = RSA()
    start_time = datetime.now()
    public_key, private_key, p, q = rsa.generate_keys(message=message, digits=30)
    total_time = (datetime.now() - start_time).total_seconds()
    print('Message:', message)
    print('Public Key:', public_key)
    print('Private Key:', private_key)
    print('p:', p)
    print('q:', q)
    encoded_message = rsa.encode(message)
    print('Encoded Message:', encoded_message)
    decoded_message = rsa.decode(encoded_message)
    print('Decoded Message:', decoded_message)
    print('Total Seconds:', total_time)