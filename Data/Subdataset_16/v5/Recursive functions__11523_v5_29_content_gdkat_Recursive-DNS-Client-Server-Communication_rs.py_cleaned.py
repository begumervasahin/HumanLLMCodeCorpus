import socket as mysoc
import sys
def fonk1(b17, b18, b19):
    def fonk2():
        try:
            return mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        except mysoc.error as err:
            print('Socket creation error:', err)
            sys.exit()
    b1 = fonk2()
    b2 = fonk2()
    b3 = fonk2()
    try:
        with open(b19, "r") as fr:
            b4 = {
                b18: {'ip': mysoc.gethostbyname(b18), 'flag': 'NS'},
                b17: {'ip': mysoc.gethostbyname(b17), 'flag': 'NS'}
            }
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
        sys.exit()
    b6 = ('', 50008)
    b1.bind(b6)
    b1.listen(1)
    b7 = mysoc.gethostname()
    b8 = mysoc.gethostbyname(b7)
    print(f"[S]: Server b7 name is: {b7}")
    print(f"[S]: Server IP address is {b8}")
    crsd, b9 = b1.accept()
    print(f"[S]: Got a connection request from a client at {b9}")
    first_edu, b10 = True, True
    while True:
        b11 = crsd.recv(100)
        b12 = b11.decode('utf-8')
        if not b12:
            break
        b13 = fonk3(b12, b4, b18, b17, first_edu, b10, b3, b2)
        if b13:
            crsd.send(b13.encode('utf-8'))
    b1.close()
    b3.close()
    b2.close()
def fonk3(b12, b4, b18, b17, first_edu, b10, b3, b2):
    if b12 in b4:
        return f"{b12} {b4[b12]['ip']} {b4[b12]['flag']}"
    if ".edu" in b12:
        return fonk4(b12, b18, first_edu, b3, 5677)
    if ".com" in b12:
        return fonk4(b12, b17, b10, b2, 5678)
    return f"{b12} - Error: HOST NOT FOUND"
def fonk4(b12, b7, b14, rstots, port):
    if not b7:
        return f"{b12} - Error: HOST NOT FOUND"
    if b14:
        b14 = False
        try:
            b6 = (mysoc.gethostbyname(b7), port)
            rstots.connect(b6)
        except mysoc.error as err:
            print('TS connect error:', err)
            sys.exit()
    rstots.send(b12.strip().encode('utf-8'))
    b15 = rstots.recv(100).decode('utf-8')
    if not b15:
        return None
    return b15
if b16 = = '__main__':
    b17 = sys.argv[1]
    b18 = sys.argv[2]
    b19 = sys.argv[3]
    fonk1(b17, b18, b19)