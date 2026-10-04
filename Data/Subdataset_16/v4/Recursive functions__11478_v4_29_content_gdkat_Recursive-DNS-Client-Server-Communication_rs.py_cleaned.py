import socket as mysoc
import sys
def fonk1(b18, b19, b20):
    try:
        b1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('[RS] RS server socket open error:', err)
        return
    try:
        b2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
        return
    try:
        b3 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
        return
    try:
        with open(b20, "r") as fr:
            b4 = {}
            b4[b19] = {'ip': mysoc.gethostbyname(b19), 'flag': 'NS'}
            b4[b18] = {'ip': mysoc.gethostbyname(b18), 'flag': 'NS'}
            for line in fr:
                b5 = line.split()
                if b5[1].strip() != '-':
                    b4[b5[0].strip()] = {
                        'ip': b5[1].strip(),
                        'flag': b5[2].strip()
                    }
    except IOError as err:
        print('File Open Error:', err)
        print("Please ensure the desired file exists in the source folder")
        return
    b6 = ('', 50008)
    b1.bind(b6)
    b1.listen(1)
    b7 = mysoc.gethostname()
    b8 = mysoc.gethostbyname(b7)
    print(f"[S]: Server b7 name is: {b7}")
    print(f"[S]: Attempting to connect to client.\n[S]: Server IP address is {b8}")
    crsd, b9 = b1.accept()
    print(f"[S]: Got a connection request from a client at {b9}")
    b10 = True
    b11 = True
    while True:
        b12 = crsd.recv(100)
        b13 = b12.decode('utf-8')
        if not b13:
            break
        b14 = ""
        if b13 in b4:
            b14 = f"{b13} {b4[b13]['ip']} {b4[b13]['flag']}"
        else:
            if ".edu" in b13:
                if not b19:
                    b14 = f"{b13} - Error: HOST NOT FOUND"
                else:
                    if b10:
                        b10 = False
                        try:
                            b15 = b4[b19]['ip']
                            a1 = 5677
                            b6 = (b15, a1)
                            b3.connect(b6)
                        except mysoc.error as err:
                            print('TSEDU connect error:', err)
                            return
                    b3.send(b13.strip().encode('utf-8'))
                    b16 = b3.recv(100).decode('utf-8')
                    if not b16:
                        break
                    b14 = b16
            elif ".com" in b13:
                if not b18:
                    b14 = f"{b13} - Error: HOST NOT FOUND"
                else:
                    if b11:
                        b11 = False
                        try:
                            b15 = b4[b18]['ip']
                            a1 = 5678
                            b6 = (b15, a1)
                            b2.connect(b6)
                        except mysoc.error as err:
                            print('TSCOM connect error:', err)
                            return
                    b2.send(b13.strip().encode('utf-8'))
                    b16 = b2.recv(100).decode('utf-8')
                    if not b16:
                        break
                    b14 = b16
            else:
                b14 = f"{b13} - Error: HOST NOT FOUND"
        crsd.send(b14.encode('utf-8'))
    b1.close()
    b3.close()
    b2.close()
if b17 = = '__main__':
    b18 = sys.argv[1]
    b19 = sys.argv[2]
    b20 = sys.argv[3]
    fonk1(b18, b19, b20)