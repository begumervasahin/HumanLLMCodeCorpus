import random
from Crypto.Cipher import AES
import socket
from time import time
host = '127.0.0.1'
port = 56739
buffersize = 4096
x_bob = 253
ServerSocketB = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ServerSocketB.bind((host, port))
def receive_message():
    data, addr = ServerSocketB.recvfrom(buffersize)
    print("The message is:", data)
    return data, addr
def perform_dh_key_exchange(sec_bob, q, a):
    y_bob = pow(a, sec_bob, q)
    return y_bob
def derive_shared_key(sec_bob, q, y_alice):
    k = pow(y_alice, sec_bob, q)
    return bin(k)[2:].zfill(24)
class AESCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, message):
        if len(message) % 16 == 0:
            plaintext = message.encode('utf-8')
        else:
            length = len(message)
            plaintext = (message + ((16 - length % 16) * str(0)))
            plaintext = plaintext.encode('utf-8')
        cipher = AES.new(self.key, AES.MODE_ECB)
        msg = cipher.encrypt(plaintext)
        return msg
    def decrypt(self, msg):
        decipher = AES.new(self.key, AES.MODE_ECB)
        plaintext = decipher.decrypt(msg)
        plaintext = plaintext.decode('utf-8')
        plaintext = plaintext.rstrip('0')
        return plaintext
def generate_nonce():
    return random.getrandbits(32)
while True:
    data, addr = receive_message()
    message = "Hey! Got your Message"
    ServerSocketB.sendto(message.encode(), addr)
    data, addr = receive_message()
    string = data.decode()
    a = int(string[0])
    q = int(string[2:7])
    y_alice = int(string[8:12])
    sec_bob = random.randint(1, q - 1)
    y_bob = perform_dh_key_exchange(sec_bob, q, a)
    ServerSocketB.sendto(str(y_bob).encode(), addr)
    shared_key = derive_shared_key(sec_bob, q, y_alice)
    data, addr = receive_message()
    initial_challenge = int(AESCipher(shared_key).decrypt(data))
    nonce = generate_nonce()
    response_challenge = nonce - 1
    response_message = f"{nonce},{response_challenge}"
    cipher_bob = AESCipher(shared_key).encrypt(response_message)
    ServerSocketB.sendto(cipher_bob, addr)
    data, addr = receive_message()
    final_challenge = int(AESCipher(shared_key).decrypt(data))
    if final_challenge == (nonce - 1):
        message = "authentication successful" * 6
        cipher_bob = AESCipher(shared_key).encrypt(message)
        end = time()
        print("The duration of AES 192 encryption:", end - start)
        ServerSocketB.sendto(cipher_bob, addr)
    else:
        message = "Authentication failure"
        ServerSocketB.sendto(message.encode(), addr)
        break
ServerSocketB.close()