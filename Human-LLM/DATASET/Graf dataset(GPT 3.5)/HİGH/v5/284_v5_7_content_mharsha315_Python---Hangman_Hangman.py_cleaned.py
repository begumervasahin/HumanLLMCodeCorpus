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
    def fonk3(self, word):
        b5 = self.b4
        for letter in word:
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
    def fonk5(self, letter, b13):
        b8 = False
        b5 = self.b4.b3
        while b5 is not None:
            if b5.b1 = = letter:
                b5.b2 = letter
                b8 = True
            b5 = b5.b3
        if not b8:
            b13.pop(0)
        self.fonk4()
        print(b13)
    def fonk6(self):
        b5 = self.b4.b3
        print("ANSWER IS...")
        time.sleep(2.0)
        while b5 is not None:
            print(b5.b1, b7 = "")
            b5 = b5.b3
def fonk7():
    b9 = class2()
    print("Type 'view' to view answer")
    print("Type 'exit' to EXIT")
    b10 = ["python", "jumble", "easy", "difficult", "computer", "b13", "failure", "brilliant", "worthy",
             "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento",
             "mystery", "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak",
             "zippy", "unknown", "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin",
             "witchcraft", "rickshaw", "mnemonic", "pneumonia", "peekaboo", "diarrhoea", "jaundice", "gossip",
             "despacito"]
    b11 = random.choice(b10)
    b9.fonk3(b11)
    b9.fonk4()
    b12 = None
    b13 = ["H", "A", "N", "G", "M", "A", "N"]
    while b12 not in ["exit", "view"] and len(b13) != 0:
        b12 = input()
        if b12 != "exit" and b12 != "view":
            b9.fonk5(b12, b13)
        elif b12 = = "view":
            b9.fonk6()
            break
        elif b12 = = "exit":
            print("Exiting...")
            break
fonk7()
def fonk8():
    print()
    print("1. PLAY AGAIN")
    return input("Do you want to play again? (yes/no): ").strip().lower()
while True:
    b14 = fonk8()
    if b14 in ["yes", "y"]:
        fonk7()
    else:
        break