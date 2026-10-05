def fonk1(b7, b9, b8):
    b1 = []
    while len(b7) % 3 != 0:
        b7 += " "
    for i in range(0, len(b7)
        b2 = b7[3*i:3*i+3]
        b3 = [str(ord(char)) for char in b2]
        b3 = [("0" * (3 - len(val)) + val) for val in b3]
        b4 = int("".join(b3))
        b1.append(fonk2(b4, b9, b8))
    return b1
def fonk2(base, exponent, modulus):
    b5 = bin(exponent)[2:][::-1]
    b6 = [base]
    for i in range(1, len(b5)):
        b6.append((b6[-1] ** 2) % modulus)
    a1 = 1
    for i in range(len(b5)):
        if b5[i] == '1':
            a1 = (a1 * b6[i]) % modulus
    return a1
def fonk3():
    while True:
        b7 = input("Enter a b7 here (or enter \"quit\" to quit): ")
        if b7.lower() == "quit":
            break
        b8 = int(input("Enter an n value: "))
        while True:
            try:
                b9 = int(input("Enter an e value: "))
                break
            except ValueError:
                print("Please enter an integer value")
        b10 = fonk1(b7, b9, b8)
        print(b10)
if b11 = = "__main__":
    fonk3()