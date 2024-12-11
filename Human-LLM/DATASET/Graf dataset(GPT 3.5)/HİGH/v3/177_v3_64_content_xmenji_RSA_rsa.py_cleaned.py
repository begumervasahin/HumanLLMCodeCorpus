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
def fonk3():
    while True:
        b3 = int(input("Enter a b3 number: "))
        if fonk1(b3):
            return b3
        else:
            print("Please enter a b3 number.")
print("RSA Encryption and Decryption")
print("\nEnter two b3 numbers to set up RSA encryption.")
b4 = fonk3()
b5 = fonk3()
b6 = b4 * b5
b7 = (b4 - 1) * (b5 - 1)
a1 = 2
while fonk2(a1, b7) != 1:
    a1 += 1
print("\nPublic key (encryption key): (a1 = {}, b6 = {})".format(a1, b6))
a2 = 10
while True:
    if (a2 * a1) % b7 = = 1:
        break
    else:
        a2 += 1
print("Private key (decryption key): (a2 = {}, b6 = {})".format(a2, b6))
b8 = input("\nEnter a message to encrypt (b10 only): ")
b9 = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b10 = list(b9)
b11 = [(b10.index(x) ** a1) % b6 for x in b8]
print("\nEncrypted message: ")
print(b11)
b12 = [b10[(x ** a2) % b6] for x in b11]
print("\nDecrypted Message: ")
print(''.join(b12))