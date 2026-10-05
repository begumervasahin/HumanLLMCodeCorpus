def fonk1(b5, exponent, modulus):
    b1 = fonk2(b5)
    b2 = [fonk4(block, exponent, modulus) for block in fonk3(b1)]
    return b2
def fonk2(b5, b3 = 3):
    while len(b5) % b3 != 0:
        b5 += " "
    return b5
def fonk3(b5, b3 = 3):
    return [b5[i:i + b3] for i in range(0, len(b5), b3)]
def fonk4(block, exponent, modulus):
    b4 = sum((ord(char) * (1000 ** idx) for idx, char in enumerate(reversed(block))))
    return pow(b4, exponent, modulus)
def fonk5():
    while True:
        b5 = input("Enter a b5 here (or enter 'quit' to quit): ")
        if b5.lower() == "quit":
            break
        b6 = int(input("Enter the modulus value (b6): "))
        b7 = int(input("Enter the exponent value (b7): "))
        b8 = fonk1(b5, b7, b6)
        print("Encrypted b5:", b8)
if b9 = = "__main__":
    fonk5()