import socket as mysoc
import pickle
import sys
rs_host = sys.argv[1]
file_name = sys.argv[2]
def client():
    try:
        ctors = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("Socket open error ", err))
    try:
        fr = open(file_name, "r")
    except IOError as err:
        print('{} \n'.format("File open error ", err))
        print("Please ensure the desired file to reverse exists in the source folder")
        exit()
    sa_sameas_myaddr = mysoc.gethostbyname(rs_host)
    port = 50008
    try:
        server_binding = (sa_sameas_myaddr, port)
        ctors.connect(server_binding)
    except mysoc.error as err:
        print('{} \n'.format("Connect error "), err)
        exit()
    with open("RESOLVED.txt", "w") as fw:
        for hostname in fr:
            ctors.send(hostname.strip().encode('utf-8'))
            data_from_rs = ctors.recv(100).decode('utf-8')
            if not data_from_rs:
                break
            fw.write(data_from_rs + '\n')
    fr.close()
    fw.close()
    ctors.close()
    exit()
client()