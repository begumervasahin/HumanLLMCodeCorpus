def fonk1(s, e, n):
    b1 = []
    while len(s)%3!=0:
            s+="
    for i in range(0,int(len(s)/3)):
        b2 = s[3*i:3*i+3]
        b8,b4,b3 = str(ord(b2[0])),str(ord(b2[1])),str(ord(b2[2]))
        while len(b4)!=3:
            b4 = "0" + b4
        while len(b3)!=3:
            b3 = "0" + b3
        b5 = int(b8 + b4 + b3)
        b1.append(fonk2(b5,e,n))
    return(b1)
def fonk2(m, dee, en):
    b6 = str(bin(dee)).lstrip("0b")
    b6 = b6[::-1]
    b4 = []
    for i in range(0, len(b6)):
        b4.append(int(b6[i]))
    b7 = [m]
    for i in range(1, len(b6)):
        b7.append((b7[i-1]**2)%en)
    a1 = 1
    for i in range(0,len(b6)):
        if b4[i] == 1:
            a1 = (a1*b7[i])%en
    return a1
b8 = True
while b8:
    b9 = input("Enter b8 message here (or enter \"quit\" to quit): ")
    b10 = input("Enter an n value: ")
    while not b10.isnumeric():
        print("Please enter an integer value")
        b10 = input("Enter an n value: ")
    b10 = int(b10)
    b11 = input("Enter an e value: ")
    while not b11.isnumeric():
        print("Please enter an integer value")
        b11 = input("Enter an e value: ")
    b11 = int(b11)
    print(fonk1(b9, b11, b10))