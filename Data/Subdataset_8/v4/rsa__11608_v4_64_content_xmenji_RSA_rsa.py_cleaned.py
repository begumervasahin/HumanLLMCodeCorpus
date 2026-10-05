
print("Enter 2 PRIME numbers for 'p' and 'q'.")
p = int(input("p: "))
q = int(input("q: "))
n = p * q
print("\nn = " + str(n))
phi = (p - 1) * (q - 1)
print("phi = " + str(phi))
tempE = 2
e = 0
for x in range(0, phi):
    if n % tempE == 0 or phi % tempE == 0:
        tempE += 1
        if tempE % 2 == 0:
            tempE += 1
    else:
        e = tempE
print("e = " + str(e))
print("ENCRYPTION KEY= (" + str(e) + ", " + str(n) + ")")
d = 10
while True:
    if (d * e) % phi == 1:
        break
    else:
        d += 1
print("d = " + str(d))
print("DECRYPTION KEY= (" + str(d) + ", " + str(n) + ")")
alphabet = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)
encryptedMsg = []
msg = input("\nEnter simple message (letters only): ")
msgArray = list(msg)
print(msgArray)
for x in msgArray:
    encryptedMsg.append((letters.index(x)**e) % n)
print("\nEncrypted message: ")
print(encryptedMsg)
decryptedMsg = []
for x in encryptedMsg:
    decryptedMsg.append(letters[(x**d) % n])
print("\nDecrypted Message: ")
print(decryptedMsg)