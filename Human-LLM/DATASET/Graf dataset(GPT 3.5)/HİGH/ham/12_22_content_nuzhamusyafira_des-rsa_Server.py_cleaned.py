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
print('IP Address Server: %b1'%b3)
def fonk1(client, uname):
    b6 = True
    b7 = b4.b7()
    while b6:
        try:
            b8 = client.recv(1024).decode('ascii')
            b9 = False
            if '**quit' in b8:
                b10 = 'Goodbye!'
                client.send(b10.encode('ascii'))
                b4.pop(uname)
                print(uname + ' logout dari server')
                b6 = False
            elif '**get' in b8:
                for i in b4:
                   if uname!=i:
                        b10 = '!!' + b5[i]
                        client.send(b10.encode('ascii'))
            elif '@' in b8:
                for i in b4:
                   if uname!=i:
                        b10 = '@' + b8
                        b4.get(i).send(b8.encode('ascii'))
            else:
                for name in b7:
                    if(uname!=name):
                        b11 = b8
                        b8 = uname +'>>'
                        print(b8, b12 = '')
                        b13 = b11
                        b13 = b13.replace(uname+'>>', '')
                        b13 = re.findall('..',b13)
                        for x in range(len(b13)):
                            b13[x]=chr(int(b13[x],16))
                        print(''.join(b13))
                        b8 = uname+'>>'
                        b4.get(name).send(b8.encode('ascii'))
                        b8 = b11
                        b8 = b8.replace(uname+'>>', '
                        b4.get(name).send(b8.encode('ascii'))
                        b9 = True
                if(not b9):
                    client.send('Gagal mengirim pesan, tidak ada lawan bicara.'.encode('ascii'))
        except:
            b4.pop(uname)
            print(uname + ' logout dari server')
            b6 = False
while b2:
    client, b14 = b1.accept()
    uname, b15 = [str(i) for i in client.recv(1024).decode('ascii').split('\n')]
    print(str(uname),'connected to the server with public key',str(b15))
    client.send('\nHalo! Mulai chat dengan lawan bicaramu!\n'.encode('ascii'))
    if(client not in b4):
        b4[uname] = client
        b5[uname] = b15
        threading.Thread(b16 = handleClient, args = (client, uname, )).start()