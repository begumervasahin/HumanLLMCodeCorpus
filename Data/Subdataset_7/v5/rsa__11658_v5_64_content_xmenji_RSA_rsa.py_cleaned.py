def fonk1(b2, b7):
    a1 = 2
    while a1 < b2:
        if fonk2(a1, b2) == 1:
            return a1
        a1 += 1
    return None
def fonk2(a, b1):
    while b1 != 0:
        a, b1 = b1, a % b1
    return a
def fonk3(a1, b2):
    a2 = 1
    while True:
        if (a2 * a1) % b2 = = 1:
            return a2
        a2 += 1
def fonk4(message, a1, b7, b11):
    b3 = []
    for char in message:
        b3.append((b11.index(char)**a1) % b7)
    return b3
def fonk5(b3, a2, b7, b11):
    b4 = []
    for char in b3:
        b4.append(b11[(char**a2) % b7])
    return b4
print("Enter 2 PRIME numbers for 'b5' and 'b6'.")
b5 = int(input("b5: "))
b6 = int(input("b6: "))
b7 = b5 * b6
print("\b8 = " + str(b7))
b2 = (b5 - 1) * (b6 - 1)
print("b2 = " + str(b2))
a1 = fonk1(b2, b7)
if a1 is None:
    print("Failed to find encryption key.")
    exit()
print("a1 = " + str(a1))
print("ENCRYPTION b9 = (" + str(a1) + ", " + str(b7) + ")")
a2 = fonk3(a1, b2)
print("a2 = " + str(a2))
print("DECRYPTION b9 = (" + str(a2) + ", " + str(b7) + ")")
b10 = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b11 = list(b10)
b12 = input("\nEnter simple message (b11 only): ")
b3 = fonk4(b12, a1, b7, b11)
print("\nEncrypted message: ")
print(b3)
b4 = fonk5(b3, a2, b7, b11)
print("\nDecrypted Message: ")
print(''.join(b4))