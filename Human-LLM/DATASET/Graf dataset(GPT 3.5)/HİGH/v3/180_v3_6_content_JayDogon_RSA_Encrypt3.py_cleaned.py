def fonk1(b8, b10, b9):
    b1 = fonk2(b8)
    b2 = []
    for i in range(0, len(b1), 3):
        b3 = b1[i:i+3]
        b4 = [str(ord(char)).zfill(3) for char in b3]
        b5 = int("".join(b4))
        b2.append(fonk3(b5, b10, b9))
    return b2
def fonk2(b8):
    while len(b8) % 3 != 0:
        b8 += " "
    return b8
def fonk3(base, exponent, modulus):
    b6 = bin(exponent)[2:][::-1]
    b7 = [base]
    for _ in range(1, len(b6)):
        b7.append((b7[-1] ** 2) % modulus)
    a1 = 1
    for i in range(len(b6)):
        if b6[i] == '1':
            a1 = (a1 * b7[i]) % modulus
    return a1
def fonk4():
    while True:
        b8 = input("Enter a b8 here (or enter \"quit\" to quit): ")
        if b8.lower() == "quit":
            break
        b9 = int(input("Enter an n value: "))
        while True:
            try:
                b10 = int(input("Enter an e value: "))
                break
            except ValueError:
                print("Please enter an integer value")
        b11 = fonk1(b8, b10, b9)
        print(b11)
if b12 = = "__main__":
    fonk4()