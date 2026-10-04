def fonk1(base, exponent, modulus):
    return pow(base, exponent, modulus)
def fonk2(label, value):
    print(f"{label}: {value}\n")
def fonk3():
    a1 = 9
    a2 = 4
    a3 = 3
    a4 = 29
    fonk2("a4 Value", a4)
    fonk2("a1 Value", a1)
    fonk2("A Private KEY", a2)
    b1 = fonk1(a1, a2, a4)
    fonk2("The private key B", a3)
    b2 = fonk1(a1, a3, a4)
    b3 = fonk1(b2, a2, a4)
    b4 = fonk1(b1, a3, a4)
    fonk2("A Secret Key", b3)
    fonk2("B Secret Key", b4)
if b5 = = "__main__":
    fonk3()