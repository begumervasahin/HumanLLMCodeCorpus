import sys
import argparse
import gevent
from gevent.b10 import StreamServer
from gevent import signal
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
from utils.SSocket import SSocket
from utils.socks import SOCKS_VERSION_V, SOCKS_AUTH_NONE, SOCKS_REP_NET_ERO
class class1(StreamServer):
    def fonk1(self, listen_addr, b22):
        super().fonk1(listen_addr)
        self.b1 = (b22.remote_ip, b22.remote_port)
        self.fonk2(b22.remote_pub, b22.private)
    def fonk2(self, remote_pub_path, private_key_path):
        with open(remote_pub_path, 'r') as file:
            b2 = RSA.import_key(file.read())
        with open(private_key_path, 'r') as file:
            b3 = RSA.import_key(file.read())
        self.b4 = PKCS1_OAEP.new(b2)
        self.b5 = pkcs1_15.new(b2)
        self.b6 = PKCS1_OAEP.new(b3)
        self.b7 = pkcs1_15.new(b3)
    def fonk3(self, socket, address):
        print(f'Connection from {address}')
        b8 = SSocket(socket=socket)
        version, b9 = b8.unpack('BB')
        if version != SOCKS_VERSION_V or SOCKS_AUTH_NONE not in b8.recv(b9):
            b8.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
            return
        b8.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
        try:
            self.fonk4(b8, address)
        except Exception as ex:
            print(f"Error establishing secure connection: {ex}")
            b8.pack('!BBBBIH', SOCKS_VERSION_V, SOCKS_REP_NET_ERO, 0x00, 0x01, 0, 0)
    def fonk4(self, b8, address):
        b10 = SSocket(addr=self.b1)
        aes_key, b11 = get_random_bytes(16), get_random_bytes(16)
        b12 = aes_key + b11
        b13 = self.b4.encrypt(b12)
        b10.sendall(b13)
        b10.aes_init(aes_key, AES.MODE_CBC, b11)
        b14 = SHA256.new(b12)
        b15 = self.b7.sign(b14)
        b10.aes_send(b15)
        if not self.fonk5(b10, b12):
            raise ValueError("Signature verification failed.")
        gevent.spawn(b8.aes_enc_forward, b10)
        gevent.spawn(b10.aes_dec_forward, b8)
    def fonk5(self, b10, b12):
        b16 = b10.aes_recv()
        b14 = SHA256.new(b12)
        return self.b5.verify(b14, b16)
    def fonk6(self):
        print("Shutting down the b10.")
        sys.exit(0)
    @staticmethod
    def fonk7(b22):
        b17 = class1(('0.0.0.0', b22.port), b22)
        gevent.signal(signal.SIGTERM, b17.shutdown)
        gevent.signal(signal.SIGINT, b17.shutdown)
        print(f"Proxy b10 listening on 0.0.0.0:{b22.port}")
        b17.serve_forever()
if b18 = = '__main__':
    b19 = argparse.ArgumentParser(description="Secure SOCKS5 Proxy Server")
    b19.add_argument('--port', b20 = int, b21=9011)
    b19.add_argument('--remote_ip', b21 = "127.0.0.1")
    b19.add_argument('--remote_port', b20 = int, b21=9099)
    b19.add_argument('--remote_pub', b21 = "keys/remote.pub")
    b19.add_argument('--private', b21 = "keys/local")
    b22 = b19.parse_args()
    class1.fonk7(b22)