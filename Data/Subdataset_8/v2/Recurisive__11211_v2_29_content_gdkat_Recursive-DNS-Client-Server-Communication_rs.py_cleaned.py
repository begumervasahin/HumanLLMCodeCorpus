import socket as mysoc
import sys
def main():
    com_host = sys.argv[1]
    edu_host = sys.argv[2]
    file_name = sys.argv[3]
    try:
        rssd = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        rstotscom = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        rstotsedu = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error: ', err)
        return
    try:
        fr = open(file_name, "r")
    except IOError as err:
        print('File Open Error: ', err)
        print("Please ensure the desired file to reverse exists in the source folder")
        return
    RS_table = {}
    edu = edu_host
    com = com_host
    if edu:
        RS_table[edu] = {'ip': mysoc.gethostbyname(edu), 'flag': 'NS'}
    if com:
        RS_table[com] = {'ip': mysoc.gethostbyname(com), 'flag': 'NS'}
    for line in fr:
        tokenize = line.split()
        if tokenize[1].strip() != '-':
            RS_table[tokenize[0].strip()] = {'ip': tokenize[1].strip(), 'flag': tokenize[2].strip()}
    try:
        server_binding = ('', 50008)
        rssd.bind(server_binding)
        rssd.listen(1)
    except mysoc.error as err:
        print('Socket bind error: ', err)
        return
    crsd, addr = rssd.accept()
    print('Got a connection request from a client at', addr)
    while True:
        data = crsd.recv(100)
        hnstring = data.decode('utf-8')
        if not hnstring:
            break
        entry = resolve_hostname(hnstring, RS_table, edu, com, rstotscom, rstotsedu)
        crsd.send(entry.encode('utf-8'))
    fr.close()
    rssd.close()
def resolve_hostname(hnstring, RS_table, edu, com, rstotscom, rstotsedu):
    if hnstring in RS_table:
        entry = hnstring + ' ' + RS_table[hnstring]['ip'] + ' ' + RS_table[hnstring]['flag']
    else:
        if ".edu" in hnstring:
            entry = resolve_TOTS(hnstring, edu, rstotsedu, RS_table)
        elif ".com" in hnstring:
            entry = resolve_TOTS(hnstring, com, rstotscom, RS_table)
        else:
            entry = hnstring + " - Error:HOST NOT FOUND"
    return entry
def resolve_TOTS(hnstring, host, rstots, RS_table):
    if not host:
        return hnstring + " - Error:HOST NOT FOUND"
    try:
        sa_sameas_myaddr = RS_table[host]['ip']
        port = 5678 if "com" in host else 5677
        server_binding = (sa_sameas_myaddr, port)
        rstots.connect(server_binding)
    except mysoc.error as err:
        print('TOTS connect error: ', err)
        exit()
    rstots.send(hnstring.strip().encode('utf-8'))
    dataFromTS = rstots.recv(100).decode('utf-8')
    return dataFromTS
if __name__ == '__main__':
    main()