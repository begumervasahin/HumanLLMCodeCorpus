import random
import time
class class1:
    def fonk1(self, b1 = "-", b2="-"):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = class1()
    def fonk3(self, b12):
        b5 = len(b12)
        b6 = self.b4
        for i in range(b5):
            b7 = class1(b12[i])
            b6.b3 = b7
            b6 = b6.b3
    def fonk4(self):
        b6 = self.b4.b3
        print()
        while b6 is not None:
            print(b6.b2, b8 = "")
            b6 = b6.b3
        print()
    def fonk5(self, letter, b13):
        b9 = False
        b6 = self.b4.b3
        while b6 is not None:
            if b6.b1 = = letter:
                b6.b2 = letter
                b9 = True
            b6 = b6.b3
        if not b9:
            b13.pop(0)
        b6 = self.b4.b3
        while b6 is not None:
            print(b6.b2, b8 = "")
            b6 = b6.b3
        print(b13)
    def fonk6(self):
        b6 = self.b4.b3
        print("ANSWER IS...")
        time.sleep(2.0)
        while b6 is not None:
            print(b6.b1, b8 = "")
            b6 = b6.b3
def fonk7():
    b10 = class2()
    print("Type 'view' to view answer")
    print("Type 'exit' to EXIT")
    b11 = [
        "python", "jumble", "easy", "difficult", "computer", "b13", "failure", "brilliant", "worthy",
        "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery",
        "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown",
        "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw",
        "mnemonic", "pneumonia", "peekaboo", "diarrhoea", "jaundice", "gossip", "despacito"
    ]
    b12 = [random.choice(b11)]
    b10.fonk3(b12)
    b10.fonk4()
    b13 = ["H", "A", "N", "G", "M", "A", "N"]
    while len(b13) != 0:
        b14 = input()
        if b14 != "exit" and b14 != "view":
            b10.fonk5(b14, b13)
        elif b14 = = "view":
            b10.fonk6()
            break
        elif b14 = = "exit":
            print("Exiting...")
            break
fonk7()
b15 = input("Do you want to play again? (yes/no): ").lower()
while b15 = = "yes":
    fonk7()
    b15 = input("Do you want to play again? (yes/no): ").lower()