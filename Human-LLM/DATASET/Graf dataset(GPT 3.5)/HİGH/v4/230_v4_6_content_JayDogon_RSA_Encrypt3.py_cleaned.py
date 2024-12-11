def fonk1(b4, b6, b5):
    b1 = fonk2(b4)
    b2 = []
    for i in range(0, len(b1), 3):
        b3 = b1[i:i + 3]
        b2.append(fonk3(b3, b6, b5))
    return b2
def fonk2(b4):
    while len(b4) % 3 != 0:
        b4 += " "
    return b4
def fonk3(b3, b6, b5):
    a1 = 0
    for char in b3:
        a1 = (a1 * 1000) + ord(char)
    a1 = pow(a1, b6, b5)
    return a1
def fonk4():
    while True:
        b4 = input("Enter a b4 here (or enter 'quit' to quit): ")
        if b4.lower() == "quit":
            break
        b5 = int(input("Enter the value of 'b5': "))
        b6 = int(input("Enter the value of 'b6': "))
        b7 = fonk1(b4, b6, b5)
        print("Encrypted b4:", b7)
if b8 = = "__main__":
    fonk4()