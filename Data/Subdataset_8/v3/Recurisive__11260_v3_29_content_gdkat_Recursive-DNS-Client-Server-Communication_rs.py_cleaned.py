import socket as mysoc
import sys
TOTS_PORT_COM = 5678
TOTS_PORT_EDU = 5677
def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <com_host> <edu_host> <file_name>")
        return
    com_host = sys.argv[1]
    edu_host = sys.argv[2]
    file_name = sys.argv[3]
    rssd = create_socket()
    rstotscom = create_socket()
    rstotsedu = create_socket()
    RS_table = initialize_dns_table(file_name, edu_host, com_host)
    bind_socket(rssd)
    crsd, addr = rssd.accept()
    print('Got a connection request from a client at', addr)
    process_requests(crsd, RS_table, edu_host, com_host, rstotscom, rstotsedu)
    rssd.close()
def create_socket():
    try:
        return mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error: ', err)
        sys.exit()
def initialize_dns_table(file_name, edu_host, com_host):
    RS_table = {}
    try:
        with open(file_name, "r") as fr:
            for line in fr:
                tokenize = line.split()
                if tokenize[1].strip() != '-':
                    RS_table[tokenize[0].strip()] = {'ip': tokenize[1].strip(), 'flag': tokenize[2].strip()}
    except IOError as err:
        print('File Open Error: ', err)
        print("Please ensure the desired file to reverse exists in the source folder")
        sys.exit()
    add_to_dns_table(RS_table, edu_host, mysoc.gethostbyname(edu_host), 'NS')
    add_to_dns_table(RS_table, com_host, mysoc.gethostbyname(com_host), 'NS')
    return RS_table
def add_to_dns_table(RS_table, host, ip, flag):
    if host:
        RS_table[host] = {'ip': ip, 'flag': flag}
def bind_socket(sock):
    try:
        server_binding = ('', 50008)
        sock.bind(server_binding)
        sock.listen(1)
    except mysoc.error as err:
        print('Socket bind error: ', err)
        sys.exit()
def process_requests(crsd, RS_table, edu_host, com_host, rstotscom, rstotsedu):
    while True:
        data = crsd.recv(100)
        hnstring = data.decode('utf-8')
        if not hnstring:
            break
        entry = resolve_hostname(hnstring, RS_table, edu_host, com_host, rstotscom, rstotsedu)
        crsd.send(entry.encode('utf-8'))
def resolve_hostname(hnstring, RS_table, edu_host, com_host, rstotscom, rstotsedu):
    if hnstring in RS_table:
        entry = f"{hnstring} {RS_table[hnstring]['ip']} {RS_table[hnstring]['flag']}"
    else:
        if ".edu" in hnstring:
            entry = resolve_TOTS(hnstring, edu_host, rstotsedu, RS_table)
        elif ".com" in hnstring:
            entry = resolve_TOTS(hnstring, com_host, rstotscom, RS_table)
        else:
            entry = f"{hnstring} - Error:HOST NOT FOUND"
    return entry
def resolve_TOTS(hnstring, host, rstots, RS_table):
    if not host:
        return f"{hnstring} - Error:HOST NOT FOUND"
    try:
        sa_sameas_myaddr = RS_table[host]['ip']
        port = TOTS_PORT_COM if "com" in host else TOTS_PORT_EDU
        server_binding = (sa_sameas_myaddr, port)
        rstots.connect(server_binding)
    except mysoc.error as err:
        print('TOTS connect error: ', err)
        sys.exit()
    rstots.send(hnstring.strip().encode('utf-8'))
    dataFromTS = rstots.recv(100).decode('utf-8')
    return dataFromTS
if __name__ == '__main__':
    main()