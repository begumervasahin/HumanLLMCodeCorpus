print()
print("---------------------------------------------------------------")
print("    Cryptanalysis of the Diffie-Hellman public key protocol    ")
print("---------------------------------------------------------------")
print()
b1 = input("Confirm the prime: ")
b1 = int(b1)
b2 = input("Confirm the generator: ")
b2 = int(b2)
print()
b3 = input("b3 sent: ")
b3 = int(b3)
b4 = input("b4 sent: ")
b4 = int(b4)
print()
for x in range(1,b1) :
    if (b2**x)%b1 = = b3 :
        b5 = x
    if (b2**x)%b1 = = b4 :
        b6 = x
print("Password for b3:",b5)
print("Password for b4:",b6)
print()
b7 = (b4**b5)%b1
b8 = (b3**b6)%b1
b9 = b7
print("Their secret common key:",b9)
print()