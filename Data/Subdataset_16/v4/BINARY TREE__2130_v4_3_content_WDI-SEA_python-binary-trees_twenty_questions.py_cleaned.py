import shelve
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
class class2:
    def fonk2(self):
        self.b4 = class1("hippo")
    def fonk3(self):
        print("Welcome to 20 Questions.")
        self.b4 = self.fonk4(self.b4)
    def fonk4(self, node):
        if node.b2 is None and node.b3 is None:
            print("You're thinking of:", node.b1)
            b5 = input("Is this correct? (y/n): ").strip().lower()
            if b5 = = "y":
                print("I win!!")
                return node
            else:
                return self.fonk5(node)
        else:
            print(node.b1)
            b5 = input("y/n: ").strip().lower()
            if b5 = = "y":
                node.b3 = self.fonk4(node.b3)
            elif b5 = = "n":
                node.b2 = self.fonk4(node.b2)
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
                return self.fonk4(node)
            return node
    def fonk5(self, old_node):
        b6 = input("Enter the thing you were thinking of: ").strip()
        b7 = input("Enter your disambiguating b7: ").strip()
        b8 = input("Enter 'y' if the answer to your b7 for your thing is 'yes', otherwise enter 'n': ").strip().lower()
        b9 = class1(b6)
        b10 = class1(b7)
        if b8 = = "y":
            b10.b3 = b9
            b10.b2 = old_node
        elif b8 = = "n":
            b10.b3 = old_node
            b10.b2 = b9
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            return self.fonk5(old_node)
        return b10
def fonk6():
    b11 = shelve.open("b12.save")
    if "tree" in b11:
        b12 = b11["tree"]
    else:
        b12 = class2()
    b12.fonk3()
    b13 = True
    while b13:
        b11["tree"] = b12
        b5 = input("Do you want to play again? (y/n): ").strip().lower()
        if b5 = = "y":
            b12.fonk3()
        elif b5 = = "n":
            print("Thanks for playing! Goodbye.")
            b13 = False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    b11.close()
if b14 = = "__main__":
    fonk6()