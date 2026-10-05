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
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8091
server.bind((host, port))
server.listen(5)
client, address = server.accept()
print(Colors.YELLOW + 'Connection from ' + str(address) + Colors.ENDC)
client.send(Colors.YELLOW + "We will use AES and SHA-256 for our key here!!" + Colors.ENDC)
print("We will use AES and SHA-256 for our key here!!" + Colors.ENDC)
print(Colors.YELLOW + "Waiting for confirmation..." + Colors.ENDC)
reply = client.recv(1024)
print(Colors.GREEN + reply.decode() + Colors.ENDC)
question = input(Colors.BLUE + "Ask a private question to your allies, Sir: " + Colors.ENDC)
client.send(encrypt(question, key))
client.send(sha256_hash(question))
valid_input = False
while not valid_input:
    number = int(input(Colors.BLUE + "Write a number between 3000 and 4000, Sir: " + Colors.ENDC))
    if 3000 < number < 4000:
        valid_input = True
        number = str(number)
    elif number < 3000:
        print(Colors.BOLD + "You are under 3000, Sir." + Colors.ENDC)
    else:
        print(Colors.BOLD + "You are writing a big number, Sir!" + Colors.ENDC)
client.send(number.encode())
print(Colors.YELLOW + "Waiting for answer..." + Colors.ENDC)
response = client.recv(1024)
answer = client.recv(1024)
decrypted_answer = decrypt(answer, key)
print(decrypted_answer)
decision = input("Is this the right answer? (y/n): ").upper()
if decision != 'Y':
    client.close()
    print(Colors.RED + "Access has been denied :)" + Colors.ENDC)
else:
    client.send("Everything is okay, we are here for orders, Sir!!".encode())
    print(Colors.YELLOW + "Waiting for orders..." + Colors.ENDC)
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("Encrypted message: " + str(data))
        order = decrypt(data, key).upper()
        print("Received: " + order)
        client.send(data)
client.close()
print(Colors.MOVE + "END OF COMMUNICATION, GOOD LUCK FOR WAR. MAY GOD PROTECT YOU!!" + Colors.ENDC)