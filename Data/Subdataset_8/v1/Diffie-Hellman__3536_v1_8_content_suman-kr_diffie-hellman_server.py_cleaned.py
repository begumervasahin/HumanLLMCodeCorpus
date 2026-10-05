import socket
print("")
print("***********************")
print("*    Diffie Hellman   *")
print("*     Key Exchange    *")
print("***********************")
Prime = int(input("Input prime number: "))
Base = int(input("Input base number : "))
aliceSecret = int(input("Enter Alice Secret here:"))
bobSecret = int(input("Enter Bob Secret here:"))
print("-----------------------------------------")
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", Prime)
print("    Publicly Shared Base:  ", Base)
print("-----------------------------------------")
A = (Base ** aliceSecret) % Prime
print("\n  Alice Sends Over Public Channel: ", A)
B = (Base ** bobSecret) % Prime
print("\n  Bob Sends Over Public Channel: ", B)
print("------------------------------------------")
print("Privately Calculated Shared Secret:")
aliceSharedSecret = (B ** aliceSecret) % Prime
print("    Alice Shared Secret: ", aliceSharedSecret)
bobSharedSecret = (A ** bobSecret) % Prime
print("    Bob Shared Secret: ", bobSharedSecret)
print("------------------------------------------")
if bobSharedSecret == aliceSharedSecret:
    print("Connection established")
print("******************************************")
s = socket.socket()
host = socket.gethostname()
port = 51125
s.bind((host, port))
s.listen(5)
print("Waiting for incoming connections...")
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(str(aliceSharedSecret) + str(bobSharedSecret))
    c.close()