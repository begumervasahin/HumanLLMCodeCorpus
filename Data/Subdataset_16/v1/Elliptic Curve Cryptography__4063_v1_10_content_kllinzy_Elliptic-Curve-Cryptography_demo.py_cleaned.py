import random
class class1:
    def fonk1(self, b1, b2, b3):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
    @staticmethod
    def fonk2(b1, b2):
        b3 = (random.fonk5(1, b1-1), random.fonk5(1, b1-1))
        return class1(b1, b2, b3)
    def fonk3(self):
        return f"Public Key:\nPrime: {self.b1}\nKey: {self.b2}\nGenerator: {self.b3}"
def fonk4(b6, b7):
    b4 = [num for num in range(b6, b7) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
    return random.choice(b4)
def fonk5(b6, b7):
    return random.fonk5(b6, b7)
def fonk6(message, b8):
    return [(ord(char) * b8.b2) % b8.b1 for char in message]
def fonk7(encrypted_message, b8, b2):
    return ''.join([chr((char * pow(b2, -1, b8.b1)) % b8.b1) for char in encrypted_message])
def fonk8():
    print("Elliptic Curve Cryptosystem: written by Kyle Linzy")
    print("*Note* press ctrl-c to exit the loop and the demo")
    print()
    b5 = int(input("Enter a number of digits for the prime number (i.e. 3 => 100 < prime < 1000).\nMinimum is 6 \nNumber of Zeros = "))
    if b5 < 6:
        b5 = 6
    b6 = 10 ** (b5 - 1)
    b7 = b6 * 10
    b1 = fonk4(b6, b7)
    b2 = fonk5(1, b1 - 1)
    b8 = class1.fonk2(b1, b2)
    print(b8)
    print()
    while True:
        b9 = input("Enter a message to be b10\n")
        print()
        b10 = fonk6(b9, b8)
        print("Encrypted array of points on the curve:\n", b10)
        print()
        print("Decrypted string:\n", fonk7(b10, b8, b2))
        print()
if b11 = = "__main__":
    fonk8()