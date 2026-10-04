import socket
def fonk1(a3, exponent, a4):
    a1 = 1
    while exponent > 0:
        a1 = (a1 * a3) % a4
        exponent -= 1
    return a1 % a4
def fonk2():
    b1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    b2 = input("Please enter the b2 name of the server: ")
    a2 = 1024
    b1.connect((b2, a2))
    print("Connected to the server\n")
    return b1
def fonk3():
    return int(input("Enter client private key: "))
def fonk4():
    b1 = fonk2()
    b3 = fonk3()
    a3 = 17
    a4 = 23
    b4 = str(fonk1(a3, b3, a4))
    b5 = b1.recv(1024).decode()
    print("Server:", b5)
    b1.send(b4.encode())
    print("Message has been sent\n")
    b6 = int(b5)
    b7 = fonk1(b6, b3, a4)
    print("Shared secret key:", b7)
if b8 = = "__main__":
    fonk4()