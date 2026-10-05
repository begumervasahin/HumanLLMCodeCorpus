import socket
import threading
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
encryption_key = b'secretencryptionk'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_running = True
ip = socket.gethostbyname(socket.gethostname())
port = 1234
clients = {}
client_public_keys = {}
s.bind((ip, port))
s.listen()
print('Server IP Address:', ip)
def decrypt_message(ciphertext):
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv=b'16byteencryption')
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode('utf-8')
def handle_client(client, uname):
    client_connected = True
    keys = clients.keys()
    while client_connected:
        try:
            ciphertext = client.recv(1024)
            if not ciphertext:
                break
            decrypted_msg = decrypt_message(ciphertext)
            if '**quit' in decrypted_msg:
                response = 'Goodbye!'
                client.send(response.encode('utf-8'))
                clients.pop(uname)
                print(uname + ' logged out from the server')
                client_connected = False
            elif '**get' in decrypted_msg:
                for i in clients:
                    if uname != i:
                        response = '!!' + client_public_keys[i]
                        client.send(response.encode('utf-8'))
            elif '@' in decrypted_msg:
                for i in clients:
                    if uname != i:
                        response = '@' + decrypted_msg
                        clients[i].send(response.encode('utf-8'))
            else:
                for name in keys:
                    if uname != name:
                        msg = uname + '>>' + decrypted_msg
                        print(msg)
                        clients[name].send(msg.encode('utf-8'))
        except Exception as e:
            print(e)
            clients.pop(uname)
            print(uname + ' logged out from the server')
            client_connected = False
while server_running:
    client, address = s.accept()
    uname, public_key_client = [str(i) for i in client.recv(1024).decode('utf-8').split('\n')]
    print(str(uname), 'connected to the server with public key', str(public_key_client))
    client.send('\nHello! Start chatting with your conversation partner!\n'.encode('utf-8'))
    if client not in clients:
        clients[uname] = client
        client_public_keys[uname] = public_key_client
        threading.Thread(target=handle_client, args=(client, uname,)).start()