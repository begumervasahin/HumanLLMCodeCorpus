
print("Enter b6 PRIME numbers for 'b1' and 'b2'.")
b1 = int(input("b1: "))
b2 = int(input("b2: "))
b3 = b1 * b2
print("\b4 = " + str(b3))
b5 = (b1 - 1) * (b2 - 1)
print("b5 = " + str(b5))
a1 = b6
a2 = 0
for x in range(0, b5):
    if b3 % a1 = = 0 or b5 % a1 == 0:
        a1 += 1
        if a1 % b6 = = 0:
            a1 += 1
    else:
        a2 = a1
print("a2 = " + str(a2))
print("ENCRYPTION b7 = (" + str(a2) + ", " + str(b3) + ")")
a3 = 10
while True:
    if (a3 * a2) % b5 = = 1:
        break
    else:
        a3 += 1
print("a3 = " + str(a3))
print("DECRYPTION b7 = (" + str(a3) + ", " + str(b3) + ")")
b8 = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b9 = list(b8)
b10 = []
b11 = input("\nEnter simple message (b9 only): ")
b12 = list(b11)
print(b12)
for x in b12:
    b10.append((b9.index(x)**a2) % b3)
print("\nEncrypted message: ")
print(b10)
b13 = []
for x in b10:
    b13.append(b9[(x**a3) % b3])
print("\nDecrypted Message: ")
print(b13)