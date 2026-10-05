import socket
def fonk1(title):
    print("\n" + "*" * 27)
    print(f"* {title.center(23)} *")
    print("*" * 27)
def fonk2():
    b1 = int(input("Enter the b1 number: "))
    b2 = int(input("Enter the b2 number: "))
    return b1, b2
def fonk3():
    b3 = int(input("Enter Alice's secret number: "))
    b4 = int(input("Enter Bob's secret number: "))
    return b3, b4
def fonk4(b1, b2, b3, b4):
    fonk1("Diffie-Hellman Key Exchange")
    print("\nPublicly Shared Variables:")
    print(f"  Prime Number: {b1}")
    print(f"  Base Number:  {b2}")
    b5 = (b2 ** b3) % b1
    b6 = (b2 ** b4) % b1
    print("\nAlice Sends Over Public Channel:", b5)
    print("Bob Sends Over Public Channel:", b6)
    b7 = (b6 ** b3) % b1
    b8 = (b5 ** b4) % b1
    if b7 = = b8:
        print("\nShared Secrets Match!")
        print("Connection Established")
    return b7, b8
def fonk5(b3, b4, shared_secret):
    print("\nSetting up server for shared secret exchange...")
    b9 = socket.socket()
    b10 = socket.gethostname()
    a1 = 51125
    b9.bind((b10, a1))
    b9.listen(5)
    print("Waiting for incoming connections...")
    while True:
        client_socket, b11 = b9.accept()
        print('Got connection from', b11)
        client_socket.send(str(shared_secret).encode())
        client_socket.close()
if b12 = = "__main__":
    prime_number, b13 = fonk2()
    alice_secret_number, b14 = fonk3()
    b7, b8 = fonk4(
        prime_number, b13, alice_secret_number, b14
    )
    fonk5(alice_secret_number, b14, b7)