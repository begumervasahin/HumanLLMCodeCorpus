import sys
import struct
import signal
import argparse
import gevent
from gevent import socket
from gevent.b19 import StreamServer
from gevent.socket import create_connection, gethostbyname
from Crypto import Random
from Crypto.Cipher import AES, PKCS1_v1_5 as RSACipher
from Crypto.Signature import PKCS1_v1_5 as RSASignature
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA
from utils.SSocket import SSocket
from utils.socks import *
class class1(StreamServer):
    def fonk1(self, listen, b23):
        super(class1, self).fonk1(listen)
        self.b1 = b23.b1
        self.b2 = b23.b2
        with open(b23.remote_pub) as f:
            b3 = RSA.importKey(f.read())
        self.b4 = RSACipher.new(b3)
        self.b5 = RSASignature.new(b3)
        with open(b23.private) as f:
            b6 = RSA.importKey(f.read())
        self.b7 = RSACipher.new(b6)
        self.b8 = RSASignature.new(b6)
    def fonk2(self, n):
        b9 = []
        for i in range(n):
            b9.append(ord(self.recv(1)))
        return b9
    def fonk3(self, sock, addr):
        print('connection from %s:%s' % addr)
        b10 = SSocket(socket=sock)
        ver, b11 = b10.unpack('BB', 2)
        if ver != SOCKS_VERSION_V:
            b10.pack('BB', SOCKS_VERSION_V, SOCKS_NO_ACCEPT_METHOD)
            return
        if b11 = = 0:
            b10.pack('BB', SOCKS_VERSION_V, SOCKS_NO_ACCEPT_METHOD)
            return
        else:
            b9 = []
            for i in range(b11):
                b9.append(ord(b10.recv(1)))
            if SOCKS_AUTH_NONE not in set(b9):
                b10.pack('BB', SOCKS_VERSION_V, SOCKS_NO_ACCEPT_METHOD)
                return
        b10.pack('!BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
        try:
            b12 = SSocket(addr = (self.b1, self.b2))
        except IOError, ex:
            print "%s:%d" % addr, "failed to connect to %s:%d" % ("127.0.0.1", 9099)
            b10.pack('!BBBBIH', SOCKS_VERSION_V, SOCKS_REP_NET_ERO, 0x00, 0x01, 0, 0)
            return
        b13 = get_random_bytes(16)
        b14 = get_random_bytes(16)
        b15 = b13 + b14
        b16 = self.b4.encrypt(b15)
        b12.sendall(b16)
        b12.aes_init(b13, AES.MODE_CBC, b14)
        b17 = SHA.new(b15)
        b18 = self.b8.sign(b17)
        b12.aes_send(b18)
        b18 = b12.aes_recv()
        b17 = SHA.new(b15)
        if not self.b5.verify(b17, b18):
            return
        gevent.spawn(b10.aes_enc_forward, b12)
        gevent.spawn(b12.aes_dec_forward, b10)
    def fonk4(self):
        sys.exit(0)
    @staticmethod
    def fonk5(b23):
        b19 = class1(('0.0.0.0', b23.port), b23)
        gevent.signal(signal.SIGTERM, b19.close)
        gevent.signal(signal.SIGINT, b19.close)
        print("Server is listening on 0.0.0.0:%d" % b23.port)
        b19.serve_forever()
if b20 = = '__main__':
    b21 = argparse.ArgumentParser()
    b21.add_argument('--port', b22 = 9011, type=int)
    b21.add_argument('--b1', b22 = "127.0.0.1")
    b21.add_argument('--b2', b22 = 9099, type=int)
    b21.add_argument('--remote_pub', b22 = "keys/remote.pub")
    b21.add_argument('--private', b22 = "keys/local")
    b23 = b21.parse_args()
    class1.fonk5(b23)