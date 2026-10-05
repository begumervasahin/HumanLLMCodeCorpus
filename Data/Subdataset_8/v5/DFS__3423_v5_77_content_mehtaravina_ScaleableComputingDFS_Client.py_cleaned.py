import socket
import pickle
def authentication():
    input_choice = input("Enter 1 to login, 2 to sign up, 3 to exit: ")
    socket_authen.send(input_choice.encode())
    username = input("Enter username: ")
    socket_authen.send(username.encode())
    password = input("Enter password: ")
    socket_authen.send(password.encode())
    print(username, password, input_choice)
    auth_result = socket_authen.recv(1024).decode()
    if auth_result == 'true':
        directory()
    elif auth_result == 'false':
        print('Incorrect password')
        authentication()
    elif auth_result == 'exists':
        print('Username already exists')
        authentication()
    else:
        print('Program terminated')
def directory():
    input_choice = input('Type 1 to create a new file, 2 to access existing file, 3 to exit: ')
    socket_dir.send(input_choice.encode())
    if input_choice == '1':
        create_file()
    elif input_choice == '2':
        access_file()
def create_file():
    file_name = input('Enter file name: ')
    socket_dir.send(file_name.encode())
    file_data = input('Write data into file: ')
    socket_dir.send(file_data.encode())
    data = socket_dir.recv(2048)
    files = pickle.loads(data)
    print(files)
    directory()
def access_file():
    print('Files in the server:')
    file_list = socket_dir.recv(2048)
    file_names = pickle.loads(file_list)
    print(file_names)
    file_name = input("Enter File Name, type 'exit' to terminate: ")
    socket_dir.send(file_name.encode())
    data = socket_dir.recv(2048)
    print(data.decode())
    file_name_choice = input("Type 'open' to access file and 'exit' to quit or 'back' to open another file: ")
    if file_name_choice == 'open':
        file_name_choice = 'exit'
        fileserver(file_name)
    elif file_name_choice == 'exit':
        file_name_choice.encode()
        socket_dir.send(file_name_choice.encode())
        print('Application Terminated')
    elif file_name_choice == 'back':
        directory()
def fileserver(f):
    status = lock(f)
    mode = ['r', 'a']
    if status == 'locked':
        user_choice = input('File is locked for writing, only read mode available. Type "yes" to continue or "exit" to quit: ')
        if user_choice == 'yes':
            read_file(f)
    else:
        user_choice = input('File unlocked, read and write available. Type "r" to read and "a" to append: ')
        if user_choice == mode[1]:
            append_file(f)
        else:
            read_file(f)
def lock(file_name):
    socket_lock.send(file_name.encode())
    status = socket_lock.recv(1024)
    print('Status of file is : ' + str(status.decode()))
    return status
def read_file(f):
    g = [f, 'r']
    socket_file.send(str(g))
    with open('received_file', 'wb') as f1:
        print('File opened')
        while True:
            print('Receiving data...')
            data = socket_file.recv(1024)
            print(data)
            if not data:
                break
    directory()
    f1.close()
def append_file(f):
    g = [f, 'a']
    socket_lock.send((str(g[0])).encode())
    socket_file.send(str(g))
    data1 = input("What do you want to write to file " + str(g[0]) + ": ")
    print("Modified content: " + str(data1))
    socket_file.send(data1.encode())
    print("Changes sent!")
    socket_lock.send('done'.encode())
    directory()
if __name__ == '__main__':
    host = 'localhost'
    port_dir = 5001
    socket_dir = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_dir.connect((host, port_dir))
    port_file = 5003
    socket_file = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_file.connect((host, port_file))
    port_lock = 6002
    socket_lock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_lock.connect((host, port_lock))
    port_authen = 5009
    socket_authen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_authen.connect((host, port_authen))
    authentication()