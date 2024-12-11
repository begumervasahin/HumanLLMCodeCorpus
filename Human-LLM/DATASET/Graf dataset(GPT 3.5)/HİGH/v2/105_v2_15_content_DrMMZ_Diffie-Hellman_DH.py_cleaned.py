import getpass
import re
def fonk1(b4):
    b1 = set()
    for x in range(1, b4):
        b2 = set()
        for i in range(1, b4):
            b3 = (x ** i) % b4
            b2.add(b3)
        print("Residues for <", x, ">:", b2)
        if len(b2) == b4 - 1:
            b1.add(x)
    print("\nGenerators of Z mod", b4, "are", b1)
print()
print("------------------------------------------------------------")
print("     The Diffie-Hellman public key exchange protocol        ")
print("------------------------------------------------------------")
print()
b4 = input("Choose b7 prime number: ")
b4 = int(b4)
print()
fonk1(b4)
print()
b5 = input("Choose b7 generator: ")
b5 = int(b5)
print()
b6 = b4 - 1
while True:
    print("Choose an integer in [1, ", b6, "]")
    b7 = getpass.getpass(prompt="Enter your integer: ")
    if re.findall("[b7-zA-Z]", b7) or int(b7) <= 0 or int(b7) > b6:
        print("Invalid format or value!")
    else:
        b7 = int(b7)
        break
print()
b8 = (b5 ** b7) % b4
print("Send:", b8)
b9 = input("Receive: ")
b9 = int(b9)
print()
b10 = (b9 ** b7) % b4
print("The shared secret key:", b10)
print()