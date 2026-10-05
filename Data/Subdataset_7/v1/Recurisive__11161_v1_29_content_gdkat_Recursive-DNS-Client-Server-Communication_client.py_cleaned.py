import socket as mysoc
import pickle
import sys
def fonk1():
    if len(sys.argv) != 3:
        print("Usage: python script.py [server_hostname] [b2]")
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    try:
        b3 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
        return
    try:
        b4 = open(b2, "r")
    except IOError as err:
        print('{} \n'.format("File Open Error ", err))
        print("Please ensure desired file to reverse exists in source folder")
        return
    b5 = mysoc.gethostbyname(b1)
    a1 = 50008
    try:
        b6 = (b5, a1)
        b3.connect(b6)
    except mysoc.error as err:
        print('{} \n'.format("connect error "), err)
        return
    with open("RESOLVED.txt", "w") as fw:
        for hostname in b4:
            b3.send(hostname.strip().encode('utf-8'))
            b7 = b3.recv(100).decode('utf-8')
            if not b7:
                break
            fw.write(b7+'\n')
    b4.close()
    fw.close()
    b3.close()
if b8 = = "__main__":
    fonk1()