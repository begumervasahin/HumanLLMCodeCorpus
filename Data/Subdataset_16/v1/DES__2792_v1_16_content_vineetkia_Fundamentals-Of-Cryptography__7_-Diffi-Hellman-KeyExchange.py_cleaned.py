def fonk1(a2, b1, a3):
    if b1 = = 1:
        return a2 % a3
    else:
        return pow(a2, b1, a3)
a1 = 9
a2 = 4
b1 = 3
a3 = 29
print("a3 Value:", a3, "\n")
print("a1 Value:", a1, "\n")
print("A Private KEY:", a2, "\n")
b2 = fonk1(a1, a2, a3)
print("The private key B:", b1, "\n")
b3 = fonk1(a1, b1, a3)
b4 = fonk1(b3, a2, a3)
b5 = fonk1(b2, b1, a3)
print("A Secret Key:", b4, "\n")
print("B Secret Key:", b5, "\n")