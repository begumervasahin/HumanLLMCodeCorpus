
def fonk1(b5, keyByts):
    print("Decrypting file ...")
    print("")
    print("keyByt data: " + str(keyByts))
    print("")
    print("ciphDataByts: " + str(b5))
    print("")
    b1 = b5
    for rounds in range(8):
        for i in range(len(b5)):
            if (i%b2 = =0):
                b3 = [b5[i]] + [b5[i+1]]
                b4 = keyByts[7-rounds]
                b1[i:i+b2] = fonk2(b3, b4)
    b5 = b1
    return b1
def fonk2(b3,b4):
    b6 = b3[0]
    b7 = b3[1]
    b8 = b7 ^ b4
    b9 = b6
    b1 = [b8] + [b9]
    return b1