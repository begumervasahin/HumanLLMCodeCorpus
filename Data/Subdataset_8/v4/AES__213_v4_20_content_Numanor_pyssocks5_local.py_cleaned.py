import sys
import argparse
import gevent
from gevent.server import StreamServer
from gevent import signal
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.Random import get_random_bytes
from utils.SSocket import SSocket
from utils.socks import SOCKS_VERSION_V, SOCKS_AUTH_NONE, SOCKS_REP_NET_ERO
class SecureSocksProxy(StreamServer):
    def __init__(self, listen_addr, args):
        super().__init__(listen_addr)
        self.remote_addr = (args.remote_ip, args.remote_port)
        self.load_crypto(args.remote_pub, args.private)
    def load_crypto(self, remote_pub_path, private_key_path):
        with open(remote_pub_path, 'r') as file:
            remote_pub_key = RSA.import_key(file.read())
        with open(private_key_path, 'r') as file:
            private_key = RSA.import_key(file.read())
        self.remote_cipher = PKCS1_OAEP.new(remote_pub_key)
        self.remote_verifier = pkcs1_15.new(remote_pub_key)
        self.local_cipher = PKCS1_OAEP.new(private_key)
        self.local_signer = pkcs1_15.new(private_key)
    def handle(self, socket, address):
        print(f'Connection from {address}')
        client = SSocket(socket=socket)
        version, n_methods = client.unpack('BB')
        if version != SOCKS_VERSION_V:
            client.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
            return
        methods = client.recv(n_methods)
        if SOCKS_AUTH_NONE not in methods:
            client.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
            return
        client.pack('BB', SOCKS_VERSION_V, SOCKS_AUTH_NONE)
        try:
            server = SSocket(addr=self.remote_addr)
        except IOError as ex:
            print(f"Failed to connect to remote server {self.remote_addr} from {address}: {ex}")
            client.pack('!BBBBIH', SOCKS_VERSION_V, SOCKS_REP_NET_ERO, 0x00, 0x01, 0, 0)
            return
        self.establish_secure_connection(client, server)
    def establish_secure_connection(self, client, server):
        aes_key, aes_iv = get_random_bytes(16), get_random_bytes(16)
        session_key = aes_key + aes_iv
        encrypted_session_key = self.remote_cipher.encrypt(session_key)
        server.sendall(encrypted_session_key)
        server.aes_init(aes_key, AES.MODE_CBC, aes_iv)
        hash_ = SHA256.new(session_key)
        signature = self.local_signer.sign(hash_)
        server.aes_send(signature)
        received_signature = server.aes_recv()
        hash_ = SHA256.new(session_key)
        if not self.remote_verifier.verify(hash_, received_signature):
            return
        gevent.spawn(client.aes_enc_forward, server)
        gevent.spawn(server.aes_dec_forward, client)
    def shutdown(self):
        print("Shutting down the server.")
        sys.exit(0)
    @staticmethod
    def start(args):
        proxy = SecureSocksProxy(('0.0.0.0', args.port), args)
        gevent.signal(signal.SIGTERM, proxy.shutdown)
        gevent.signal(signal.SIGINT, proxy.shutdown)
        print(f"Proxy server listening on 0.0.0.0:{args.port}")
        proxy.serve_forever()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Secure SOCKS5 Proxy Server")
    parser.add_argument('--port', type=int, default=9011)
    parser.add_argument('--remote_ip', default="127.0.0.1")
    parser.add_argument('--remote_port', type=int, default=9099)
    parser.add_argument('--remote_pub', default="keys/remote.pub")
    parser.add_argument('--private', default="keys/local")
    args = parser.parse_args()
    SecureSocksProxy.start(args)