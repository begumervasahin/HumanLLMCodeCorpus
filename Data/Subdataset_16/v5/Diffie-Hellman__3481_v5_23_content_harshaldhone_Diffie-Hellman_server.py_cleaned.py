import socket
def fonk1(a3, exponent, a4):
    a1 = 1
    while exponent > 0:
        a1 = (a1 * a3) % a4
        exponent -= 1
    return a1
def fonk2():
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2 = socket.gethostname()
    a2 = 1024
    b1.bind((b2, a2))
    print(f"Server will start on b2: {b2}\n")
    print("Server has successfully bound to b2 and a2")
    print("Server is waiting for a connection...\n")
    b1.listen(1)
    return b1
def fonk3(conn):
    b3 = int(input("Enter server private key: "))
    a3 = 17
    a4 = 23
    b4 = str(fonk1(a3, b3, a4))
    conn.send(b4.encode())
    print("Message has been sent\n")
    b5 = conn.recv(1024).decode()
    print(f"Client: {b5}")
    b6 = int(b5)
    b7 = fonk1(b6, b3, a4)
    print(f"Shared secret key: {b7}")
def fonk4():
    b1 = fonk2()
    conn, b8 = b1.accept()
    print(f"{b8} is connected to the server and is now online...\n")
    fonk3(conn)
if b9 = = "__main__":
    fonk4()