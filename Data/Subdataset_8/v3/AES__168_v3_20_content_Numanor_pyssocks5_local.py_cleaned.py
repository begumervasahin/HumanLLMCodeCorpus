import sys
import signal
import argparse
import gevent
from gevent.server import StreamServer
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from utils.SSocket import SSocket
from utils.socks import *
class SecureSocksProxy(StreamServer):
    def __init__(self, listen_address, args):
        super().__init__(listen_address)
        self.remote_address = (args.remote_ip, args.remote_port)
        self.encryption_tools = {}
        self.load_encryption_keys(args.remote_pub, args.private)
    def load_encryption_keys(self, remote_public_key_path, local_private_key_path):
        with open(remote_public_key_path, 'r') as file:
            remote_public_key = RSA.import_key(file.read())
        with open(local_private_key_path, 'r') as file:
            local_private_key = RSA.import_key(file.read())
        self.encryption_tools = {
            'remote_cipher': PKCS1_OAEP.new(remote_public_key),
            'remote_verifier': pkcs1_15.new(remote_public_key),
            'local_cipher': PKCS1_OAEP.new(local_private_key),
            'local_signer': pkcs1_15.new(local_private_key)
        }
    def handle(self, source_socket, address):
        print(f'Incoming connection from {address}')
        source = SSocket(socket=source_socket)
        try:
            destination = SSocket(addr=self.remote_address)
        except IOError as error:
            print(f"Error connecting to remote server {self.remote_address} from {address}: {error}")
            source.send_error_reply()
            return
    def terminate_server(self):
        print("Shutting down the server.")
        sys.exit(0)
    @classmethod
    def run(cls, args):
        server = cls(('0.0.0.0', args.port), args)
        gevent.signal(signal.SIGTERM, server.terminate_server)
        gevent.signal(signal.SIGINT, server.terminate_server)
        print(f"Proxy server listening on 0.0.0.0:{args.port}")
        server.serve_forever()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Secure SOCKS5 Proxy Server")
    parser.add_argument('--port', type=int, default=9011, help="Local listening port")
    parser.add_argument('--remote_ip', default="127.0.0.1", help="Remote server IP address")
    parser.add_argument('--remote_port', type=int, default=9099, help="Remote server port")
    parser.add_argument('--remote_pub', default="keys/remote.pub", help="Remote server's public RSA key path")
    parser.add_argument('--private', default="keys/local", help="Local server's private RSA key path")
    arguments = parser.parse_args()
    SecureSocksProxy.run(arguments)