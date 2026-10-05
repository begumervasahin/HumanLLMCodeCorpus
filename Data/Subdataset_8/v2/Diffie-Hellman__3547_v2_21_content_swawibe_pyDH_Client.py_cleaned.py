import socket
from DiffieHellman import DiffieHellman
import json
class ClientSocket:
    def __init__(self, debug_flag):
        self.diffie_hellman = DiffieHellman()
        self.debug_flag = debug_flag
    def init_diffie_hellman(self, socket):
        socket.send("connected".encode())
        step1 = socket.recv(2048)
        if self.debug_flag:
            print(step1)
        json_data = json.loads(step1.decode())
        dh_key_exchange = json_data["dh-keyexchange"]
        self.diffie_hellman.base = int(dh_key_exchange["base"])
        self.diffie_hellman.shared_prime = int(dh_key_exchange["prime"])
        public_secret = int(dh_key_exchange["publicSecret"])
        calculated_public_secret = str(self.diffie_hellman.calc_public_secret())
        step2 = {
            "dh-keyexchange": {
                "step": 2,
                "publicSecret": calculated_public_secret
            }
        }
        socket.send(json.dumps(step2).encode())
        self.diffie_hellman.calc_shared_secret(public_secret)
    def start_client(self, ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, 20000))
            self.init_diffie_hellman(sock)
            print("The secret key is {}".format(self.diffie_hellman.key))
        finally:
            sock.close()
if __name__ == "__main__":
    client = ClientSocket(debug_flag=True)
    client.start_client("127.0.0.1")
