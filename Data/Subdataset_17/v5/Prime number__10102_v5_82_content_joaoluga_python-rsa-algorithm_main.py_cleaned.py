import sys
from datetime import datetime
from rsa import Rsa
sys.setrecursionlimit(5000)
def main():
    message = "The information security is of great importance to ensure the privacy of communications"
    rsa_code = Rsa()
    start = datetime.now()
    rsa_code.key_gen(message=message, digits=30)
    total_time = (datetime.now() - start).total_seconds()
    print(f'Message: {rsa_code._message}\n')
    print(f'Public key: {rsa_code._public_key}\n')
    print(f'Private Key: {rsa_code._private_key}\n')
    print(f'p: {rsa_code._p}')
    print(f'q: {rsa_code._q}\n')
    print(f'Encoded message: {rsa_code._encode}\n')
    print(f'Decoded message: {rsa_code._decode}\n')
    print(f'Performance: {rsa_code._performance}')
    print(f'Total time taken: {total_time} seconds')
if __name__ == "__main__":
    main()