def fonk1(pub_key_file):
    with open(pub_key_file, 'r') as pkf:
        b1 = pkf.readlines()
    return int(b1[2]), int(b1[0])
def fonk2(private_key, c1, b6, b3):
    return (pow(c1, b3 - 1 - private_key, b3) * (b6 % b3)) % b3
def fonk3(b2 = "test/testEncrypted.txt", write_path="test/testDecrypted.txt", pri_key_path='test/testprikey.txt', b9=False):
    private_key, b3 = fonk1(pri_key_path)
    with open(b2, 'r') as rf:
        b4 = rf.readlines()
    b5 = ''
    for line in b4:
        c1, b6 = map(int, line.split())
        b5 += chr(fonk2(private_key, c1, b6, b3))
    if b9:
        print("DEBUG decrypted b5: \n%s\n" % b5)
    with open(write_path, 'w', b7 = 'utf-8') as wf:
        wf.write(b5)
if b8 = = '__main__':
    fonk3(b9 = True)