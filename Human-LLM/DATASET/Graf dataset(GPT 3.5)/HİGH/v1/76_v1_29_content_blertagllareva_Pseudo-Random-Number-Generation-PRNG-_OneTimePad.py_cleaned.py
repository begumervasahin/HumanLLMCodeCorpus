def fonk1(char):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    a1 = 0
    for b2 in b1:
        a1 += 1
        if b2 = = char:
            break
    return a1
def fonk2(a1):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1[a1 - 1]
def fonk3(b7, b10):
    b3 = fonk1(b7)
    b4 = fonk1(b10)
    b5 = (b3 + b4) % 26
    b6 = fonk2(b5)
    return b6
def fonk4(b6, b10):
    b5 = fonk1(b6)
    b4 = fonk1(b10)
    b3 = (b5 - b4) % 26
    b7 = fonk2(b3)
    return b7
def fonk5(b7, b10):
    b6 = ""
    for i in range(len(b7)):
        b6 += fonk3(b7[i], b10[i])
    return b6
def fonk6(b6, b10):
    b7 = ""
    for i in range(len(b6)):
        b7 += fonk4(b6[i], b10[i])
    return b7
def fonk7():
    print("OneTimePad Program. Çelësi duhet të jetë më i vogël ose i barabartë me plain-tekstin. Plain-teksti nuk duhet të ketë numra.")
    print("\nMundësitë:\n1: Enkodimi\n2: Dekodimi\n3: Ndërprerje")
    while True:
        b8 = input(">>> ")
        if b8 = = "1":
            b9 = input("Plain-teksti: ")
            b10 = input("Çelësi: ")
            if len(b10) < len(b9):
                print("Çelësi duhet të jetë i paktën aq i gjatë sa plain-teksti.")
            else:
                print("Cipher-teksti:", fonk5(b9, b10))
        elif b8 = = "2":
            b11 = input("Cipher-teksti: ")
            b10 = input("Çelësi: ")
            if len(b10) < len(b11):
                print("Çelësi duhet të jetë i paktën aq i gjatë sa cipher-teksti.")
            else:
                print("Plain-teksti:", fonk6(b11, b10))
        elif b8 = = "3":
            break
        else:
            print("Ju lutem zgjedhni 1, 2, ose 3.")
if b12 = = "__main__":
    fonk7()