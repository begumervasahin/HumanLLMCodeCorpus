
def fonk1(num):
    if num <= 1:
        return False
    for b1 in range(2, int(num**0.5) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(a, b2):
    while b2 != 0:
        a, b2 = b2, a % b2
    return a
print("Enter 2 PRIME numbers for 'b3' and 'b4'.")
b3 = int(input("b3: "))
b4 = int(input("b4: "))
if not (fonk1(b3) and fonk1(b4)):
    print("Both 'b3' and 'b4' must be prime numbers.")
    exit()
b5 = b3 * b4
print("\b6 = " + str(b5))
b7 = (b3 - 1) * (b4 - 1)
print("b7 = " + str(b7))
a1 = 2
while fonk2(a1, b7) != 1:
    a1 += 1
print("a1 = " + str(a1))
print("ENCRYPTION b8 = (" + str(a1) + ", " + str(b5) + ")")
a2 = 10
while True:
    if (a2 * a1) % b7 = = 1:
        break
    else:
        a2 += 1
print("a2 = " + str(a2))
print("DECRYPTION b8 = (" + str(a2) + ", " + str(b5) + ")")
b9 = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b10 = list(b9)
b11 = input("\nEnter simple message (b10 only): ")
b12 = [(b10.index(x) ** a1) % b5 for x in b11]
print("\nEncrypted message: ")
print(b12)
b13 = [b10[(x ** a2) % b5] for x in b12]
print("\nDecrypted Message: ")
print(''.join(b13))