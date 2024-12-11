def fonk1(char):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    a1 = 1
    for b2 in b1:
        if b2 = = char:
            break
        else:
            a1+=1
    return a1
def fonk2(a1):
    b1 = "abcdefghijklmnopqrstuvwxyz"
    return b1[a1+1]
def fonk3(b6, key):
    b3 = ( fonk1(b6) + fonk1(key) ) % 26
    b4 = fonk2(b3)
    return b4
def fonk4(b4, key):
    b5 = fonk1(b4) - fonk1(key)
    b6 = fonk2(b5)
    return b6
def fonk5(b6, key):
    b4 = ""
    for i in range(0, len(b6)):
        b4 += fonk3(b6[i], key[i])
    return b4
def fonk6(b4, key):
    b6 = ""
    for i in range(0, len(b4)):
        b6 += fonk4(b4[i], key[i])
    return b6
def fonk7():
    b7 = True
    b8 = ""
    print("OneTimePad Program.  ÃelÃ«si duhet tÃ« jetÃ« mÃ« i vogÃ«l ose i barabartÃ« me plain-tekstin.  Plain-teksti nuk duhet tÃ« ketÃ« numra.")
    print("\nMundÃ«sitÃ«:\n1: Enkodimi\n2: Dekodimi\n3: NdÃ«rprerje")
    while b7 = = True:
        b8 = input(">>> ")
        if b8 = = "1":
            print("Cipher-teksti: " + fonk5(input("Plain-teksti: "), input("ÃelÃ«si: ")))
        elif b8 = = "2":
            print("Plain-teksti: " + fonk6(input("Cipher-teksti: "), input("ÃelÃ«si: ")))
        elif b8 = = "3":
            b7 = False
        else:
            print("Ju lutem zgjedhni 1, 2, or 3")
fonk7()