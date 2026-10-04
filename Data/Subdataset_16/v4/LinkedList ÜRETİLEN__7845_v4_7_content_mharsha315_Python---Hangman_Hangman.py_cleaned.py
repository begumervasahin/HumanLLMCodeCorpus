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
        for char in word:
            b6 = class1(char)
            b5.b3 = b6
            b5 = b5.b3
    def fonk4(self):
        b5 = self.b4.b3
        print("\n", b7 = "")
        while b5 is not None:
            print(b5.b2, b7 = "")
            b5 = b5.b3
        print()
    def fonk5(self, guess, b12):
        b8 = False
        b5 = self.b4.b3
        while b5 is not None:
            if b5.b1 = = guess:
                b5.b2 = guess
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
        print()
def fonk7():
    b9 = class2()
    print("Type 'view' to view answer")
    print("Type 'exit' to EXIT")
    b10 = [
        "python", "jumble", "easy", "difficult", "computer", "hangman", "failure", "brilliant", "worthy", "xylophone",
        "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery", "pajama", "pixel",
        "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown", "battleground",
        "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw", "mnemonic", "pneumonia",
        "peekaboo", "diarrhea", "jaundice", "gossip", "despacito"
    ]
    b11 = random.choice(b10)
    b9.fonk3(b11)
    b9.fonk4()
    b12 = ["H", "A", "N", "G", "M", "A", "N"]
    while len(b12) != 0:
        b13 = input().strip().lower()
        if b13 = = "exit":
            print("Exiting...")
            break
        elif b13 = = "view":
            b9.fonk6()
            break
        else:
            b9.fonk5(b13, b12)
def fonk8():
    print("Welcome to Hangman!")
    b14 = "yes"
    while b14.lower() == "yes":
        fonk7()
        b14 = input("Do you want to play again? (yes/no): ").strip().lower()
    print("Thank you for playing!")
if b15 = = "__main__":
    fonk8()