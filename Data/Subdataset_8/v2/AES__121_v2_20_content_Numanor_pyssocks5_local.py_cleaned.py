import sys
import signal
import argparse
import gevent
from gevent.server import StreamServer
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from utils.SSocket import SSocket
from utils.socks import *
class SocksLocalServer(StreamServer):
    def __init__(self, listen_addr, args):
        super().__init__(listen_addr)
        self.remote_ip = args.remote_ip
        self.remote_port = args.remote_port
        self.remote_cipher, self.remote_verifier, self.local_cipher, self.local_signer = None, None, None, None
        self.load_keys(args.remote_pub, args.private)
    def load_keys(self, remote_pub_path, local_private_path):
        with open(remote_pub_path, 'r') as file:
            remote_pubkey = RSA.import_key(file.read())
        self.remote_cipher = PKCS1_OAEP.new(remote_pubkey)
        self.remote_verifier = pkcs1_15.new(remote_pubkey)
        with open(local_private_path, 'r') as file:
            private_key = RSA.import_key(file.read())
        self.local_cipher = PKCS1_OAEP.new(private_key)
        self.local_signer = pkcs1_15.new(private_key)
    def handle(self, sock, addr):
        print(f'Connection from {addr}')
        src = SSocket(socket=sock)
        try:
            dest = SSocket(addr=(self.remote_ip, self.remote_port))
        except IOError as ex:
            print(f"Failed to connect to {self.remote_ip}:{self.remote_port} from {addr}")
            src.send_error_reply()
            return
    def close(self):
        sys.exit(0)
    @staticmethod
    def start_server(args):
        server = SocksLocalServer(('0.0.0.0', args.port), args)
        gevent.signal(signal.SIGTERM, server.close)
        gevent.signal(signal.SIGINT, server.close)
        print(f"Server is listening on 0.0.0.0:{args.port}")
        server.serve_forever()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SOCKS5 Proxy Server")
    parser.add_argument('--port', help="Local listening port", default=9011, type=int)
    parser.add_argument('--remote_ip', help="Remote server IP address", default="127.0.0.1")
    parser.add_argument('--remote_port', help="Remote server port", default=9099, type=int)
    parser.add_argument('--remote_pub', help="Path to remote server's public RSA key", default="keys/remote.pub")
    parser.add_argument('--private', help="Path to local server's private RSA key", default="keys/local")
    args = parser.parse_args()
    SocksLocalServer.start_server(args)