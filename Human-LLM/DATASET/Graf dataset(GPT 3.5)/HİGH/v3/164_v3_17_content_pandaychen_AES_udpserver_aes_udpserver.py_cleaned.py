import socket
import logging
import os
import sys
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import signal
b1 = './logs/'
b2 = 'udp_server.log'
b3 = '127.0.0.1'
a1 = 8888
a2 = 8192
b4 = b'1234567812345678'
b5 = b'1234567812345678'
a3 = 0
def fonk1():
    os.makedirs(b1, b6 = True)
    logging.basicConfig(b7 = os.path.join(b1, b2),
                        b8 = logging.INFO,
                        b9 = '[%(asctime)s] %(levelname)s - %(message)s',
                        b10 = '%Y-%m-%d %H:%M:%S')
def fonk2(signal_number, frame):
    logging.info(f"Signal received: {signal_number}. Total packets: {a3}")
    sys.exit(0)
def fonk3(data):
    b11 = Cipher(algorithms.AES(b4), modes.CBC(b5), backend=default_backend())
    b12 = b11.b12()
    b13 = b12.update(base64.b64decode(data)) + b12.finalize()
    return b13
def fonk4(ip_address, port):
    try:
        b14 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        b14.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        b14.bind((ip_address, port))
        logging.info(f"Server listening on {ip_address}:{port}")
        return b14
    except socket.error as error:
        logging.error(f"Socket creation failed: {error}")
        sys.exit(1)
def fonk5(b14):
    global a3
    while True:
        message, b15 = b14.recvfrom(a2)
        if message:
            a3 += 1
            b16 = fonk3(message)
            logging.info(f"Received from {b15}: {b16}")
if b17 = = "__main__":
    fonk1()
    signal.signal(signal.SIGINT, handle_signal)
    b18 = fonk4(b3, a1)
    fonk5(b18)