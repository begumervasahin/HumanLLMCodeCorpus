import socket
import rsa_encryption as rsa
import sys
import argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description="Client for securely receiving a file via RSA encryption.")
    parser.add_argument("-l", "--length", type=int, default=128,
                        help="Minimum length required to represent a symbol (default: 128)")
    return parser.parse_args()
def validate_length(args):
    primes = rsa.primes
    if args.length < 128:
        print("Error: The minimum value of 128 is required to represent all ASCII characters uniquely.")
        sys.exit()
    elif args.length > primes[-1] * primes[-2]:
        print("Error: Using primes higher than 293 (length > 82919) is outside the scope of this project.")
        sys.exit()
def receive_file(s, filename):
    with open(filename, 'wb') as f:
        print('File opened')
        while True:
            print('Receiving data...')
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
    print('File received successfully')
def decrypt_file(filename, n, d):
    rsa.decode(filename, n, d)
    print('File decrypted successfully')
def main():
    args = parse_arguments()
    validate_length(args)
    n, e, d = rsa.keygen(args.length)
    s = socket.socket()
    host = socket.gethostname()
    port = 60000
    s.connect((host, port))
    s.send(b"Hello server!")
    filename = "received_file.txt"
    receive_file(s, filename)
    decrypt_file(filename, n, d)
    s.close()
    print('Connection closed')
if __name__ == "__main__":
    main()