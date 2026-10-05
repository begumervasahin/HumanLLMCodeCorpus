from string import ascii_uppercase, ascii_lowercase
from random import choice, random
b1 = "METHINKS IT IS LIKE A WEASEL"
b2 = ascii_uppercase + ascii_lowercase + ' '
class class1:
    def fonk1(self, b4, b5, b3 = 0.09, b7=b13):
        self.b4 = b4
        self.b5 = b5
        self.b6 = [choice(self.b5) for _ in range(len(self.b4))]
        self.b3 = b3
        self.b7 = b7
        self.b8 = float(len(self.b4))
    def fonk2(self, trial):
        return sum(b9 = = h for b9, h in zip(trial, self.b4))
    def fonk3(self):
        return 1 - ((self.b8 - self.fonk2(self.b6)) / self.b8 * (1 - self.b3))
    def fonk4(self, b6, b12):
        return [(ch if random() <= b12 else choice(self.b5)) for ch in b6]
    def fonk5(self, a, b):
        b10 = choice(range(len(self.b4))) if choice(range(10)) < 7 else 0
        return a, b, a[:b10] + b[b10:], b[:b10] + a[b10:]
    def fonk6(self):
        a1 = 0
        b11 = len(range(self.b7))
        while self.b6 != list(self.b4):
            b12 = self.fonk3()
            a1 += 1
            if a1 % b13 = = 0:
                self.fonk7(a1)
            b14 = [self.fonk4(self.b6, b12) for _ in range(self.b7)] + [self.b6]
            b15 = max(b14[:b11], key=self.fitness)
            b16 = max(b14[b11:], key=self.fitness)
            self.b6 = max(self.fonk5(b15, b16), key=self.fitness)
        self.fonk7(a1)
    def fonk7(self, a1):
        print("(a1: {}, fitness: {:.2f}%, b6: {})".format(a1, self.fonk2(self.b6) * b13. / self.b8, ''.join(self.b6)))
if b17 = = "__main__":
    b18 = class1(b1, b2)
    b18.fonk6()