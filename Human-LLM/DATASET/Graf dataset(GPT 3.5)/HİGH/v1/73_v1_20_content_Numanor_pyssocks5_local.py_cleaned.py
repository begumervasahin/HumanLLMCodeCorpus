import sys
import signal
import argparse
import gevent
from gevent.b11 import StreamServer
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from utils.SSocket import SSocket
from utils.socks import *
class class1(StreamServer):
    def fonk1(self, listen_addr, b15):
        super().fonk1(listen_addr)
        self.b1 = b15.b1
        self.b2 = b15.b2
        self.b3 = None
        self.b4 = None
        self.b5 = None
        self.b6 = None
        self.fonk2(b15.remote_pub, b15.private)
    def fonk2(self, remote_pub_path, local_private_path):
        with open(remote_pub_path, 'r') as f:
            b7 = RSA.import_key(f.read())
        self.b3 = PKCS1_OAEP.new(b7)
        self.b4 = pkcs1_15.new(b7)
        with open(local_private_path, 'r') as f:
            b8 = RSA.import_key(f.read())
        self.b5 = PKCS1_OAEP.new(b8)
        self.b6 = pkcs1_15.new(b8)
    def fonk3(self, sock, addr):
        print(f'Connection from {addr}')
        b9 = SSocket(socket=sock)
        try:
            b10 = SSocket(addr=(self.b1, self.b2))
        except IOError as ex:
            print(f"{addr} failed to connect to {self.b1}:{self.b2}")
            b9.send_error_reply()
            return
    def fonk4(self):
        sys.exit(0)
    @staticmethod
    def fonk5(b15):
        b11 = class1(('0.0.0.0', b15.port), b15)
        gevent.signal(signal.SIGTERM, b11.close)
        gevent.signal(signal.SIGINT, b11.close)
        print(f"Server is listening on 0.0.0.0:{b15.port}")
        b11.serve_forever()
if b12 = = '__main__':
    b13 = argparse.ArgumentParser()
    b13.add_argument('--port', b14 = 9011, type=int)
    b13.add_argument('--b1', b14 = "127.0.0.1")
    b13.add_argument('--b2', b14 = 9099, type=int)
    b13.add_argument('--remote_pub', b14 = "keys/remote.pub")
    b13.add_argument('--private', b14 = "keys/local")
    b15 = b13.parse_args()
    class1.fonk5(b15)