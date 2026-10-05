class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
    def fonk2(self, plaintext):
        return pow(plaintext, self.b1, self.b2)
def fonk3(u, v):
    a, b3 = u, v
    x, b4 = 0, 1
    while a != 0:
        b5 = b3
        a, b3 = b3 - b5 * a, a
        x, b4 = b4 - b5 * x, x
    return b4 % v
def fonk4(prime_p, prime_q):
    b6 = (prime_p - 1) * (prime_q - 1)
    b2 = prime_p * prime_q
    a1 = 65537
    b7 = fonk3(a1, b6)
    b8 = class1(b1=a1, b2=b2)
    b9 = class1(b1=b7, b2=b2)
    return b8, b9
def fonk5():
    b8, b9 = fonk4(23, 29)
    a2 = 42
    b10 = b8.fonk2(a2)
    b11 = b9.fonk2(b10)
    print("Original:", a2)
    print("Encrypted:", b10)
    print("Decrypted:", b11)
if b12 = = '__main__':
    fonk5()