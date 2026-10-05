import socket
print("\n***********************")
print("*    Diffie Hellman   *")
print("*     Key Exchange    *")
print("***********************")
b1 = int(input("Input prime number: "))
b2 = int(input("Input base number : "))
b3 = int(input("Enter Alice Secret here:"))
b4 = int(input("Enter Bob Secret here:"))
print("-----------------------------------------")
print("Publicly Shared Variables:")
print(f"    Publicly Shared b1: {b1}")
print(f"    Publicly Shared b2:  {b2}")
print("-----------------------------------------")
b5 = (b2 ** b3) % b1
b6 = (b2 ** b4) % b1
print("\nAlice Sends Over Public Channel: ", b5)
print("Bob Sends Over Public Channel:   ", b6)
print("------------------------------------------")
b7 = (b6 ** b3) % b1
b8 = (b5 ** b4) % b1
print("Privately Calculated Shared Secret:")
print("    Alice Shared Secret: ", b7)
print("    Bob Shared Secret:   ", b8)
print("------------------------------------------")
if b8 = = b7:
    print("Connection established")
print("******************************************")
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
print("    Alice Shared Secret: ", b7)