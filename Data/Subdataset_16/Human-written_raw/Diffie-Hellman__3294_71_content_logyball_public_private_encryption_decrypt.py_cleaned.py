def fonk1(pubKeyFile):
    with open(pubKeyFile, 'r') as pkf:
        b1 = pkf.readlines()
    return int(b1[2]), int(b1[0])
def fonk2(priKey, b8, b9, b3):
    return (pow(b8, b3-1-priKey, b3) * (b9 % b3)) % b3
def fonk3(b2 = "test/testEncrypted.txt", writePath="test/testDecrypted.txt", priKeyPath='test/testprikey.txt', debug=False):
    priKey, b3 = fonk1(priKeyPath)
    with open(b2, 'r') as rf:
        b4 = rf.readlines()
    with open(writePath, 'w', b5 = 'utf-8') as wf:
        b6 = ''
        for line in b4:
            b7 = line.split()
            b8 = int(b7[0])
            b9 = int(b7[1])
            b6 += chr(fonk2(priKey, b8, b9, b3))
        if debug:
            print("DEBUG decrypted b6: \n%s\n" % b6)
        wf.write(b6)