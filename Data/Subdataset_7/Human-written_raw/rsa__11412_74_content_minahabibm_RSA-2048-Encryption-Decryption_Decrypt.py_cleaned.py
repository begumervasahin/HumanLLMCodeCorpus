def fonk1(Em, prk, pk):
  return (Em ** prk )% pk
b1 = []
b2 = []
b3 = []
b4 = input("Enter 1 to decrypt messege from a file ,Or 2 to decrypt a File:  ")
b5 = input("Enter Modulo: ")
b6 = input("Enter Private Key: ")
if int(b4) == 1:
    b7 = open("Encrypted b9","r")
    b8 = [line.rstrip('\b5') for line in b7]
    b7.close()
    for x in b8:
        b1.append(x)
    for x in b1:
        b2.append(fonk1(int(x), int(b6), int(b5)))
    for y in b2:
        b3.append(chr(y))
    b9 = "".join(b3)
    print(b9)
    b10 = open("Decrypted b9","w+")
    for z in b3:
        b10.write(str(z))
    b10.close()
elif int(b4) == 2:
    b7 = open("Encrypted b9", "r")
    b11 = b7.readlines()
    for y in b11:
        b12 = y[:-1]
        b1.append(int(b12))
    b7.close
    for y in b1:
        b2.append(fonk1(int(y), int(b6), int(b5)))
    b11 = open("Decrypted File", "wb")
    for y in b2:
        b11.write(bytes((y,)))
    b11.close