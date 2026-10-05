import socket
import logging
import os
import time
import sys
import signal
import base64
from aes_main import CBCMode, AES
b1 = {
    "key": "1234567812345678",
    "b12": "1234567812345678",
    "b10": 8192,
    "b2": './logs/',
    "bind_ip": "127.0.0.1",
    "bind_port": 8888
}
a1 = 0
def fonk1():
    b2 = b1['b2']
    if not os.path.exists(b2):
        os.makedirs(b2)
    b3 = time.strftime("%Y%m%d")
    b4 = os.path.join(b2, f'udp_server_{b3}.log')
    logging.basicConfig(b5 = b4, b8=logging.INFO,
                        b6 = '[%(asctime)s] %(levelname)s: %(message)s',
                        b7 = '%Y-%m-%d %H:%M:%S')
def fonk2(message, b8 = logging.INFO):
    if b8 = = logging.ERROR:
        logging.error(message)
    else:
        logging.info(message)
def fonk3(signum, frame):
    global a1
    fonk2(f"Received signal: {signum}; Total packets received: {a1}")
    sys.exit(0)
def fonk4(bind_ip, bind_port):
    try:
        b9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        b9.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        b9.bind((bind_ip, bind_port))
        fonk2(f"UDP Server bound to {bind_ip}:{bind_port}")
        return b9
    except socket.error as e:
        fonk2(f"Failed to bind UDP server: {e}", logging.ERROR)
        sys.exit(1)
def fonk5(b9):
    global a1
    b10 = b1['b10']
    while True:
        message, b11 = b9.recvfrom(b10)
        if message:
            a1 += 1
            fonk2(f"Packet {a1} received from {b11}")
def fonk6(data_str):
    if data_str is None:
        return
    key, b12 = b1['key'], b1['b12']
    b13 = base64.b64decode(data_str)
    b14 = CBCMode(AES(key), b12)
    b15 = b14.decrypt(b13)
    return b15
if b16 = = "__main__":
    fonk1()
    signal.signal(signal.SIGINT, graceful_exit)
    b9 = fonk4(b1['bind_ip'], b1['bind_port'])
    fonk5(b9)