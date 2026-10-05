import sys
import argparse
import gevent
from gevent.b11 import StreamServer
from gevent import signal
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
from utils.SSocket import SSocket
from utils.socks import SOCKS_VERSION_V, SOCKS_AUTH_NONE, SOCKS_REP_NET_ERO
class class1(StreamServer):
    def fonk1(self, listen_addr, b23):
        super().fonk1(listen_addr)
        self.b1 = (b23.remote_ip, b23.remote_port)
        self.fonk2(b23.remote_pub, b23.private)
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
        if version != SOCKS_VERSION_V:
            b8.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
            return
        b10 = b8.recv(b9)
        if SOCKS_AUTH_NONE not in b10:
            b8.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
            return
        b8.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
        try:
            b11 = SSocket(addr=self.b1)
        except IOError as ex:
            print(f"Failed to connect to remote b11 {self.b1} from {address}: {ex}")
            b8.pack('!BBBBIH', SOCKS_VERSION_V, SOCKS_REP_NET_ERO, 0x00, 0x01, 0, 0)
            return
        self.fonk4(b8, b11)
    def fonk4(self, b8, b11):
        aes_key, b12 = get_random_bytes(16), get_random_bytes(16)
        b13 = aes_key + b12
        b14 = self.b4.encrypt(b13)
        b11.sendall(b14)
        b11.aes_init(aes_key, AES.MODE_CBC, b12)
        b15 = SHA256.new(b13)
        b16 = self.b7.sign(b15)
        b11.aes_send(b16)
        b17 = b11.aes_recv()
        b15 = SHA256.new(b13)
        if not self.b5.verify(b15, b17):
            return
        gevent.spawn(b8.aes_enc_forward, b11)
        gevent.spawn(b11.aes_dec_forward, b8)
    def fonk5(self):
        print("Shutting down the b11.")
        sys.exit(0)
    @staticmethod
    def fonk6(b23):
        b18 = class1(('0.0.0.0', b23.port), b23)
        gevent.signal(signal.SIGTERM, b18.shutdown)
        gevent.signal(signal.SIGINT, b18.shutdown)
        print(f"Proxy b11 listening on 0.0.0.0:{b23.port}")
        b18.serve_forever()
if b19 = = '__main__':
    b20 = argparse.ArgumentParser(description="Secure SOCKS5 Proxy Server")
    b20.add_argument('--port', b21 = int, b22=9011)
    b20.add_argument('--remote_ip', b22 = "127.0.0.1")
    b20.add_argument('--remote_port', b21 = int, b22=9099)
    b20.add_argument('--remote_pub', b22 = "keys/remote.pub")
    b20.add_argument('--private', b22 = "keys/local")
    b23 = b20.parse_args()
    class1.fonk6(b23)