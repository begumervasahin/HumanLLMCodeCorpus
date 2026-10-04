import socket
def powmod(base, exp, mod):
    result = 1
    while exp != 0:
        result = (result * base) % mod
        exp -= 1
    return result % mod
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input("Please enter the host name of the server: ")
    port = 1024
    s.connect((host, port))
    print("Connected to the server\n")
    private_key = int(input("Enter client private key: "))
    base = 17
    mod = 23
    message = str(powmod(base, private_key, mod))
    print()
    incoming_message = s.recv(1024).decode()
    print("Server:", incoming_message)
    s.send(message.encode())
    print("Message has been sent\n")
    incoming_message = int(incoming_message)
    shared_secret = powmod(incoming_message, private_key, mod)
    print("Secret key shared:", shared_secret)
if __name__ == "__main__":
    main()