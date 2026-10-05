import socket as mysoc
import pickle
import sys
rs_host = sys.argv[1]
file_name = sys.argv[2]
def client():
    try:
        ctors=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
    try:
        fr = open(file_name, "r")
    except IOError as err:
        print('{} \n'.format("File Open Error ",err))
        print("Please ensure desired file to reverse exists in source folder")
        exit()
    sa_sameas_myaddr = mysoc.gethostbyname(rs_host)
    port = 50008
    try:
        server_binding=(sa_sameas_myaddr,port)
        ctors.connect(server_binding)
    except mysoc.error as err:
        print('{} \n'.format("connect error "), err)
        exit()
    with open("RESOLVED.txt", "w") as fw:
        for hostname in fr:
            ctors.send(hostname.strip().encode('utf-8'))
            dataFromRS=ctors.recv(100).decode('utf-8')
            if not dataFromRS: break
            fw.write(dataFromRS+'\n')
    fr.close()
    fw.close()
    ctors.close()
    exit()
client()