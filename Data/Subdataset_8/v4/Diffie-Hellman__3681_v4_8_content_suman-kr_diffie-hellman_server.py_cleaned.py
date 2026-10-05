import socket
print("\n***********************")
print("*    Diffie Hellman   *")
print("*     Key Exchange    *")
print("***********************")
Prime = int(input("Input prime number: "))
Base = int(input("Input base number : "))
aliceSecret = int(input("Enter Alice Secret here:"))
bobSecret = int(input("Enter Bob Secret here:"))
print("-----------------------------------------")
print("Publicly Shared Variables:")
print(f"    Publicly Shared Prime: {Prime}")
print(f"    Publicly Shared Base:  {Base}")
print("-----------------------------------------")
A = (Base ** aliceSecret) % Prime
B = (Base ** bobSecret) % Prime
print("\nAlice Sends Over Public Channel: ", A)
print("Bob Sends Over Public Channel:   ", B)
print("------------------------------------------")
aliceSharedSecret = (B ** aliceSecret) % Prime
bobSharedSecret = (A ** bobSecret) % Prime
print("Privately Calculated Shared Secret:")
print("    Alice Shared Secret: ", aliceSharedSecret)
print("    Bob Shared Secret:   ", bobSharedSecret)
print("------------------------------------------")
if bobSharedSecret == aliceSharedSecret:
    print("Connection established")
print("******************************************")
server = socket.socket()
host = socket.gethostname()
port = 51125
server.bind((host, port))
server.listen(5)
while True:
    client, addr = server.accept()
    print('Got connection from', addr)
    client.send(str(aliceSharedSecret) + str(bobSharedSecret))
    client.close()
print("    Alice Shared Secret: ", aliceSharedSecret)