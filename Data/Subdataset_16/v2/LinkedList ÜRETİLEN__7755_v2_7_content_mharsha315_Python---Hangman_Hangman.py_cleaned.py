import random
import time
class class1:
    def fonk1(self, b1 = "-", b5="-"):
        """
        Initialize a new node with the given b1.
        Args:
            b1: The character to store in the node.
            b5: The character to display in the b2 state. Default is "-".
        Initialize a new b6 with an empty linked list.
        Insert the given word into the linked list.
        Args:
            word: The word to insert into the linked list.
        Display the b2 state of the word.
        """
        b2 = self.head.next
        print("\nCurrent state of the word:")
        while b2:
            print(b2.b5, b3 = " ")
            b2 = b2.next
        print()
    def fonk2(self, guess, b9):
        b4 = False
        b2 = self.head.next
        while b2:
            if b2.b1 = = guess:
                b2.b5 = guess
                b4 = True
            b2 = b2.next
        if not b4:
            b9.pop(0)
        self.display()
        print("Remaining chances: ", ''.join(b9))
    def fonk3(self):
        b2 = self.head.next
        print("ANSWER IS...")
        time.sleep(2.0)
        while b2:
            print(b2.b1, b3 = " ")
            b2 = b2.next
        print()
def fonk4():
    b6 = Game()
    b7 = [
        "python", "jumble", "easy", "difficult", "computer", "b9", "failure", "brilliant", "worthy",
        "xylophone", "awkward", "gypsy", "jinx", "burglar", "bankrupt", "crisis", "hyphen", "memento", "mystery",
        "pajama", "pixel", "rogue", "rhythmic", "twelfth", "jealous", "zombie", "yacht", "yak", "zippy", "unknown",
        "battleground", "player", "psycho", "beast", "buzzard", "boycott", "coffin", "witchcraft", "rickshaw",
        "mnemonic", "pneumonia", "peekaboo", "diarrhea", "jaundice", "gossip", "despacito"
    ]
    b8 = random.choice(b7)
    b6.insert(b8)
    b6.display()
    b9 = ["H", "A", "N", "G", "M", "A", "N"]
    while True:
        b10 = input("Enter your guess or command (view/exit): ").strip().lower()
        if b10 = = "exit":
            print("Exiting...")
            break
        elif b10 = = "view":
            b6.fonk3()
            break
        elif len(b9) == 0:
            print("You've run out of chances!")
            b6.fonk3()
            break
        else:
            b6.fonk2(b10, b9)
def fonk5():
    while True:
        fonk4()
        b11 = input("Do you want to play again? (yes/no): ").strip().lower()
        if b11 != "yes":
            print("Thank you for playing!")
            break
if b12 = = "__main__":
    fonk5()