import socket
def fonk1(a3, exp, a4):
    a1 = 1
    while exp != 0:
        a1 = (a1 * a3) % a4
        exp -= 1
    return a1 % a4
def fonk2():
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2 = input("Please enter the b2 name of the server: ")
    a2 = 1024
    b1.connect((b2, a2))
    print("Connected to the server\n")
    b3 = int(input("Enter client private key: "))
    a3 = 17
    a4 = 23
    b4 = str(fonk1(a3, b3, a4))
    print()
    b5 = b1.recv(1024).decode()
    print("Server:", b5)
    b1.send(b4.encode())
    print("Message has been sent\n")
    b5 = int(b5)
    b6 = fonk1(b5, b3, a4)
    print("Secret key shared:", b6)
if b7 = = "__main__":
    fonk2()