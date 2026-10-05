import socket
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
class Colors:
    MOVE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def sha256_hash(message):
    sha256 = SHA256.new()
    sha256.update(message.encode())
    return sha256.hexdigest()
def encrypt(message, key):
    cipher = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    return cipher.encrypt(message.encode())
def decrypt(message, key):
    cipher = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    decrypted_message = cipher.decrypt(message)
    return decrypted_message.decode()
def accept_connection(server_socket):
    client, address = server_socket.accept()
    print(Colors.YELLOW + 'Connection from ' + str(address) + Colors.ENDC)
    return client
def send_message(client, message):
    client.send(message.encode())
def receive_message(client):
    return client.recv(1024)
def get_confirmation():
    return input(Colors.YELLOW + "Waiting for confirmation..." + Colors.ENDC)
def get_input(prompt):
    return input(prompt)
def print_message(message):
    print(message)
def print_encrypted_message(message):
    print("Encrypted message: " + str(message))
def print_decrypted_message(message):
    print("Received: " + message)
def is_valid_number(number):
    return 3000 < number < 4000
def is_correct_answer(decision):
    return decision == 'Y'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8091
server.bind((host, port))
server.listen(5)
client = accept_connection(server)
send_message(client, Colors.YELLOW + "We will use AES and SHA-256 for our key here!!" + Colors.ENDC)
print_message("We will use AES and SHA-256 for our key here!!" + Colors.ENDC)
reply = receive_message(client)
print_message(Colors.GREEN + reply.decode() + Colors.ENDC)
question = get_input(Colors.BLUE + "Ask a private question to your allies, Sir: " + Colors.ENDC)
send_message(client, encrypt(question, key))
send_message(client, sha256_hash(question))
valid_input = False
while not valid_input:
    number = int(get_input(Colors.BLUE + "Write a number between 3000 and 4000, Sir: " + Colors.ENDC))
    if is_valid_number(number):
        valid_input = True
        number = str(number)
    elif number < 3000:
        print(Colors.BOLD + "You are under 3000, Sir." + Colors.ENDC)
    else:
        print(Colors.BOLD + "You are writing a big number, Sir!" + Colors.ENDC)
send_message(client, number)
print_message(Colors.YELLOW + "Waiting for answer..." + Colors.ENDC)
response = receive_message(client)
answer = receive_message(client)
decrypted_answer = decrypt(answer, key)
print_decrypted_message(decrypted_answer)
decision = get_input("Is this the right answer? (y/n): ").upper()
if is_correct_answer(decision):
    send_message(client, "Everything is okay, we are here for orders, Sir!!".encode())
    print_message(Colors.YELLOW + "Waiting for orders..." + Colors.ENDC)
    while True:
        data = receive_message(client)
        if not data:
            break
        print_encrypted_message(data)
        order = decrypt(data, key).upper()
        print_decrypted_message(order)
client.close()
print(Colors.MOVE + "END OF COMMUNICATION, GOOD LUCK FOR WAR. MAY GOD PROTECT YOU!!" + Colors.ENDC)