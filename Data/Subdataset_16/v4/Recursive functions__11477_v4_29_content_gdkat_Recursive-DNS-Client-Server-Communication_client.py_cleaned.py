import socket as mysoc
import sys
b1 = sys.argv[1]
b2 = sys.argv[2]
def fonk1():
    try:
        b3 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print(f'socket open error: {err}')
        return
    try:
        with open(b2, "r") as fr:
            b4 = fr.readlines()
    except IOError as err:
        print(f'File Open Error: {err}')
        print("Please ensure the desired file to reverse exists in the source folder")
        return
    b5 = mysoc.gethostbyname(b1)
    a1 = 50008
    try:
        b6 = (b5, a1)
        b3.connect(b6)
    except mysoc.error as err:
        print(f'connect error: {err}')
        return
    try:
        with open("RESOLVED.txt", "w") as fw:
            for hostname in b4:
                b3.send(hostname.strip().encode('utf-8'))
                b7 = b3.recv(100).decode('utf-8')
                if not b7:
                    break
                fw.write(b7 + '\n')
    except IOError as err:
        print(f'File Write Error: {err}')
    finally:
        b3.close()
if b8 = = "__main__":
    fonk1()