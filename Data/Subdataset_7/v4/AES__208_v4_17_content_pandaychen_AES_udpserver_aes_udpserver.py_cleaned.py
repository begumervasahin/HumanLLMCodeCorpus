import socket
import logging
import select
import signal
import sys
import os
import time
import json
import base64
from aes_main import CBCMode, AES
from aes_utils import _str_roundto16
from trans import *
b1 = "1234567812345678"
b2 = "1234567812345678"
a1 = 0
a2 = 8192
b3 = './logs/'
def fonk1():
    if not os.path.exists(b3):
        os.makedirs(b3)
    b4 = time.strftime("%Y%m%d")
    logging.basicConfig(b5 = os.path.join(b3, f'udp_server_{b4}.log'),
                        b6 = logging.INFO,
                        b7 = '[%(asctime)s] %(message)s',
                        b8 = '%Y-%m-%d %H:%M:%S')
def fonk2(message):
    logging.info(message)
def fonk3(signum, frame):
    fonk2(f"Received signal: {signum}; Total packets received: {a1}")
    sys.exit(1)
def fonk4(bind_ip, bind_port):
    try:
        b9 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        b9.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        b9.bind((bind_ip, bind_port))
        fonk2(f"Server bound to {bind_ip}:{bind_port}")
        return b9
    except socket.error as e:
        fonk2(f"Server bind error: {e}")
        sys.exit(1)
def fonk5(b9):
    global a1
    if b9 is None:
        fonk2("Server socket error")
        sys.exit(1)
    while True:
        message, b10 = b9.recvfrom(a2)
        if message:
            a1 += 1
            fonk2(f"Packet {a1} received from {b10}")
def fonk6(data_str):
    if data_str is None:
        return
    b11 = base64.b64decode(data_str)
    b12 = CBCMode(AES(b1), b2)
    b13 = b12.decrypt(b11)
    return b13
if b14 = = "__main__":
    fonk1()
    signal.signal(signal.SIGINT, user_exit)
    b15 = fonk4("127.0.0.1", 8888)
    fonk5(b15)