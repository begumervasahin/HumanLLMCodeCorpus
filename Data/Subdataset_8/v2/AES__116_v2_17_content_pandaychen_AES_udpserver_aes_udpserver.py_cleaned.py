import socket
import logging
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import signal
LOG_DIRECTORY = './logs/'
LOG_FILENAME = 'udp_server.log'
SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888
MAX_BUFFER_SIZE = 8192
ENCRYPTION_KEY = b'1234567812345678'
ENCRYPTION_IV = b'1234567812345678'
received_packets_count = 0
os.makedirs(LOG_DIRECTORY, exist_ok=True)
logging.basicConfig(filename=os.path.join(LOG_DIRECTORY, LOG_FILENAME),
                    level=logging.INFO,
                    format='[%(asctime)s] %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
def signal_handler(signal_number, frame):
    logging.info(f"Received signal: {signal_number}; Total packets received: {received_packets_count}")
    sys.exit(0)
def decrypt_data(data):
    cipher = Cipher(algorithms.AES(ENCRYPTION_KEY), modes.CBC(ENCRYPTION_IV), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(base64.b64decode(data)) + decryptor.finalize()
    return decrypted_data
def setup_server(ip_address, port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip_address, port))
        logging.info(f"Server is listening on {ip_address}:{port}")
        return server_socket
    except socket.error as err:
        logging.error(f"Failed to create socket: {err}")
        sys.exit(1)
def server_loop(server_socket):
    global received_packets_count
    while True:
        message, client_address = server_socket.recvfrom(MAX_BUFFER_SIZE)
        if message:
            received_packets_count += 1
            decrypted_message = decrypt_data(message)
            logging.info(f"Packet received from {client_address}. Decrypted message: {decrypted_message}")
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    udp_server_socket = setup_server(SERVER_IP, SERVER_PORT)
    server_loop(udp_server_socket)