import socket
import threading
import re
b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
b2 = True
b3 = str(socket.gethostbyname(socket.gethostname()))
a1 = 1234
b4 = {}
b5 = {}
b1.bind((b3, a1))
b1.listen()
print('Server IP Address:', b3)
def fonk1(client_socket, client_username):
    b6 = True
    while b6:
        try:
            b7 = client_socket.recv(1024).decode('ascii')
            if not b7:
                break
            if '**quit' in b7:
                fonk2(client_socket, client_username)
                b6 = False
            elif '**get' in b7:
                fonk3(client_socket, client_username)
            elif '@' in b7:
                fonk4(client_socket, client_username, b7)
            else:
                fonk5(client_socket, client_username, b7)
        except Exception as e:
            fonk7(client_socket, client_username, e)
            b6 = False
def fonk2(client_socket, client_username):
    b8 = 'Goodbye!'
    client_socket.send(b8.encode('ascii'))
    b4.pop(client_username)
    print(f'{client_username} logged out from the server')
def fonk3(client_socket, client_username):
    for client_name, b15 in b5.items():
        if client_username != client_name:
            b8 = '!!' + b15
            client_socket.send(b8.encode('ascii'))
def fonk4(client_socket, client_username, b7):
    for client_name, socket_obj in b4.items():
        if client_username != client_name:
            b8 = '@' + b7
            socket_obj.send(b8.encode('ascii'))
def fonk5(client_socket, client_username, b7):
    for name, socket_obj in b4.items():
        if client_username != name:
            b9 = fonk6(client_username, b7)
            socket_obj.send(b9.encode('ascii'))
def fonk6(sender, b7):
    b10 = sender + '>>'
    b11 = b7.replace(b10, '')
    b12 = re.findall('..', b11)
    b13 = ''.join(chr(int(char, 16)) for char in b12)
    return b10 + b13
def fonk7(client_socket, client_username, error):
    b4.pop(client_username)
    print(f'{client_username} logged out from the server due to error:', error)
while b2:
    client_socket, b14 = b1.accept()
    client_username, b15 = [str(i) for i in client_socket.recv(1024).decode('ascii').split('\n')]
    print(f'{client_username} connected to the server with public key {b15}')
    client_socket.send('\nHello! Start chatting with your conversation partner!\n'.encode('ascii'))
    if client_socket not in b4:
        b4[client_username] = client_socket
        b5[client_username] = b15
        threading.Thread(b16 = handle_client_connection, args=(client_socket, client_username)).start()