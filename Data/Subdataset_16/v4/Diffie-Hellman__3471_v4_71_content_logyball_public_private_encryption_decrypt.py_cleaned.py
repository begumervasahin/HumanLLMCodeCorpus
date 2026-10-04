def fonk1(file_path):
    with open(file_path, 'r') as file:
        b1 = file.readlines()
    b2 = int(b1[0].strip())
    b3 = int(b1[2].strip())
    return b3, b2
def fonk2(b3, c1, b7, b2):
    return (pow(c1, b2 - 1 - b3, b2) * b7) % b2
def fonk3(b4 = "test/testEncrypted.txt", b11="test/testDecrypted.txt", b12='test/testprikey.txt', b13=False):
    b3, b2 = fonk1(b12)
    with open(b4, 'r') as read_file:
        b5 = read_file.readlines()
    b6 = []
    for line in b5:
        c1, b7 = map(int, line.split())
        b6.append(chr(fonk2(b3, c1, b7, b2)))
    b8 = ''.join(b6)
    if b13:
        print(f"DEBUG decrypted output: \n{b8}\n")
    with open(b11, 'w', b9 = 'utf-8') as write_file:
        write_file.write(b8)
if b10 = = '__main__':
    fonk3(
        b4 = "test/testEncrypted.txt",
        b11 = "test/testDecrypted.txt",
        b12 = 'test/testprikey.txt',
        b13 = True
    )