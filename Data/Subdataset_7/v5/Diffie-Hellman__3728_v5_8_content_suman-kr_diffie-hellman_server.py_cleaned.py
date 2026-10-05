import socket
def fonk1(text):
    print("\n***********************")
    print(f"*    {text}    *")
    print("*     Key Exchange    *")
    print("***********************")
def fonk2():
    b1 = int(input("Input prime number: "))
    b2 = int(input("Input base number : "))
    b3 = int(input("Enter Alice Secret here:"))
    b4 = int(input("Enter Bob Secret here:"))
    return b1, b2, b3, b4
def fonk3(b1, b2):
    print("-----------------------------------------")
    print("Publicly Shared Variables:")
    print(f"    Publicly Shared b1: {b1}")
    print(f"    Publicly Shared b2:  {b2}")
    print("-----------------------------------------")
def fonk4(b1, b2, b3, b4):
    b5 = (b2 ** b3) % b1
    b6 = (b2 ** b4) % b1
    return b5, b6
def fonk5(b5, b6):
    print("\nAlice Sends Over Public Channel: ", b5)
    print("Bob Sends Over Public Channel:   ", b6)
    print("------------------------------------------")
def fonk6(b1, b5, b6, b3, b4):
    b7 = (b6 ** b3) % b1
    b8 = (b5 ** b4) % b1
    return b7, b8
def fonk7(b7, b8):
    print("Privately Calculated Shared Secret:")
    print("    Alice Shared Secret: ", b7)
    print("    Bob Shared Secret:   ", b8)
    print("------------------------------------------")
def fonk8(b7, b8):
    if b8 = = b7:
        print("Connection established")
    print("******************************************")
def fonk9(b7, b8):
    b9 = socket.socket()
    b10 = socket.gethostname()
    a1 = 51125
    b9.bind((b10, a1))
    b9.listen(5)
    while True:
        client, b11 = b9.accept()
        print('Got connection from', b11)
        client.send(str(b7) + str(b8))
        client.close()
def fonk10():
    fonk1("Diffie Hellman Key Exchange")
    b1, b2, b3, b4 = fonk2()
    fonk3(b1, b2)
    b5, b6 = fonk4(b1, b2, b3, b4)
    fonk5(b5, b6)
    b7, b8 = fonk6(b1, b5, b6, b3, b4)
    fonk7(b7, b8)
    fonk8(b7, b8)
    fonk9(b7, b8)
if b12 = = "__main__":
    fonk10()