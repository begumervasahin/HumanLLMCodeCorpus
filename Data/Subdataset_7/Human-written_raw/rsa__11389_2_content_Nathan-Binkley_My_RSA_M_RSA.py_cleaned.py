from ecdsa.numbertheory import inverse_mod as modinv
import sys, os
x
a1 = 65537
try:
    b1 = input("Input a prime number ")
    b2 = input("Input a different prime number (minimum added value of 26 for letters in alphabet) ")
    b1 = int(b1)
    b2 = int(b2)
    if b1 + b2 < 26:
        raise BaseException
except:
    print("Try again, added input values below 26")
    sys.exit()
b3 = b1 * b2
b4 = modinv(a1, ((b1-1)*(b2-1)))
b5 = input("What would you like to encrypt? ")
b5 = b5.lower()
print("Your b5 is: " + b5)
print("b1: " + str(b1))
print("b2: " + str(b2))
b6 = []
b7 = []
b8 = []
b9 = ""
for i in b5:
    b6.append(ord(i))
print("Your b5 list is: " + str(b6))
for i in b6:
    b7.append(i**a1 % b3)
print("Your encrypted values are " + str(b7))
for i in b7:
    b8.append(i**b4 % b3)
print("Your end result list is " + str(b8))
for i in b8:
    b9 += chr(i)
print("Plaintext(Unencrypted) is: " + b9)