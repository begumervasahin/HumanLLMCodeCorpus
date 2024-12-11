def fonk1(Em, prk, pk):
    return (Em ** prk) % pk
def fonk2():
    b1 = []
    b2 = []
    b3 = []
    b4 = int(input("Enter Modulo: "))
    b5 = int(input("Enter Private Key: "))
    with open("Encrypted_Message.txt", "r") as f:
        b6 = [line.rstrip('\b4') for line in f]
    for x in b6:
        b1.append(x)
    for x in b1:
        b2.append(fonk1(int(x), b5, b4))
    for y in b2:
        b3.append(chr(y))
    b7 = "".join(b3)
    print("Decrypted b7:", b7)
    with open("Decrypted_Message.txt", "w") as fw:
        for z in b3:
            fw.write(str(z))
def fonk3():
    b1 = []
    b2 = []
    b4 = int(input("Enter Modulo: "))
    b5 = int(input("Enter Private Key: "))
    with open("Encrypted_File.txt", "r") as f:
        b8 = f.readlines()
    for y in b8:
        b9 = y[:-1]
        b1.append(int(b9))
    for y in b1:
        b2.append(fonk1(int(y), b5, b4))
    with open("Decrypted_File.txt", "wb") as b8:
        for y in b2:
            b8.write(bytes((y,)))
def fonk4():
    b10 = input("Enter 1 to decrypt message from a file, or 2 to decrypt a file: ")
    if b10 = = '1':
        fonk2()
    elif b10 = = '2':
        fonk3()
    else:
        print("Invalid choice. Please enter either 1 or 2.")
if b11 = = "__main__":
    fonk4()