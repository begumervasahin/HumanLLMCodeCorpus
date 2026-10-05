import getpass
import re
def fonk1(b4):
    b1 = set()
    for x in range(1, b4):
        b2 = set()
        for i in range(1, b4):
            b3 = (x ** i) % b4
            b2.add(b3)
        print("Residues for", x, ":", b2)
        if len(b2) == b4 - 1:
            b1.add(x)
    print("\nGenerators of Z mod", b4, "are", b1)
print("\n" + "-" * 60)
print("     The Diffie-Hellman public key exchange protocol        ")
print("-" * 60 + "\n")
b4 = int(input("Choose b7 prime number: "))
print()
fonk1(b4)
print()
b5 = int(input("Choose b7 generator: "))
print()
b6 = b4 - 1
while True:
    print("Choose an integer in [1, {}]".format(b6))
    b7 = getpass.getpass(prompt="Enter your integer: ")
    if not b7.isdigit() or int(b7) <= 0 or int(b7) > b6:
        print("Invalid format or value!")
    else:
        b7 = int(b7)
        break
print()
b8 = (b5 ** b7) % b4
print("Send:", b8)
b9 = int(input("Receive: "))
print()
b10 = (b9 ** b7) % b4
print("The shared secret key:", b10)
print()