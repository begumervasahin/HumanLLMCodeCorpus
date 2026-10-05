import socket as mysoc
import pickle
import sys
com_host = sys.argv[1]
edu_host = sys.argv[2]
file_name = sys.argv[3]
def rs():
    try:
        rssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('[RS]{} \n'.format("RS server socket open error ", err))
    try:
        rstotscom=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    try:
        rstotsedu=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('{} \n'.format("socket open error ", err))
    try:
        fr = open(file_name, "r")
    except IOError as err:
        print('{} \n'.format("File Open Error ",err))
        print("Please ensure desired file to reverse exists in source folder")
        exit()
    RS_table = {}
    edu = edu_host
    RS_table[edu] = {'ip': mysoc.gethostbyname(edu), 'flag':'NS'}
    com = com_host
    RS_table[com] = {'ip': mysoc.gethostbyname(com), 'flag':'NS'}
    for line in fr:
        tokenize = line.split()
        if tokenize[1].strip() == '-':
            pass
        RS_table[tokenize[0].strip()] = {'ip': tokenize[1].strip(), 'flag':tokenize[2].strip()}
        """ if RS_table[tokenize[0].strip()]['flag'] == 'NS':
            if ".edu" in tokenize[0].strip():
                edu = tokenize[0].strip()
            if ".com" in tokenize[0].strip():
                com = tokenize[0].strip() """
    if not edu:
        print("Warning, no TS.edu server to redirect miss\n")
    if not com:
        print("Warning, no TS.com server to redirect miss\n")
    server_binding = ('',50008)
    rssd.bind(server_binding)
    rssd.listen(1)
    host=mysoc.gethostname()
    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Attempting to connect to client.\n[S]: Server IP address is  ",localhost_ip)
    crsd,addr=rssd.accept()
    print ("[S]: Got a connection request from a client at", addr)
    firstEDU = True
    firstCOM = True
    while True:
        data=crsd.recv(100)
        hnstring=data.decode('utf-8')
        if not hnstring: break
        entry = ""
        if hnstring in RS_table:
            entry= hnstring + ' ' + RS_table[hnstring]['ip'] + ' ' + RS_table[hnstring]['flag']
        else:
            if ".edu" in hnstring:
                if not edu:
                    entry=hnstring + " - Error:HOST NOT FOUND"
                else:
                    if firstEDU:
                        firstEDU = False
                        try:
                            sa_sameas_myaddr = RS_table[edu]['ip']
                            port = 5677
                            server_binding = (sa_sameas_myaddr, port)
                            rstotsedu.connect(server_binding)
                        except mysoc.error as err:
                            print('{} \n'.format("TSEDU connect error "), err)
                            exit()
                    rstotsedu.send(hnstring.strip().encode('utf-8'))
                    dataFromTS=rstotsedu.recv(100).decode('utf-8')
                    if not dataFromTS: break
                    entry=dataFromTS
            elif ".com" in hnstring:
                if not com:
                    entry=hnstring + " - Error:HOST NOT FOUND"
                else:
                    if firstCOM:
                        firstCOM = False
                        try:
                            sa_sameas_myaddr = RS_table[com]['ip']
                            port = 5678
                            server_binding = (sa_sameas_myaddr, port)
                            rstotscom.connect(server_binding)
                        except mysoc.error as err:
                            print('{} \n'.format("TSCOM connect error "), err)
                            exit()
                    rstotscom.send(hnstring.strip().encode('utf-8'))
                    dataFromTS=rstotscom.recv(100).decode('utf-8')
                    if not dataFromTS: break
                    entry=dataFromTS
            else:
                entry=hnstring + " - Error:HOST NOT FOUND"
        crsd.send(entry.encode('utf-8'))
    fr.close()
    rssd.close()
rs()