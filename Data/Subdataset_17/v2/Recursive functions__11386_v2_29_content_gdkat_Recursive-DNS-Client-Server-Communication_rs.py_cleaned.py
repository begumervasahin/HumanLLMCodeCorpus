import socket as mysoc
import sys
com_host = sys.argv[1]
edu_host = sys.argv[2]
file_name = sys.argv[3]
def load_rs_table(file_name, edu_host, com_host):
    RS_table = {
        edu_host: {'ip': mysoc.gethostbyname(edu_host), 'flag': 'NS'},
        com_host: {'ip': mysoc.gethostbyname(com_host), 'flag': 'NS'}
    }
    try:
        with open(file_name, "r") as file:
            for line in file:
                tokens = line.split()
                if tokens[1].strip() != '-':
                    RS_table[tokens[0].strip()] = {'ip': tokens[1].strip(), 'flag': tokens[2].strip()}
    except IOError as err:
        print('File Open Error:', err)
        print("Please ensure the file exists in the source folder")
        sys.exit(1)
    return RS_table
def initialize_socket():
    try:
        return mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    except mysoc.error as err:
        print('Socket open error:', err)
        sys.exit(1)
def connect_to_server(socket, host, port):
    try:
        server_binding = (host, port)
        socket.connect(server_binding)
    except mysoc.error as err:
        print(f'Connection error to {host}:{port}:', err)
        sys.exit(1)
def main():
    RS_table = load_rs_table(file_name, edu_host, com_host)
    rs_socket = initialize_socket()
    rs_socket.bind(('', 50008))
    rs_socket.listen(1)
    host = mysoc.gethostname()
    localhost_ip = mysoc.gethostbyname(host)
    print(f"[RS]: Server host name is {host}")
    print(f"[RS]: Server IP address is {localhost_ip}")
    client_socket, client_addr = rs_socket.accept()
    print(f"[RS]: Got a connection request from a client at {client_addr}")
    ts_com_socket = initialize_socket()
    ts_edu_socket = initialize_socket()
    first_com = True
    first_edu = True
    while True:
        data = client_socket.recv(100)
        hostname = data.decode('utf-8').strip()
        if not hostname:
            break
        if hostname in RS_table:
            entry = f"{hostname} {RS_table[hostname]['ip']} {RS_table[hostname]['flag']}"
        else:
            entry = f"{hostname} - Error:HOST NOT FOUND"
            if ".edu" in hostname:
                if first_edu:
                    connect_to_server(ts_edu_socket, RS_table[edu_host]['ip'], 5677)
                    first_edu = False
                ts_edu_socket.send(hostname.encode('utf-8'))
                entry = ts_edu_socket.recv(100).decode('utf-8')
            elif ".com" in hostname:
                if first_com:
                    connect_to_server(ts_com_socket, RS_table[com_host]['ip'], 5678)
                    first_com = False
                ts_com_socket.send(hostname.encode('utf-8'))
                entry = ts_com_socket.recv(100).decode('utf-8')
        client_socket.send(entry.encode('utf-8'))
    rs_socket.close()
if __name__ == '__main__':
    main()