def fonk1(s, e, n):
    b1 = []
    while len(s) % 3 != 0:
        s += " "
    for i in range(0, int(len(s)/3)):
        b2 = s[3*i:3*i+3]
        a, b4, b3 = str(ord(b2[0])), str(ord(b2[1])), str(ord(b2[2]))
        while len(b4) != 3:
            b4 = "0" + b4
        while len(b3) != 3:
            b3 = "0" + b3
        b5 = int(a + b4 + b3)
        b1.append(fonk2(b5, e, n))
    return b1
def fonk2(m, dee, en):
    b6 = str(bin(dee)).lstrip("0b")
    b6 = b6[::-1]
    b4 = []
    for i in range(0, len(b6)):
        b4.append(int(b6[i]))
    b7 = [m]
    for i in range(1, len(b6)):
        b7.append((b7[i-1] ** 2) % en)
    a1 = 1
    for i in range(0, len(b6)):
        if b4[i] == 1:
            a1 = (a1 * b7[i]) % en
    return a1
def fonk3():
    while True:
        b8 = input("Enter a message here (or enter \"quit\" to quit): ")
        if b8.lower() == "quit":
            break
        b9 = input("Enter an n value: ")
        while not b9.isnumeric():
            print("Please enter an integer value")
            b9 = input("Enter an n value: ")
        b9 = int(b9)
        b10 = input("Enter an e value: ")
        while not b10.isnumeric():
            print("Please enter an integer value")
            b10 = input("Enter an e value: ")
        b10 = int(b10)
        print(fonk1(b8, b10, b9))
if b11 = = "__main__":
    fonk3()