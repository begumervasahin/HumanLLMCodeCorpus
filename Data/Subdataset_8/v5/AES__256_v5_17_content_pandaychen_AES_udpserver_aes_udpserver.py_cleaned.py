import socket
import logging
import os
import time
import sys
import signal
import base64
from aes_main import CBCMode, AES
CONFIG = {
    "key": "1234567812345678",
    "iv": "1234567812345678",
    "max_udp_buffer": 8192,
    "log_dir": './logs/',
    "bind_ip": "127.0.0.1",
    "bind_port": 8888
}
packet_count = 0
def setup_logging():
    log_dir = CONFIG['log_dir']
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    cur_date = time.strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f'udp_server_{cur_date}.log')
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='[%(asctime)s] %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
def log_message(message, level=logging.INFO):
    if level == logging.ERROR:
        logging.error(message)
    else:
        logging.info(message)
def graceful_exit(signum, frame):
    global packet_count
    log_message(f"Received signal: {signum}; Total packets received: {packet_count}")
    sys.exit(0)
def bind_udp_server(bind_ip, bind_port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((bind_ip, bind_port))
        log_message(f"UDP Server bound to {bind_ip}:{bind_port}")
        return server_socket
    except socket.error as e:
        log_message(f"Failed to bind UDP server: {e}", logging.ERROR)
        sys.exit(1)
def udp_server_worker(server_socket):
    global packet_count
    max_udp_buffer = CONFIG['max_udp_buffer']
    while True:
        message, client_addr = server_socket.recvfrom(max_udp_buffer)
        if message:
            packet_count += 1
            log_message(f"Packet {packet_count} received from {client_addr}")
def decrypt_udp_packet(data_str):
    if data_str is None:
        return
    key, iv = CONFIG['key'], CONFIG['iv']
    b64decoded_str = base64.b64decode(data_str)
    decryptor = CBCMode(AES(key), iv)
    decrypted_str = decryptor.decrypt(b64decoded_str)
    return decrypted_str
if __name__ == "__main__":
    setup_logging()
    signal.signal(signal.SIGINT, graceful_exit)
    server_socket = bind_udp_server(CONFIG['bind_ip'], CONFIG['bind_port'])
    udp_server_worker(server_socket)