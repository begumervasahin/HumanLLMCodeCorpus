import socket
import pickle
user_credentials = {'user1': 'password1', 'user2': 'password2'}
file_contents = {}
HOST = 'localhost'
PORT_DIR = 5001
PORT_FILE = 5003
PORT_LOCK = 6002
PORT_AUTHEN = 5009
socket_dir = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_dir.bind((HOST, PORT_DIR))
socket_dir.listen(5)
socket_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_file.bind((HOST, PORT_FILE))
socket_file.listen(5)
socket_lock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_lock.bind((HOST, PORT_LOCK))
socket_lock.listen(5)
socket_authen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_authen.bind((HOST, PORT_AUTHEN))
socket_authen.listen(5)
print("Server started. Listening for connections...")
def authentication(conn):
    input1 = conn.recv(1024).decode()
    conn.sendall(input1.encode())
    username = conn.recv(1024).decode()
    conn.sendall(username.encode())
    password = conn.recv(1024).decode()
    conn.sendall(password.encode())
    print(username, password, input1)
    if username in user_credentials:
        if user_credentials[username] == password:
            conn.sendall('true'.encode())
            return username
        else:
            conn.sendall('false'.encode())
            return None
    else:
        user_credentials[username] = password
        conn.sendall('exists'.encode())
        return None
def directory(conn):
    inp = conn.recv(1024).decode()
    conn.sendall(inp.encode())
    if inp == '1':
        f_name = conn.recv(1024).decode()
        conn.sendall(f_name.encode())
        info = conn.recv(1024).decode()
        conn.sendall(info.encode())
        file_contents[f_name] = info
        files = pickle.dumps(list(file_contents.keys()))
        conn.sendall(files)
    elif inp == '2':
        f_list = pickle.dumps(list(file_contents.keys()))
        conn.sendall(f_list)
        file_name = conn.recv(1024).decode()
        if file_name in file_contents:
            conn.sendall(file_contents[file_name].encode())
        else:
            conn.sendall("File not found.".encode())
def lock(conn):
    file_name = conn.recv(1024).decode()
    if file_name in file_contents:
        conn.sendall('locked'.encode())
    else:
        conn.sendall('unlocked'.encode())
def client_handler(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        if data == '1':
            directory(conn)
        elif data == '2':
            lock(conn)
def main():
    while True:
        conn, addr = socket_authen.accept()
        print('Connected by', addr)
        username = authentication(conn)
        if username:
            print('User authenticated:', username)
            client_handler(conn)
        else:
            print('Authentication failed. Closing connection.')
        conn.close()
if __name__ == '__main__':
    main()