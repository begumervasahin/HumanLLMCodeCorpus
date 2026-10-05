import socket
def print_header(text):
    print("")
    print("***********************")
    print(f"*    {text}    *")
    print("***********************")
def input_prime_and_base():
    Prime = int(input("Input prime number: "))
    Base = int(input("Input base number: "))
    return Prime, Base
def input_secrets():
    aliceSecret = int(input("Enter Alice Secret here:"))
    bobSecret = int(input("Enter Bob Secret here:"))
    return aliceSecret, bobSecret
def perform_diffie_hellman(Prime, Base, aliceSecret, bobSecret):
    print_header("Diffie Hellman Key Exchange")
    print("-----------------------------------------")
    print("Publicly Shared Variables:")
    print(f"    Publicly Shared Prime: {Prime}")
    print(f"    Publicly Shared Base:  {Base}")
    print("-----------------------------------------")
    A = (Base ** aliceSecret) % Prime
    print(f"\n  Alice Sends Over Public Channel: {A}")
    B = (Base ** bobSecret) % Prime
    print(f"\n  Bob Sends Over Public Channel: {B}")
    print("------------------------------------------")
    print("Privately Calculated Shared Secret:")
    aliceSharedSecret = (B ** aliceSecret) % Prime
    print(f"    Alice Shared Secret: {aliceSharedSecret}")
    bobSharedSecret = (A ** bobSecret) % Prime
    print(f"    Bob Shared Secret: {bobSharedSecret}")
    print("------------------------------------------")
    if bobSharedSecret == aliceSharedSecret:
        print("Connection established")
    return aliceSharedSecret, bobSharedSecret
def establish_server(aliceSharedSecret, bobSharedSecret):
    print("******************************************")
    print("Setting up server for shared secret exchange...")
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
if __name__ == "__main__":
    Prime, Base = input_prime_and_base()
    aliceSecret, bobSecret = input_secrets()
    aliceSharedSecret, bobSharedSecret = perform_diffie_hellman(Prime, Base, aliceSecret, bobSecret)
    establish_server(aliceSharedSecret, bobSharedSecret)