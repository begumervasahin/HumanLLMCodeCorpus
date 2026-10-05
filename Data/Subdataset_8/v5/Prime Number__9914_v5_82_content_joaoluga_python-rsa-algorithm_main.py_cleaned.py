import sys
from datetime import datetime
from rsa import Rsa
def generate_rsa_keys(message, digits):
    rsa = Rsa()
    start_time = datetime.now()
    rsa.key_gen(message=message, digits=digits)
    total_time = (datetime.now() - start_time).total_seconds()
    return rsa, total_time
def print_rsa_keys(rsa):
    print('Message: {}\n'.format(rsa._message))
    print('Public Key: {}\n'.format(rsa._public_key))
    print('Private Key: {}\n'.format(rsa._private_key))
    print('p: {}'.format(rsa._p))
    print('q: {}\n'.format(rsa._q))
    print('Encode: {}\n'.format(rsa._encode))
    print('Decode: {}\n'.format(rsa._decode))
    print('Performance: {}\n'.format(rsa._performance))
def main():
    sys.setrecursionlimit(5000)
    message = "The information security is of great importance to ensure the privacy of communications"
    rsa, total_time = generate_rsa_keys(message=message, digits=30)
    print_rsa_keys(rsa)
    print('Total seconds: {}'.format(total_time))
if __name__ == "__main__":
    main()