import socket
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
class bcolors:
    MOVE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BBLUE = '\033[1m'
    UNDERLINE = '\033[4m'
def sha2(message):
    sha256 = SHA256.new()
    sha256.update(message.encode())
    hex_hash_sha256 = sha256.hexdigest()
    return hex_hash_sha256
def encrypt(message, key):
    cipher_aes = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    encrypted_aes = cipher_aes.encrypt(message.encode())
    return encrypted_aes
def decrypt(message, key):
    dec_cipher_aes = AES.new(key.encode(), AES.MODE_CFB, key.encode())
    decrypted_aes = dec_cipher_aes.decrypt(message)
    return decrypted_aes.decode()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8091
server.bind((host, port))
server.listen(5)
client, address = server.accept()
print(bcolors.YELLOW + 'Connection from ' + str(address) + bcolors.ENDC)
client.send(bcolors.YELLOW + "We will use AES and SHA-256 for our key here!!" + bcolors.ENDC)
print("We will use AES and SHA-256 for our key here!!" + bcolors.ENDC)
print(bcolors.YELLOW + "Waiting for confirmation..." + bcolors.ENDC)
rep = client.recv(1024)
print(bcolors.GREEN + rep.decode() + bcolors.ENDC)
question = input(bcolors.BLUE + "Ask a private question to your allies Sir: " + bcolors.ENDC)
client.send(encrypt(question, key))
client.send(sha2(question))
b = False
while not b:
    NA = int(input(bcolors.BLUE + "Write a number between 3000 and 4000 Sir: " + bcolors.ENDC))
    if 3000 < NA < 4000:
        b = True
        NA = str(NA)
    elif NA < 3000:
        print(bcolors.BBLUE + "You are under 3000 Sir" + bcolors.ENDC)
    else:
        print(bcolors.BBLUE + "You are writing a big number Sir!!" + bcolors.ENDC)
client.send(NA.encode())
print(bcolors.YELLOW + "Waiting for answer..." + bcolors.ENDC)
nb = client.recv(1024)
ans = client.recv(1024)
like = decrypt(ans, key)
print(like)
reject = input("This is the right answer y/n: ").upper()
if reject != 'Y':
    client.close()
    print(bcolors.RED + "Access has been denied :)" + bcolors.ENDC)
else:
    client.send("Every think is okay, we are here for order Sir !!".encode())
    print(bcolors.YELLOW + "Waiting for orders..." + bcolors.ENDC)
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("Crypted message: " + str(data))
        order = decrypt(data, key).upper()
        print("Received: " + order)
        client.send(data)
client.close()
print(bcolors.MOVE + "END OF COMMUNICATION, GOOD LUCK FOR WAR MAY GOD PROTECT YOU !!" + bcolors.ENDC)