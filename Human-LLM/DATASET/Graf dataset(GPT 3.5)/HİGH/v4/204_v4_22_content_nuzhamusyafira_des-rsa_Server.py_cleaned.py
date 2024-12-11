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
def fonk1(client_socket, username):
    b6 = True
    b7 = b4.b7()
    while b6:
        try:
            b8 = client_socket.recv(1024).decode('ascii')
            b9 = False
            if '**quit' in b8:
                b10 = 'Goodbye!'
                client_socket.send(b10.encode('ascii'))
                b4.pop(username)
                print(username + ' logged out from the server')
                b6 = False
            elif '**get' in b8:
                for client_name in b4:
                    if username != client_name:
                        b10 = '!!' + b5[client_name]
                        client_socket.send(b10.encode('ascii'))
            elif '@' in b8:
                for client_name in b4:
                    if username != client_name:
                        b10 = '@' + b8
                        b4[client_name].send(b10.encode('ascii'))
            else:
                for name in b7:
                    if username != name:
                        b11 = b8
                        b8 = username + '>>'
                        print(b8, b12 = '')
                        b13 = b11.replace(username + '>>', '')
                        b13 = re.findall('..', b13)
                        for x in range(len(b13)):
                            b13[x] = chr(int(b13[x], 16))
                        print(''.join(b13))
                        b8 = username + '>>' + b11
                        b4[name].send(b8.encode('ascii'))
                        b9 = True
                if not b9:
                    client_socket.send('Gagal mengirim pesan, tidak ada lawan bicara.'.encode('ascii'))
        except:
            b4.pop(username)
            print(username + ' logged out from the server')
            b6 = False
while b2:
    client_socket, b14 = b1.accept()
    username, b15 = [str(i) for i in client_socket.recv(1024).decode('ascii').split('\n')]
    print(str(username), 'connected to the server with public key', str(b15))
    client_socket.send('\nHalo! Mulai chat dengan lawan bicaramu!\n'.encode('ascii'))
    if client_socket not in b4:
        b4[username] = client_socket
        b5[username] = b15
        threading.Thread(b16 = handle_client, args=(client_socket, username)).start()