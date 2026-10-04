import random
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    @staticmethod
    def fonk2(b1, b2):
        b3 = (random.randint(1, b1 - 1), random.randint(1, b1 - 1))
        return class1(b1, b2, b3)
    def fonk3(self):
        return f"Public Key:\nPrime: {self.b1}\nKey: {self.b2}\nGenerator: {self.b3}"
def fonk4(b6, b7):
    b4 = [num for num in range(b6, b7) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return random.choice(b4)
def fonk5(b10, b9):
    return [(ord(char) * b9.b2) % b9.b1 for char in b10]
def fonk6(b11, b9, b8):
    return ''.join([chr((char * pow(b8, -1, b9.b1)) % b9.b1) for char in b11])
def fonk7():
    print("Elliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* Press Ctrl-C to exit the loop and the demo")
    print()
    b5 = int(input("Enter a number of digits for the b1 number (i.e. 3 => 100 < b1 < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if b5 < 6:
        b5 = 6
    b6 = 10 ** (b5 - 1)
    b7 = b6 * 10
    b1 = fonk4(b6, b7)
    b8 = random.randint(1, b1 - 1)
    b9 = class1.fonk2(b1, b8)
    print(b9)
    print()
    while True:
        b10 = input("Enter a b10 to be encrypted\n")
        print()
        b11 = fonk5(b10, b9)
        print("Encrypted array of points on the curve:\n", b11)
        print()
        b12 = fonk6(b11, b9, b8)
        print("Decrypted string:\n", b12)
        print()
if b13 = = "__main__":
    fonk7()