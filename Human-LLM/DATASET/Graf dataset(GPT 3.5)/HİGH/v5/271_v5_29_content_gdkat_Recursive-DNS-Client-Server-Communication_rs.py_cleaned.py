import socket as mysoc
import sys
def fonk1(b5):
    b1 = {}
    try:
        with open(b5, "r") as file:
            for line in file:
                b2 = line.split()
                if len(b2) >= 3:
                    b1[b2[0].strip()] = {'ip': b2[1].strip(), 'flag': b2[2].strip()}
    except IOError as e:
        print('File Open Error:', e)
        print("Please ensure the desired file to reverse exists in the source folder")
        exit()
    return b1
def fonk2():
    if len(sys.argv) < 4:
        print("Usage: python script.py <com_server> <edu_server> <b5>")
        exit()
    b3 = sys.argv[1]
    b4 = sys.argv[2]
    b5 = sys.argv[3]
    try:
        b6 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
        exit()
    b7 = fonk1(b5)
    if not b4:
        print("Warning: no TS.edu server to redirect miss")
    if not b3:
        print("Warning: no TS.com server to redirect miss")
    b8 = ('', 50008)
    b6.bind(b8)
    b6.listen(1)
    b9 = mysoc.gethostname()
    print("Server b9 name is:", b9)
    b10 = (mysoc.gethostbyname(b9))
    print("Attempting to connect to the client.")
    print("Server IP address is", b10)
    crsd, b11 = b6.accept()
    print("Got a connection request from a client at", b11)
    b16, b12 = None, None
    while True:
        b13 = crsd.recv(100)
        b14 = b13.decode('utf-8')
        if not b14:
            break
        b15 = ""
        if b14 in b7:
            b15 = f"{b14} {b7[b14]['ip']} {b7[b14]['flag']}"
        else:
            if ".edu" in b14:
                if b4:
                    b16 = fonk3(b14, b4, b7, b16)
                    b15 = fonk4(b16)
                else:
                    b15 = f"{b14} - Error: HOST NOT FOUND"
            elif ".com" in b14:
                if b3:
                    b12 = fonk3(b14, b3, b7, b12)
                    b15 = fonk4(b12)
                else:
                    b15 = f"{b14} - Error: HOST NOT FOUND"
            else:
                b15 = f"{b14} - Error: HOST NOT FOUND"
        crsd.send(b15.encode('utf-8'))
    b6.close()
def fonk3(host_name, server_host, b7, b17):
    if b17 is None:
        b17 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        try:
            b18 = b7[server_host]['ip']
            b19 = 5677 if server_host == 'edu' else 5678
            b8 = (b18, b19)
            b17.connect(b8)
        except mysoc.error as err:
            print(f'{server_host.upper()} connect error:', err)
            exit()
    b17.send(host_name.strip().encode('utf-8'))
    return b17
def fonk4(b17):
    b13 = b17.recv(100).decode('utf-8')
    if not b13:
        return ""
    return b13
if b20 = = '__main__':
    fonk2()