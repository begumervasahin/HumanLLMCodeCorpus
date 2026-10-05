import socket
import rsa_encryption as rsa
import sys
import argparse
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, help="Minimum number of bits required to represent a symbol (default: 128)", default=128)
    return parser.parse_args()
def check_length_feasibility(length):
    primes = rsa.primes
    if length < 128:
        print("Error: At least a value of 128 is required to represent all ASCII characters uniquely.")
        sys.exit()
    elif length > primes[-1] * primes[-2]:
        print("Error: Using primes higher than 293 (length > 82919) is outside the scope of this project.")
        sys.exit()
def generate_rsa_keys(length):
    return rsa.keygen(length)
def establish_connection():
    s = socket.socket()
    host = socket.gethostname()
    port = 60000
    s.connect((host, port))
    return s
def send_message(s, message):
    s.send(message.encode())
def receive_file(s, filename):
    with open(filename, 'wb') as f:
        print('File opened')
        while True:
            print('Receiving data...')
            data = s.recv(1024)
            if not data:
                break
            f.write(data)
def decrypt_received_file(filename, n, d):
    rsa.decode(filename, n, d)
def print_success_message():
    print('Successfully received the file')
def close_connection(s):
    s.close()
    print('Connection closed')
def main():
    args = parse_arguments()
    check_length_feasibility(args.length)
    n, e, d = generate_rsa_keys(args.length)
    s = establish_connection()
    send_message(s, "Hello server!")
    filename = "received_file.txt"
    receive_file(s, filename)
    decrypt_received_file(filename, n, d)
    print_success_message()
    close_connection(s)
if __name__ == "__main__":
    main()