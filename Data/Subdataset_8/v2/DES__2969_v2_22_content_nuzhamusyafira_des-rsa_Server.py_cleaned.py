import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
encryption_key = b'secretencryptionk'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_running = True
ip = socket.gethostbyname(socket.gethostname())
port = 1234
clients = {}
client_public_keys = {}
server_socket.bind((ip, port))
server_socket.listen()
print('Server IP Address:', ip)
def decrypt_message(ciphertext):
    cipher = AES.new(encryption_key, AES.MODE_CBC, iv=b'16byteencryption')
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode('utf-8')
def handle_client(client_socket, username):
    client_connected = True
    while client_connected:
        try:
            ciphertext = client_socket.recv(1024)
            if not ciphertext:
                break
            decrypted_msg = decrypt_message(ciphertext)
            if '**quit' in decrypted_msg:
                response = 'Goodbye!'
                client_socket.send(response.encode('utf-8'))
                clients.pop(username)
                print(username + ' logged out from the server')
                client_connected = False
            elif '**get' in decrypted_msg:
                for client_name in clients:
                    if username != client_name:
                        response = '!!' + client_public_keys[client_name]
                        client_socket.send(response.encode('utf-8'))
            elif '@' in decrypted_msg:
                for client_name in clients:
                    if username != client_name:
                        response = '@' + decrypted_msg
                        clients[client_name].send(response.encode('utf-8'))
            else:
                for client_name in clients:
                    if username != client_name:
                        msg = username + '>>' + decrypted_msg
                        print(msg)
                        clients[client_name].send(msg.encode('utf-8'))
        except Exception as e:
            print(e)
            clients.pop(username)
            print(username + ' logged out from the server')
            client_connected = False
while server_running:
    client_socket, address = server_socket.accept()
    username, public_key = [str(i) for i in client_socket.recv(1024).decode('utf-8').split('\n')]
    print(str(username), 'connected to the server with public key', str(public_key))
    client_socket.send('\nHello! Start chatting with your conversation partner!\n'.encode('utf-8'))
    if client_socket not in clients:
        clients[username] = client_socket
        client_public_keys[username] = public_key
        threading.Thread(target=handle_client, args=(client_socket, username)).start()