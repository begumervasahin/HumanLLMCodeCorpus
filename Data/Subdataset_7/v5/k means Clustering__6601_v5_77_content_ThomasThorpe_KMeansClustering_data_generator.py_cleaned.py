import csv
import random
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        with open(self.b5, 'w', b6 = '\n') as csvfile:
            b7 = csv.b7(csvfile, delimiter=',')
            for _ in range(self.b2):
                b8 = [random.uniform(self.b3, self.b4) for _ in range(self.b1)]
                b7.writerow(b8)
if b9 = = "__main__":
    b1 = random.randint(2, 5)
    b2 = random.randint(10000, 100000)
    b3 = -10
    b4 = 10
    b5 = "data.csv"
    b10 = class1(b1, b2, b3, b4, b5)
    b10.fonk2()