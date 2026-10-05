import random
import socket
from Crypto.Cipher import AES
from time import time
HOST = '127.0.0.1'
PORT = 56739
BUFFER_SIZE = 4096
X_BOB = 253
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
while True:
    data, addr = server_socket.recvfrom(BUFFER_SIZE)
    print("Received message:", data.decode())
    ack_message = "Hey! Got your Message"
    server_socket.sendto(ack_message.encode(), addr)
    data = server_socket.recvfrom(BUFFER_SIZE)[0]
    print("Received Diffie-Hellman parameters:", data.decode())
    a, q, y_alice = map(int, data.decode().split())
    y_bob = (a ** X_BOB) % q
    print("Y_bob:", y_bob)
    server_socket.sendto(str(y_bob).encode(), addr)
    k = (y_alice ** X_BOB) % q
    shared_key = bin(k)[2:].zfill(32)
    aes_cipher = AESCipher(shared_key)
    data = server_socket.recvfrom(BUFFER_SIZE)[0]
    initial_challenge = int(aes_cipher.decrypt(data))
    print("Initial challenge received from Alice:", initial_challenge)
    nonce = random.getrandbits(32)
    initial_challenge -= 1
    challenge_message = f"{nonce},{initial_challenge}"
    encrypted_challenge = aes_cipher.encrypt(challenge_message)
    print("First challenge message sent:", nonce, encrypted_challenge)
    server_socket.sendto(encrypted_challenge, addr)
    data = server_socket.recvfrom(BUFFER_SIZE)[0]
    final_challenge = int(aes_cipher.decrypt(data))
    print("Final challenge received:", final_challenge)
    if final_challenge == (nonce - 1):
        print("Authentication successful")
        success_message = "authentication successful" * 6
        encrypted_success_message = aes_cipher.encrypt(success_message)
        server_socket.sendto(encrypted_success_message, addr)
    else:
        print("Authentication failure")
        failure_message = "Authentication failure"
        server_socket.sendto(failure_message.encode(), addr)
        break
server_socket.close()
class AESCipher:
    def __init__(self, key):
        self.key = key
    def encrypt(self, message):
        plaintext = message.encode('utf-8')
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_ECB)
        return cipher.encrypt(plaintext)
    def decrypt(self, ciphertext):
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext)
        return plaintext.decode('utf-8').rstrip('\x00')