from ecdsa.numbertheory import inverse_mod as modinv
import sys, os
x
e = 65537
try:
    p = input("Input a prime number ")
    q = input("Input a different prime number (minimum added value of 26 for letters in alphabet) ")
    p = int(p)
    q = int(q)
    if p + q < 26:
        raise BaseException
except:
    print("Try again, added input values below 26")
    sys.exit()
n = p * q
d = modinv(e, ((p-1)*(q-1)))
plaintext = input("What would you like to encrypt? ")
plaintext = plaintext.lower()
print("Your plaintext is: " + plaintext)
print("p: " + str(p))
print("q: " + str(q))
plain_list_num = []
enc_list_num = []
end_list_num = []
ending = ""
for i in plaintext:
    plain_list_num.append(ord(i))
print("Your plaintext list is: " + str(plain_list_num))
for i in plain_list_num:
    enc_list_num.append(i**e % n)
print("Your encrypted values are " + str(enc_list_num))
for i in enc_list_num:
    end_list_num.append(i**d % n)
print("Your end result list is " + str(end_list_num))
for i in end_list_num:
    ending += chr(i)
print("Plaintext(Unencrypted) is: " + ending)