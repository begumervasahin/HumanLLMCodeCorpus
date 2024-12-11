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
    def fonk3(self, b11):
        b5 = self.b4
        for letter in b11:
            b6 = class1(letter)
            b5.b3 = b6
            b5 = b5.b3
    def fonk4(self):
        b5 = self.b4.b3
        print()
        while b5 is not None:
            print(b5.b2, b7 = "")
            b5 = b5.b3
        print()
    def fonk5(self, letter, b12):
        b8 = False
        b5 = self.b4.b3
        while b5 is not None:
            if b5.b1 = = letter:
                b5.b2 = letter
                b8 = True
            b5 = b5.b3
        if not b8:
            b12.pop(0)
        b5 = self.b4.b3
        while b5 is not None:
            print(b5.b2, b7 = "")
            b5 = b5.b3
        print(b12)
    def fonk6(self):
        b5 = self.b4.b3
        print("ANSWER IS...")
        time.sleep(2.0)
        while b5 is not None:
            print(b5.b1, b7 = "")
            b5 = b5.b3
def fonk7():
    b9 = class2()
    print("Type 'view' to view the answer")
    print("Type 'exit' to EXIT")
    b10 = [
        "python", "jumble", "easy", "difficult", "computer", "b12", "failure", "brilliant", "worthy",
        "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery",
        "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown",
        "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw",
        "mnemonic", "pneumonia", "peekaboo", "diarrhoea", "jaundice", "gossip", "despacito"
    ]
    b11 = [random.choice(b10)]
    b9.fonk3(b11)
    b9.fonk4()
    b12 = ["H", "A", "N", "G", "M", "A", "N"]
    while len(b12) != 0:
        b13 = input()
        if b13 != "exit" and b13 != "view":
            b9.fonk5(b13, b12)
        elif b13 = = "view":
            b9.fonk6()
            break
        elif b13 = = "exit":
            print("Exiting...")
            break
def fonk8():
    return input("Do you want to play again? (yes/no): ").lower()
def fonk9():
    fonk7()
    while fonk8() == "yes":
        fonk7()
if b14 = = "__main__":
    fonk9()