import socket
import threading
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
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
def fonk1(b11):
    b7 = AES.new(b1, AES.MODE_CBC, iv=b'16byteencryption')
    b8 = unpad(b7.decrypt(b11), AES.block_size)
    return b8.decode('utf-8')
def fonk2(client, uname):
    b9 = True
    b10 = b5.b10()
    while b9:
        try:
            b11 = client.recv(1024)
            if not b11:
                break
            b12 = fonk1(b11)
            if '**quit' in b12:
                b13 = 'Goodbye!'
                client.send(b13.encode('utf-8'))
                b5.pop(uname)
                print(uname + ' logged out from the server')
                b9 = False
            elif '**get' in b12:
                for i in b5:
                    if uname != i:
                        b13 = '!!' + b6[i]
                        client.send(b13.encode('utf-8'))
            elif '@' in b12:
                for i in b5:
                    if uname != i:
                        b13 = '@' + b12
                        b5[i].send(b13.encode('utf-8'))
            else:
                for name in b10:
                    if uname != name:
                        b14 = uname + '>>' + b12
                        print(b14)
                        b5[name].send(b14.encode('utf-8'))
        except Exception as e:
            print(e)
            b5.pop(uname)
            print(uname + ' logged out from the server')
            b9 = False
while b3:
    client, b15 = b2.accept()
    uname, b16 = [str(i) for i in client.recv(1024).decode('utf-8').split('\n')]
    print(str(uname), 'connected to the server with public key', str(b16))
    client.send('\nHello! Start chatting with your conversation partner!\n'.encode('utf-8'))
    if client not in b5:
        b5[uname] = client
        b6[uname] = b16
        threading.Thread(b17 = handle_client, args=(client, uname,)).start()