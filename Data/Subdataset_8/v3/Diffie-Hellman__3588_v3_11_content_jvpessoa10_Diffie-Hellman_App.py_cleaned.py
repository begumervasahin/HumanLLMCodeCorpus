import socket
import threading
from DHCalculator import DHCalculator
from getIp import get_lan_ip
LOCAL_IP = ""
FIRST_CONNECTION_FLAG = False
G = 0
P = 0
class MessageReceiver(threading.Thread):
    def __init__(self, local_host, local_port):
        threading.Thread.__init__(self, name="MessageReceiver")
        self.host = local_host
        self.port = local_port
        self.data_received = ""
    def run(self):
        self._listen()
    def _listen(self):
        global FIRST_CONNECTION_FLAG, G, P
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(10)
        while True:
            connection, _ = sock.accept()
            try:
                full_message = ""
                while True:
                    data = connection.recv(16)
                    full_message += data.decode("utf-8")
                    if not data:
                        if full_message.count(",") == 1:
                            self.data_received = full_message.split(",")
                            print("Data received:", self.data_received)
                            G, P = map(int, self.data_received)
                            print("Transported P and G:", G, P)
                        break
            finally:
                connection.shutdown(2)
                connection.close()
class MessageSender(threading.Thread):
    def __init__(self, remote_host, remote_port):
        threading.Thread.__init__(self, name="MessageSender")
        self.host = remote_host
        self.port = remote_port
    def run(self):
        global FIRST_CONNECTION_FLAG, G, P
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.host, self.port))
                message = str(G) + "," + str(P)
                s.send(message.encode("utf-8"))
            except Exception:
                FIRST_CONNECTION_FLAG = True
                calculator = DHCalculator()
                G = calculator.generateGP()
                P = calculator.generateGP()
            else:
                print("Global P and G:", P, G)
                if (P and G) != 0:
                    print("Global P and G:", P, G)
                    s.shutdown(2)
                    s.close()
                    break
def execute():
    global LOCAL_IP
    calculator = DHCalculator()
    a = int(input("Type your local key:\n>> "))
    calculator.setA(a)
    local_port = int(input("Local PORT:"))
    remote_host = input("Remote IP:")
    remote_port = int(input("Remote PORT:"))
    print("Waiting for another peer")
    receiver = MessageReceiver(LOCAL_IP, local_port)
    sender = MessageSender(remote_host, remote_port)
    threads = [receiver.start(), sender.start()]
def main():
    global LOCAL_IP
    LOCAL_IP = get_lan_ip()
    dialog = input("Your IP is: " + LOCAL_IP + "? (y/n)\n>>")
    if dialog == "y":
        execute()
    elif dialog == "n":
        LOCAL_IP = input("Local IP:\n>>")
        execute()
    else:
        print("Invalid input!")
        main()
if __name__ == "__main__":
    main()