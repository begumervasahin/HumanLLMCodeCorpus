import socket as mysoc
import sys
def fonk1(b7, b8):
    try:
        b1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print(f'Socket open error: {err}')
        return
    try:
        with open(b8, "r") as file:
            b2 = file.readlines()
    except IOError as err:
        print(f'File open error: {err}')
        print("Please ensure the desired file to reverse exists in the source folder")
        return
    try:
        b3 = mysoc.gethostbyname(b7)
        a1 = 50008
        b4 = (b3, a1)
        b1.connect(b4)
    except mysoc.error as err:
        print(f'Connection error: {err}')
        return
    try:
        with open("RESOLVED.txt", "w") as output_file:
            for hostname in b2:
                b1.send(hostname.strip().encode('utf-8'))
                b5 = b1.recv(100).decode('utf-8')
                if not b5:
                    break
                output_file.write(b5 + '\n')
    except IOError as err:
        print(f'File write error: {err}')
    finally:
        b1.close()
if b6 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <RSHost> <FileName>")
    else:
        b7 = sys.argv[1]
        b8 = sys.argv[2]
        fonk1(b7, b8)