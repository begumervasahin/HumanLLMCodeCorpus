import sys
from datetime import datetime
from rsa import Rsa
sys.setrecursionlimit(5000)
def main():
    message = "The information security is of great importance to ensure the privacy of communications"
    rsa = Rsa()
    start_time = datetime.now()
    rsa.key_gen(message=message, digits=30)
    total_time = (datetime.now() - start_time).total_seconds()
    print(f'Message: {rsa._message}\n')
    print(f'Public Key: {rsa._public_key}\n')
    print(f'Private Key: {rsa._private_key}\n')
    print(f'Prime p: {rsa._p}')
    print(f'Prime q: {rsa._q}\n')
    print(f'Encoded Message: {rsa._encode}\n')
    print(f'Decoded Message: {rsa._decode}\n')
    print(f'Performance: {rsa._performance}')
    print(f'Total Time for Key Generation: {total_time} seconds')
if __name__ == "__main__":
    main()