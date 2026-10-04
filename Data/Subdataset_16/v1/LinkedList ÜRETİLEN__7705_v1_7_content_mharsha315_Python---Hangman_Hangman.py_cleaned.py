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
        print("\nCurrent state of the word:")
        while b5:
            print(b5.b2, b7 = " ")
            b5 = b5.b3
        print()
    def fonk5(self, guess, b11):
        a1 = 0
        b5 = self.b4.b3
        while b5:
            if b5.b1 = = guess:
                b5.b2 = guess
                a1 = 1
            b5 = b5.b3
        if not a1:
            b11.pop(0)
        self.fonk4()
        print("Remaining chances: ", ''.join(b11))
    def fonk6(self):
        b5 = self.b4.b3
        print("ANSWER IS...")
        time.sleep(2.0)
        while b5:
            print(b5.b1, b7 = " ")
            b5 = b5.b3
        print()
def fonk7():
    b8 = class2()
    print("Type 'view' to view answer")
    print("Type 'exit' to EXIT")
    b9 = ["python", "jumble", "easy", "difficult", "computer", "b11", "failure", "brilliant", "worthy",
             "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery",
             "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown",
             "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw",
             "mnemonic", "pneumonia", "peekaboo", "diarrhea", "jaundice", "gossip", "despacito"]
    b10 = random.choice(b9)
    b8.fonk3(b10)
    b8.fonk4()
    b11 = ["H", "A", "N", "G", "M", "A", "N"]
    while True:
        b12 = input("Enter your guess or command: ").strip().lower()
        if b12 = = "exit":
            print("Exiting...")
            break
        elif b12 = = "view":
            b8.fonk6()
            break
        elif len(b11) == 0:
            print("You've run out of chances!")
            b8.fonk6()
            break
        else:
            b8.fonk5(b12, b11)
if b13 = = "__main__":
    fonk7()
    while True:
        b14 = input("Do you want to play again? (yes/no): ").strip().lower()
        if b14 = = "yes":
            fonk7()
        else:
            print("Thank you for playing!")
            break