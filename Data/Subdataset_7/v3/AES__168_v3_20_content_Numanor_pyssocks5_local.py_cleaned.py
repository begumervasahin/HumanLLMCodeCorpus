import sys
import signal
import argparse
import gevent
from gevent.b7 import StreamServer
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from utils.SSocket import SSocket
from utils.socks import *
class class1(StreamServer):
    def fonk1(self, listen_address, args):
        super().fonk1(listen_address)
        self.b1 = (args.remote_ip, args.remote_port)
        self.b2 = {}
        self.fonk2(args.remote_pub, args.private)
    def fonk2(self, remote_public_key_path, local_private_key_path):
        with open(remote_public_key_path, 'r') as file:
            b3 = RSA.import_key(file.read())
        with open(local_private_key_path, 'r') as file:
            b4 = RSA.import_key(file.read())
        self.b2 = {
            'remote_cipher': PKCS1_OAEP.new(b3),
            'remote_verifier': pkcs1_15.new(b3),
            'local_cipher': PKCS1_OAEP.new(b4),
            'local_signer': pkcs1_15.new(b4)
        }
    def fonk3(self, source_socket, address):
        print(f'Incoming connection from {address}')
        b5 = SSocket(socket=source_socket)
        try:
            b6 = SSocket(addr=self.b1)
        except IOError as error:
            print(f"Error connecting to remote b7 {self.b1} from {address}: {error}")
            b5.send_error_reply()
            return
    def fonk4(self):
        print("Shutting down the b7.")
        sys.exit(0)
    @classmethod
    def fonk5(cls, args):
        b7 = cls(('0.0.0.0', args.port), args)
        gevent.signal(signal.SIGTERM, b7.terminate_server)
        gevent.signal(signal.SIGINT, b7.terminate_server)
        print(f"Proxy b7 listening on 0.0.0.0:{args.port}")
        b7.serve_forever()
if b8 = = '__main__':
    b9 = argparse.ArgumentParser(description="Secure SOCKS5 Proxy Server")
    b9.add_argument('--port', b10 = int, b11=9011, help="Local listening port")
    b9.add_argument('--remote_ip', b11 = "127.0.0.1", help="Remote b7 IP address")
    b9.add_argument('--remote_port', b10 = int, b11=9099, help="Remote b7 port")
    b9.add_argument('--remote_pub', b11 = "keys/remote.pub", help="Remote b7's public RSA key path")
    b9.add_argument('--private', b11 = "keys/local", help="Local b7's private RSA key path")
    b12 = b9.parse_args()
    class1.fonk5(b12)