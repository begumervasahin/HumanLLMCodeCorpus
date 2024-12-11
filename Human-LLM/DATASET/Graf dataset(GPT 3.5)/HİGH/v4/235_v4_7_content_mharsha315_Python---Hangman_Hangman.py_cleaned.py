class class1:
    def fonk1(self, b1 = "-", b2="-"):
        self.b1 = b1
        self.b2 = b2
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = class1()
    def fonk3(self, word):
        b5 = len(word)
        b6 = self.b4
        a1 = 0
        while a1 < b5:
            b7 = class1(word[a1])
            b6.b3 = b7
            b6 = b6.b3
            a1 += 1
    def fonk4(self):
        b6 = self.b4.b3
        print()
        while b6 is not None:
            print(b6.b2, b8 = "")
            b6 = b6.b3
        print()
    def fonk5(self, letter, b13):
        a2 = 0
        b6 = self.b4.b3
        while b6 is not None:
            if b6.b1 = = letter:
                b6.b2 = letter
                a2 = 1
            b6 = b6.b3
        if a2 = = 0:
            b13.pop(0)
        b6 = self.b4.b3
        while b6 is not None:
            print(b6.b2, b8 = "")
            b6 = b6.b3
        print(b13)
    def fonk6(self):
        import time
        b6 = self.b4.b3
        print("ANSWER IS...")
        time.sleep(2.0)
        while b6 is not None:
            print(b6.b1, b8 = "")
            b6 = b6.b3
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
    import random
    b11 = random.choice(b10)
    b9.fonk3(b11)
    b9.fonk4()
    b12 = None
    b13 = ["H", "A", "N", "G", "M", "A", "N"]
    while (b12 != "exit" and b12 != "view") and len(b13) != 0:
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
b14 = None
while b14 != "no":
    print()
    print("1. PLAY AGAIN")
    b14 = input("Do you want to play again? (yes/no): ")
    if b14.lower() in ["yes", "y"]:
        fonk7()
    else:
        break