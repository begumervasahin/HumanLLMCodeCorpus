import socket
import threading
import re
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_running = True
server_ip = str(socket.gethostbyname(socket.gethostname()))
server_port = 1234
clients = {}
client_public_keys = {}
server_socket.bind((server_ip, server_port))
server_socket.listen()
print('Server IP Address:', server_ip)
def handle_client(client_socket, username):
    client_connected = True
    keys = clients.keys()
    while client_connected:
        try:
            msg = client_socket.recv(1024).decode('ascii')
            found = False
            if '**quit' in msg:
                response = 'Goodbye!'
                client_socket.send(response.encode('ascii'))
                clients.pop(username)
                print(username + ' logged out from the server')
                client_connected = False
            elif '**get' in msg:
                for client_name in clients:
                    if username != client_name:
                        response = '!!' + client_public_keys[client_name]
                        client_socket.send(response.encode('ascii'))
            elif '@' in msg:
                for client_name in clients:
                    if username != client_name:
                        response = '@' + msg
                        clients[client_name].send(response.encode('ascii'))
            else:
                for name in keys:
                    if username != name:
                        temp_msg = msg
                        msg = username + '>>'
                        print(msg, end='')
                        msg2 = temp_msg.replace(username + '>>', '')
                        msg2 = re.findall('..', msg2)
                        for x in range(len(msg2)):
                            msg2[x] = chr(int(msg2[x], 16))
                        print(''.join(msg2))
                        msg = username + '>>' + temp_msg
                        clients[name].send(msg.encode('ascii'))
                        found = True
                if not found:
                    client_socket.send('Gagal mengirim pesan, tidak ada lawan bicara.'.encode('ascii'))
        except:
            clients.pop(username)
            print(username + ' logged out from the server')
            client_connected = False
while server_running:
    client_socket, address = server_socket.accept()
    username, public_key = [str(i) for i in client_socket.recv(1024).decode('ascii').split('\n')]
    print(str(username), 'connected to the server with public key', str(public_key))
    client_socket.send('\nHalo! Mulai chat dengan lawan bicaramu!\n'.encode('ascii'))
    if client_socket not in clients:
        clients[username] = client_socket
        client_public_keys[username] = public_key
        threading.Thread(target=handle_client, args=(client_socket, username)).start()