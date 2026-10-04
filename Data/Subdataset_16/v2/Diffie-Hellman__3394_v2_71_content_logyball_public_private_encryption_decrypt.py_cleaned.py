def fonk1(pub_key_file):
    with open(pub_key_file, 'r') as file:
        b1 = file.readlines()
    b2 = int(b1[0].strip())
    b3 = int(b1[2].strip())
    return b3, b2
def fonk2(b3, c1, b8, b2):
    b4 = (pow(c1, b2 - 1 - b3, b2) * (b8 % b2)) % b2
    return b4
def fonk3(b5 = "test/testEncrypted.txt", write_path="test/testDecrypted.txt", pri_key_path='test/testprikey.txt', b11=False):
    b3, b2 = fonk1(pri_key_path)
    with open(b5, 'r') as read_file:
        b6 = read_file.readlines()
    b7 = ''
    for line in b6:
        c1, b8 = map(int, line.split())
        b7 += chr(fonk2(b3, c1, b8, b2))
    if b11:
        print(f"DEBUG decrypted output: \n{b7}\n")
    with open(write_path, 'w', b9 = 'utf-8') as write_file:
        write_file.write(b7)
if b10 = = '__main__':
    fonk3(b11 = True)