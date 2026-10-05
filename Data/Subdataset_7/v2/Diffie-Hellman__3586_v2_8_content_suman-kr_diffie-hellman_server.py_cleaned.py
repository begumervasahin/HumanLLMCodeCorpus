import socket
def fonk1(text):
    print("")
    print("***********************")
    print(f"*    {text}    *")
    print("***********************")
def fonk2():
    b1 = int(input("Input prime number: "))
    b2 = int(input("Input base number: "))
    return b1, b2
def fonk3():
    b3 = int(input("Enter Alice Secret here:"))
    b4 = int(input("Enter Bob Secret here:"))
    return b3, b4
def fonk4(b1, b2, b3, b4):
    fonk1("Diffie Hellman Key Exchange")
    print("-----------------------------------------")
    print("Publicly Shared Variables:")
    print(f"    Publicly Shared b1: {b1}")
    print(f"    Publicly Shared b2:  {b2}")
    print("-----------------------------------------")
    b5 = (b2 ** b3) % b1
    print(f"\n  Alice Sends Over Public Channel: {b5}")
    b6 = (b2 ** b4) % b1
    print(f"\n  Bob Sends Over Public Channel: {b6}")
    print("------------------------------------------")
    print("Privately Calculated Shared Secret:")
    b7 = (b6 ** b3) % b1
    print(f"    Alice Shared Secret: {b7}")
    b8 = (b5 ** b4) % b1
    print(f"    Bob Shared Secret: {b8}")
    print("------------------------------------------")
    if b8 = = b7:
        print("Connection established")
    return b7, b8
def fonk5(b7, b8):
    print("******************************************")
    print("Setting up server for shared secret exchange...")
    b9 = socket.socket()
    b10 = socket.gethostname()
    a1 = 51125
    b9.bind((b10, a1))
    b9.listen(5)
    print("Waiting for incoming connections...")
    while True:
        c, b11 = b9.accept()
        print('Got connection from', b11)
        c.send(str(b7) + str(b8))
        c.close()
if b12 = = "__main__":
    b1, b2 = fonk2()
    b3, b4 = fonk3()
    b7, b8 = fonk4(b1, b2, b3, b4)
    fonk5(b7, b8)