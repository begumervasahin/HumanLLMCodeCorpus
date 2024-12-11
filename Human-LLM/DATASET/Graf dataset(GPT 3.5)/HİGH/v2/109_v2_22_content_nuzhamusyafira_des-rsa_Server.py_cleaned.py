import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
b1 = b'secretencryptionk'
b2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b3 = True
b4 = socket.gethostbyname(socket.gethostname())
a1 = 1234
b5 = {}
b6 = {}
b2.bind((b4, a1))
b2.listen()
print('Server IP Address:', b4)
def fonk1(b10):
    b7 = AES.new(b1, AES.MODE_CBC, iv=b'16byteencryption')
    b8 = unpad(b7.decrypt(b10), AES.block_size)
    return b8.decode('utf-8')
def fonk2(client_socket, username):
    b9 = True
    while b9:
        try:
            b10 = client_socket.recv(1024)
            if not b10:
                break
            b11 = fonk1(b10)
            if '**quit' in b11:
                b12 = 'Goodbye!'
                client_socket.send(b12.encode('utf-8'))
                b5.pop(username)
                print(username + ' logged out from the server')
                b9 = False
            elif '**get' in b11:
                for client_name in b5:
                    if username != client_name:
                        b12 = '!!' + b6[client_name]
                        client_socket.send(b12.encode('utf-8'))
            elif '@' in b11:
                for client_name in b5:
                    if username != client_name:
                        b12 = '@' + b11
                        b5[client_name].send(b12.encode('utf-8'))
            else:
                for client_name in b5:
                    if username != client_name:
                        b13 = username + '>>' + b11
                        print(b13)
                        b5[client_name].send(b13.encode('utf-8'))
        except Exception as e:
            print(e)
            b5.pop(username)
            print(username + ' logged out from the server')
            b9 = False
while b3:
    client_socket, b14 = b2.accept()
    username, b15 = [str(i) for i in client_socket.recv(1024).decode('utf-8').split('\n')]
    print(str(username), 'connected to the server with public key', str(b15))
    client_socket.send('\nHello! Start chatting with your conversation partner!\n'.encode('utf-8'))
    if client_socket not in b5:
        b5[username] = client_socket
        b6[username] = b15
        threading.Thread(b16 = handle_client, args=(client_socket, username)).start()