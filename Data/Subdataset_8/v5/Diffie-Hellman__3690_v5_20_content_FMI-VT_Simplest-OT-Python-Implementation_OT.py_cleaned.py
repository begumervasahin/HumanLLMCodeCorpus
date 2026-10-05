from Crypto.Cipher import AES
import hashlib
import random
import sys
import socket
from ecc import getcurvebyname
HOST = "127.168.2.75"
PORT = 4446
def setup_server_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Listening for connections.. ")
    client_socket, addr = server_socket.accept()
    return client_socket
def setup_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    return client_socket
def send_data(socket, data):
    socket.send(data.encode())
def receive_message(socket):
    return socket.recv(1024).strip().decode('ascii')
def generate_random_curve_point(curve):
    return curve.G * random.randint(1, curve.order)
def get_user_input():
    user_input = []
    for i in range(10):
        input_data = input("Please enter something: ").ljust(32)
        print("You entered: " + input_data)
        user_input.append(input_data)
    return user_input
def generate_keys(curve, Alice, b, c):
    if c == 0:
        Bob = curve.G * b
    else:
        Bob = (Alice * c) + (curve.G * b)
    keys = [hashlib.blake2s() for _ in range(10)]
    for i in range(10):
        keys[i].update(str((Bob + (Alice * (-i))).mul(a)).encode())
        keys[i] = keys[i].digest()
    return keys
def encrypt_data(keys, data):
    cipher = [AES.new(key, AES.MODE_ECB) for key in keys]
    encrypted_data = [cipher[i].encrypt(data[i].encode()) for i in range(10)]
    return encrypted_data
def generate_bob_key(Alice, b):
    m = hashlib.blake2s()
    m.update(str(Alice * b).encode())
    return m.digest()
def decrypt_data(Bob_key, encrypted_data):
    cipher = AES.new(Bob_key, AES.MODE_ECB)
    decrypted_data = [cipher.decrypt(encrypted_data[i]).decode() for i in range(10)]
    return decrypted_data
curve = getcurvebyname("ed25519")
g = curve.G
a = random.randint(1, 2**255 - 19)
Alice = g * a
client_socket = setup_server_socket()
send_data(client_socket, input("Enter data to be sent: "))
client_socket.close()
client_socket = setup_client_socket()
message_from_server = receive_message(client_socket)
print("Message from server: " + message_from_server)
client_socket.close()
user_input = get_user_input()
b = random.randint(1, 2**255 - 19)
c = 2 if len(sys.argv) > 1 else int(sys.argv[1])
Bob_keys = generate_keys(curve, Alice, b, c)
encrypted_data = encrypt_data(Bob_keys, user_input)
Bob_key = generate_bob_key(Alice, b)
decrypted_data = decrypt_data(Bob_key, encrypted_data)
print('\nBob decrypts the messages:')
for i in range(10):
    print("message:", decrypted_data[i])